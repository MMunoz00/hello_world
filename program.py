#   Author:    Michael Munoz
#   Program:   Hello World
#   Created:   January 10th, 2024

#define main program function
def main():
    print("Hello World")            #basic print statement using a string

    default = "Hello World"         #set predefined string
    print(default)                  #basic print statement using an initialized variable

    #define secondary function with the purpose to only display a string determined from function parameter
    def Hello(text):
        print(text)                 #basic print statement using an implicit variable parameter

    Hello(default)                  #custom function with predefined variable as parameter
    Hello("Hello World")            #custom function with string as parameter

#running the program should display four identical Hello World statements using four different methods
main()