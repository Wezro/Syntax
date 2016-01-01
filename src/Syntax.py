# Main class for Syntax
import ProcessManager
import Error
import Objects
import sys

syntaxFile = "../example.syn"
cssPath = "../example.css"

workingDirectory = None


def getInput():
    args = raw_input("Syntax:")
    args = args.split()
    if (len(args) > 0):

        if (args[0] == "exit"):
            print "Closing Syntax."
            sys.exit(0)

        elif (args[0] == "dir"):
            if (args[1] != None):
                workingDirectory = args[1]

    getInput() #Get the users input again, incase they want to do somthing else.



def execute():
    with open(syntaxFile,"r") as syntaxLines:
        for line in syntaxLines:
            if not line.strip(): #Skip empty lines
                continue
            else:
                ProcessManager.process(line)

    #Objects.elements = Objects.combineList(Objects.elements) # This makes sure if there are any duplicates elements, they are combined.
    Objects.export(cssPath)
    Error.showErrors() #Return the errors


try:
    getInput()
except KeyboardInterrupt:
    print "\n Exiting Syntax"
