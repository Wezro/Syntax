# Main class for Syntax
import ProcessManager
import Error
import Objects
syntaxFile = open("../example.syn","r")
syntaxLines = syntaxFile.readlines()




for line in syntaxLines:
    if not line.strip(): #Skip empty lines
        continue
    else:
        ProcessManager.process(line)

Objects.outputFile.write("}") # We have to write this to the output file, othrwise the last element in the CSS will be hanging.


Error.showErrors() #Return the errors
