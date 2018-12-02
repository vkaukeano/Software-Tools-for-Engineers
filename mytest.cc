#include "mytest.h"
#include <string.h>

int main (int argc, char ** argv){
	Mytest foo;
	printf("The class name is %s\n", foo.name());

// no arguments message
//
	if(argc<2){
		printf("No arguments.\n stopping program now...\n");
		return -1;
	}

// no value for debug flag message, preventing seg fault
//
if(argc<3){
	printf("There is no value set for -debug flag.\n stopping program now...");
	return -1;
}

// check for debug flag, if found then proceed
//
	if(strcmp(argv[1],"-debug")==0){

		if(strcmp(argv[2], "full")==0 || strcmp(argv[2], "partial")==0 ||
			strcmp(argv[2], "brief")==0 || strcmp(argv[2], "none")==0){

				// valid input exists, procced
				//
				printf("The debug level is set to %s\n", argv[2]);

				//copy command line arguments to foo
				//
				foo.strs[0] = new char[strlen(argv[1])+1];
				strcpy(foo.strs[0], argv[1]);

				foo.strs[1] = new char[strlen(argv[2])+1];
				strcpy(foo.strs[1], argv[2]);

				// full debug
				//
				if(strcmp(argv[2],"full")==0){

					printf("full worked\n");
					printf("command line args: %s, %s\n", foo.strs[0], foo.strs[1]);
					foo.set_debug(Mytest::FULL);
					foo.debug(stdout);
					
					// print all algorithms
					printf("\ncompute_1 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_1);

					printf("\ncompute_2 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_2);

					printf("\ncompute_3 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_3);

					return 0;
				}

				// partial debug
				else if(strcmp(argv[2],"partial")==0){

					printf("partial worked\n");
					printf("command line args: %s, %s\n", foo.strs[0], foo.strs[1]);
					foo.set_debug(Mytest::PARTIAL);
					foo.debug(stdout);
					
					// print two algorithms
					printf("\ncompute_1 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_1);

					printf("\ncompute_2 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_2);

					return 0;
				}

				// breif debug
				else if(strcmp(argv[2],"brief")==0){

					printf("brief worked\n");
					printf("command line args: %s, %s\n", foo.strs[0], foo.strs[1]);
					foo.set_debug(Mytest::BRIEF);
					foo.debug(stdout);
					
					// print one algorithms
					printf("\ncompute_1 is below\n");
					foo.set_algorithm(Mytest::COMPUTE_1);

					return 0;
				}

				// none debug
				else if(strcmp(argv[2],"none")==0){

					foo.set_debug(Mytest::BRIEF);
					
					// print none message
					printf("\nnone flag used. that's lame...\n");

					return 0;
				}

				else{
					printf("Invalid value used for the -debug flag! try again...");
					return -1;
				}


			}
}

else{
	//printf("Input1: %s or Input2: %s are incorrect\n", argv[1], argv[2]);
	return -1;
}

	return 0;
}