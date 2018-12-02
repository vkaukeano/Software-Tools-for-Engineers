#include "mytest.h"

// declare statics
//
const char* Mytest::NAME = "Mytest";


// method debug
//
long Mytest::debug(FILE* arg){
	printf("the value of debug_level_d is %u\n", debug_level_d);
	return 0;
}
