#An object can be a class, id, element, etc, or the contents such as background-color, width, etc.


import Variable
import Error

prevString = ""
currentString = ""
var = ""
tok = ""
outputFile = open("../example.css","w")

parents = []





def processObject(string):
    global prevString
    global parents

    if len(prevString) > 0 and len(string) > 0 : # Make sure there actually is a previous string. We could be starting at the start of a file, and there could be no previous strings.
        prevIndention = indentation(prevString)
        currentIndention = indentation(string)

        if (prevIndention < currentIndention): #If it is less than the current indention, that means we are probably creating a new section.
            if (len(parents) > 0): #If there are parents, then we have to add the ending brackert.
                outputFile.write("}")
            outputFile.write( strip(' '.join(map(str, parents)))  + " " + strip(prevString) + "{") #Outputs the parents if there are any, and the object that is being used. ex(body .class {})
            parents.append(strip(prevString)) #This is now the parent.

        elif (prevIndention == currentIndention): #If the indention is the same, we are setting variables.
            var, tok = Variable.processVariable(prevString)
            if var != None:
                outputFile.write(var + ":" + tok[0] + tok[1] + ";") # Creates something like "var: 50px;"

        elif (prevIndention > currentIndention):
            parents = listRemove(prevIndention-currentIndention,parents)
            var, tok = Variable.processVariable(prevString)
            if var != None:
                outputFile.write(var + ":" + tok[0] + tok[1] + ";}")


    prevString = string

def indentation(string): #Returns the number of intentions in a string
    return len(string) - len(string.lstrip())

def strip(string):
    return string.strip("\t").strip("\n") #Strips indents and linebreaks from a string.

def listRemove(amount,list):
    for index in range(0,amount): #We have to subtract one because Python lists start at 0
        del list[index-1]
    return list
