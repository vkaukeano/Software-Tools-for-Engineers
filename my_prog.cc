#include<stdio.h>
#include<stdlib.h>

int read_data(float *val, FILE** fp, const char *type);

int main(int argc, char *argv[]){

 float sum = 0;
 int i = 0;
 float val;
 bool status = true;
 FILE* fp = fopen(argv[1], "r");
 while (fread(&val,sizeof(char),1,fp) != 0) {
 status = read_data(&sum, &fp, "char");
 i++;
 sum += val;
 }
 
 fclose(fp);
 printf("The number of elements read was %d\n", i);
 printf("The sum of these elements is %d\n\n", sum);

 i = 0;
 fp = fopen(argv[1], "r");
 while (fread(&val,sizeof(short int),1,fp) != 0) {
 status = read_data((float*)&sum, &fp,"short int");
 i++;
 sum += val;
 }
 fclose(fp);
 printf("The number of elements read was %d\n", i);
 printf("The sum of these elements is %d\n\n", sum);
 
 i=0;
 fp = fopen(argv[1], "r");
 while (fread(&val,sizeof(float),1,fp) != 0) {
 status = read_data((float*)&sum, &fp, "float");
 i++;
 sum += val;
 }
 fclose(fp);

 printf("The number of elements read was %d\n", i);
 printf("The sum of these elements is %f\n\n", sum);

 return(0);
}

int read_data (float *val, FILE** fp, const char *type){
if(!fp){
printf("File could not be opened.\n");
}
return(1);
}
