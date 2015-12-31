# Main class for Syntax
import ProcessManager
import Error
import Objects
syntaxFile = "../example.syn"
cssPath = "../example.css"


with open(syntaxFile,"r") as syntaxLines:
    for line in syntaxLines:
        if not line.strip(): #Skip empty lines
            continue
        else:
            ProcessManager.process(line)

#Objects.elements = Objects.combineList(Objects.elements) # This makes sure if there are any duplicates elements, they are combined.
Objects.export(cssPath)


Error.showErrors() #Return the errors
