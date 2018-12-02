# file:GNUMakefile
#

# define a traget for the application
#
all: mytest.exe

# define a target to link the application
#
mytest.exe: mytest.o mytest_00.o
	    g++ -O3 -ggdb -lm mytest.o mytest_00.o -o mytest.exe

# define targets to compile the source code
#
mytest.o: mytest.cc mytest.h makefile
	g++ -O3 -ggdb -c mytest.cc -o mytest.o

mytest_00.o: mytest_00.cc mytest.h makefile
	g++ -O3 -ggdb -c mytest_00.cc -o mytest_00.o

# define target to clean the directory
#
clean:
	rm -f mytest.exe mytest.o mytest_00.o

#
# end of file