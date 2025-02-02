import os
import json
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from cryptography.fernet import Fernet

# Kunci untuk enkripsi
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

VIRUS_SIGNATURES_FILE = "virus_signatures.json"  # File untuk menyimpan tanda tangan virus
QUARANTINE_FOLDER = "quarantine"
LOG_FILE = "scan_log.txt"

# Fungsi untuk memuat tanda tangan virus dari file
def load_signatures():
    if os.path.exists(VIRUS_SIGNATURES_FILE):
        with open(VIRUS_SIGNATURES_FILE, 'r') as f:
            return json.load(f)
    else:
        return ["This is infected by the virus!"]  # Default signature jika file tidak ada

# Fungsi untuk menyimpan tanda tangan virus ke dalam file
def save_signatures():
    with open(VIRUS_SIGNATURES_FILE, 'w') as f:
        json.dump(VIRUS_SIGNATURES, f)

# Memuat tanda tangan virus saat aplikasi dimulai
VIRUS_SIGNATURES = load_signatures()

# Fungsi untuk memindai file
def scan_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            for signature in VIRUS_SIGNATURES:
                if signature in content:
                    return True
    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")
    return False

# Fungsi untuk memindai direktori dan mencari file terinfeksi
def scan_directory(directory):
    infected_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                infected_files.append(file_path)
    return infected_files

# Fungsi untuk mengkarantina file dengan enkripsi
def quarantine_files(files):
    if not os.path.exists(QUARANTINE_FOLDER):
        os.makedirs(QUARANTINE_FOLDER)
    for file in files:
        try:
            with open(file, 'rb') as f:
                data = f.read()
            encrypted_data = cipher.encrypt(data)
            with open(os.path.join(QUARANTINE_FOLDER, os.path.basename(file)), 'wb') as f:
                f.write(encrypted_data)
            os.remove(file)
        except Exception as e:
            print(f"Failed to quarantine {file}: {e}")

# Fungsi untuk mencatat log
def write_log(infected_files):
    with open(LOG_FILE, 'a') as log:
        log.write(f"Scan Date: {datetime.now()}\n")
        if infected_files:
            log.write(f"Infected Files ({len(infected_files)}):\n")
            for file in infected_files:
                log.write(f" - {file}\n")
        else:
            log.write("No infected files found.\n")
        log.write("=" * 50 + "\n")

# Fungsi untuk menambahkan tanda tangan virus
def add_to_database():
    signature = new_signature.get()
    if signature:
        if signature not in VIRUS_SIGNATURES:
            VIRUS_SIGNATURES.append(signature)
            save_signatures()  # Simpan tanda tangan baru ke dalam file JSON
            messagebox.showinfo("Success", "New virus signature added to database.")
        else:
            messagebox.showwarning("Duplicate Signature", "This signature already exists.")
    else:
        messagebox.showwarning("Input Error", "Signature cannot be empty.")

# Fungsi untuk memulai pemindaian direktori
def start_scan():
    directory = filedialog.askdirectory(title="Select Directory to Scan")
    if not directory:
        return

    infected_files = scan_directory(directory)
    if infected_files:
        result_text.set(f"{len(infected_files)} infected files found!")
        results_list.delete(0, tk.END)
        for file in infected_files:
            results_list.insert(tk.END, file)
        quarantine_files(infected_files)
        write_log(infected_files)
        messagebox.showwarning("Scan Complete", f"Scan finished. {len(infected_files)} infected files found and quarantined!")
    else:
        result_text.set("No infected files found.")
        results_list.delete(0, tk.END)
        write_log([])
        messagebox.showinfo("Scan Complete", "Scan finished. No infected files found!")


# Fungsi untuk memindai file tunggal (upload and check)
def upload_and_check():
    file_path = filedialog.askopenfilename(title="Select File to Check")
    if not file_path:
        return
    if scan_file(file_path):
        messagebox.showwarning("Scan Result", f"The file '{os.path.basename(file_path)}' is infected!")
        quarantine_files([file_path])
    else:
        messagebox.showinfo("Scan Result", f"The file '{os.path.basename(file_path)}' is clean.")

# Root window
root = tk.Tk()
root.title("BlazeShield - Antivirus Application")
root.geometry("800x600")
root.configure(bg="#1e1e2f")

# Gaya untuk ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1e1e2f")
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10), padding=6)
style.map("TButton", background=[("active", "#ff5e57"), ("!active", "#ff6f61")], foreground=[("active", "white")])

# Frame utama
main_frame = ttk.Frame(root)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Header
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill="x")
header_label = ttk.Label(header_frame, text="\u26A1 BlazeShield Antivirus", font=("Arial", 20, "bold"), anchor="center")
header_label.pack(pady=10)

# Result label
result_text = tk.StringVar()
result_text.set("No results yet.")
result_label = ttk.Label(main_frame, textvariable=result_text, anchor="center", font=("Arial", 14, "italic"))
result_label.pack(pady=10)

# Scan buttons
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

scan_button = ttk.Button(button_frame, text="Scan Directory", command=start_scan, width=20)
scan_button.grid(row=0, column=0, padx=10, pady=10)

upload_button = ttk.Button(button_frame, text="Upload and Check File", command=upload_and_check, width=20)
upload_button.grid(row=0, column=1, padx=10, pady=10)

# Virus signature input
signature_frame = ttk.Frame(main_frame)
signature_frame.pack(pady=20)

signature_label = ttk.Label(signature_frame, text="Add New Virus Signature:")
signature_label.grid(row=0, column=0, padx=5, pady=5)

new_signature = tk.StringVar()
signature_entry = ttk.Entry(signature_frame, textvariable=new_signature, width=50)
signature_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = ttk.Button(signature_frame, text="Add to Database", command=add_to_database)
add_button.grid(row=0, column=2, padx=5, pady=5)

# Results list
results_label = ttk.Label(main_frame, text="Scan Results:")
results_label.pack(pady=10)

results_list = tk.Listbox(main_frame, width=80, height=10, bg="#2e2e3f", fg="white", font=("Courier", 10), selectbackground="#ff6f61", selectforeground="black")
results_list.pack(pady=10)

# Footer buttons
footer_frame = ttk.Frame(main_frame)
footer_frame.pack(pady=20)

exit_button = ttk.Button(footer_frame, text="Exit", command=root.quit, width=15)
exit_button.pack()

# Start main loop
root.mainloop()
