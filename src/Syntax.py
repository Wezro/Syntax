# Main class for Syntax
import ProcessManager
import Error
import Objects
import sys
import os
import time


syntaxFiles = []
workingDirectory = None


def execute(fileName):
    ProcessManager.init()
    with open(fileName,"r") as syntaxLines:
        for line in syntaxLines:
            print(line)
            if not line.strip(): #Skip empty lines
                continue
            else:
                ProcessManager.process(line)

    #Objects.elements = Objects.combineList(Objects.elements) # This makes sure if there are any duplicates elements, they are combined.
    print(fileName.strip(".syntax").strip(".syn") + ".css")
    Objects.export(fileName.replace(".syntax","").replace(".syn","") + ".css")
    Error.showErrors() #Return the errors
    syntaxLines.close()

def getFiles(folder):
    global syntaxFiles
    syntaxFiles = []
    for fileName in os.listdir(folder):
        if fileName.endswith(".syn") or fileName.endswith(".syntax") :
            filePath = folder + fileName # Have to add a extra slash, othwises Python thinks we are trying to escape the double quote.
            syntaxFiles.append({"path": filePath, "time": os.stat(filePath).st_mtime})


def getInput():
    global workingDirectory
    global syntaxFiles

    args = raw_input("Syntax:")
    args = args.split()

    if (len(args) > 0 ):

        if (args[0] == "dir" and len(args) == 2):
            if  os.path.isdir(args[1]):
                workingDirectory = args[1]
                getFiles(workingDirectory)
            else:
                print "Directory does not exist."

        elif (args[0] == "watch"):
            print "Watching for changes. Press (CTRL-C) to exit."
            while True:
                time.sleep(1)
                for file in syntaxFiles:
                    if (file["time"] != os.stat(file["path"]).st_mtime): # If the times are different, that means the folder has been updated
                        file["time"] = os.stat(file["path"]).st_mtime
                        execute(file["path"])
    getInput() #Get the users input again, incase the user wants to do somthing else.


try:
    getInput()
except KeyboardInterrupt:
    print "\n Exiting Syntax"
