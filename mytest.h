// file: mytest.h
//

// make sure definitions are only made once
//
#ifndef MYTEST
#define MYTEST


// system include files
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#define MAX_ARGS 2

// Mytest:
//
class Mytest {
	//---------------------------------------------------------------------------
	//
	// public constants
	//
	//---------------------------------------------------------------------------
public:

	// define the class name
	//
	static const char* NAME;

	// define DEBUG_LEVEL choices
	//
	enum  DEBUG_LEVEL { FULL = 0, PARTIAL, BRIEF, NONE };

	// define ALGORITHM choices
	//
	enum  ALGORITHM { COMPUTE_1 = 0, COMPUTE_2, COMPUTE_3};

	// declare strs
	//
	char* strs[MAX_ARGS];

	//---------------------------------------------------------------------------
	//
	// protected data
	//
	//---------------------------------------------------------------------------
protected:
	//---------------------------------------------------------------------------
	//
	// required public methods
	//
	//---------------------------------------------------------------------------
	
	// declare a register to hold the current checksum
	//
	float sum_d;

	// declare a static debug level for all class instantiations
	//
	DEBUG_LEVEL debug_level_d;
	

	ALGORITHM algorithm;

	// compute methods
	//
	int COMPUTE_1val(){
		int x = 3;
		return x;
	}

	int COMPUTE_2val(){
		int x = 2;
		return x;
	}
	int COMPUTE_3val(){
		int x = 1;
		return x;
	}

public:

	// method: name
	//
	static const char* name() {
		return NAME;
	}

	// method: setDebug
	//
	bool set_debug(DEBUG_LEVEL level) {
		debug_level_d = level;
		return true;
	}

	// other constructor(s)
	//
	Mytest() {
		sum_d = 0.0;
	}

	// method: destructor
	//
	~Mytest() {
		//delete [] strs[0];
		//delete [] strs[1];
	};

	// method: copy constructor
	//
	Mytest(const Mytest& arg) {
		sum_d = arg.sum_d;
	}

	// method: debug
	//
	long debug(FILE* arg);

	// method: set_algorithm
	//
	bool set_algorithm(ALGORITHM a){
		algorithm = a; 
		switch(algorithm)
		{
			case COMPUTE_1: printf("blue\n"); break;
			case COMPUTE_2: printf("green\n"); break;
			case COMPUTE_3: printf("yellow\n"); break;
		}
		return true;
	}
	//---------------------------------------------------------------------------
	//
	// private methods
	//
	//---------------------------------------------------------------------------
private:

	// zero-out data in an algorithm dependent manner
	//
	bool reset() {
		sum_d = 0;
		return true;
  }
};

// end of include file
//
#endif