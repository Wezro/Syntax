# Main class for Syntax
import ProcessManager
import Error
import Objects
import sys
import os
import time

syntaxFile = "../example.syn"
cssPath = "../example.css"

fileSavedTime = os.stat(syntaxFile).st_mtime

workingDirectory = None



def execute():
    ProcessManager.init()
    with open(syntaxFile,"r") as syntaxLines:
        for line in syntaxLines:
            if not line.strip(): #Skip empty lines
                continue
            else:
                ProcessManager.process(line)

    #Objects.elements = Objects.combineList(Objects.elements) # This makes sure if there are any duplicates elements, they are combined.
    Objects.export(cssPath)
    Error.showErrors() #Return the errors



def getInput():
    global i
    args = raw_input("Syntax:")
    args = args.split()
    if (len(args) > 0 ):

        if (args[0] == "dir" and args[1] != None):
            if  os.path.isdir(workingDirectory):
                workingDirectory = args[1]

            else:
                print "Directory does not exist."

        elif (args[0] == "watch"):
            print "Watching for changes. Press (CTRL-C) to exit."
            while True:
                fileCurrentTime = os.stat(syntaxFile).st_mtime
                if (fileCurrentTime != fileSavedTime):
                    fileSavedTime = fileCurrentTime
                    execute()

    getInput() #Get the users input again, incase they want to do somthing else.





try:
    getInput()
except KeyboardInterrupt:
    print "\n Exiting Syntax"
