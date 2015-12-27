#An object can be a class, id, element, etc, or the contents such as background-color, width, etc.


import Variable
import Error

prevString = ""
currentString = ""
var = ""
tok = ""
outputFile = open("../example.css","w")

elements = []
prevName = []

def processObject(string):
    global prevString
    global prevName
    global elements

    currentIndentation = indentation(string)
    prevIndentation = indentation(prevString)
    element = 0

    if (currentIndentation > prevIndentation): # This means the previous one was a parent.
        elements.append({"name": ' '.join(prevName) + prevString,"children":[]})
        element = lastIndex(elements) # Make element "point" to the last index in the list elements.
        elements[element]["children"].append(string) # Add the current string to the current element
        prevName.append(prevString) #Add the name to the list of previous names.

    elif (currentIndentation < prevIndentation): # This means we are going down a parent.
        element -= prevIndentation - currentIndentation
        prevName = listRemove(prevIndentation-currentIndentation,prevName)
        elements[element]["children"].append(string) # Add the current string to the current element

    else:
        elements[element]["children"].append(string) # Add the current string to the current element

    prevString  = string



#------ Tidbits ------#

def lastIndex(list): # Returns the last index of a given list.
    return len(list)-1

def indentation(string): # Returns the number of intentions in a string
    return len(string) - len(string.lstrip())

def strip(string): # Strips indents and linebreaks from a string.
    return string.strip("\t").strip("\n")

def listRemove(amount,list): # Removes (n) amount of items from a list, starting from the end.
    return list[:amount-1]
