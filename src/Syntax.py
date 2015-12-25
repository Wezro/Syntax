# Main class for Syntax
import ProcessManager
import Error
syntaxFile = open("../example.syn","r")
syntaxLines = syntaxFile.readlines()

outputFile = open("../example.css","w")



for line in syntaxLines:
    if not line.strip(): #Skip empty lines
        continue
    else:
        ProcessManager.process(line)


Error.showErrors() #Return the errors
