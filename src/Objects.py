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

element = None


# processObject parses .syn file contents into a list. The parameter string is one of the lines from the .syn file
def process(string):
    global prevString
    global prevName
    global elements
    global element
    currentIndentation = indentation(string)
    prevIndentation = indentation(prevString)


    if (currentIndentation > prevIndentation): # Previous one must be a parent.


        if (element == None): # Make sure the parent isn't fake.
            element = 0

        elif (element == 0): # If this is the first one, there won't be any elements to delete.
            prevName.append(prevString)
            elements.append({"name": " ".join(prevName), "children":[]})
            element = lastIndex(elements)

        elif (element != 0):
            prevName.append(prevString)
            elements[element]["children"] = listRemove(1,elements[element]["children"]) # Delete this parent from the children of the previous parent.
            elements.append({"name": " ".join(prevName), "children":[]})
            element = lastIndex(elements)


    elif (currentIndentation < prevIndentation): # This means we are not a child of the previous parent(s).
        # Remove the previous parent(s), and go down a certain amount of elements
        element -= prevIndentation-currentIndentation
        for i in 0,prevIndentation-currentIndentation:
            prevName.pop()

    if (len(elements) > 0):
        elements[element]["children"].append(string)


    print "---------------------------------"
    print elements

    prevString  = string



#------ Tidbits ------#

def lastIndex(list): # Returns the last index of a given list.
    return len(list)-1

def indentation(string): # Returns the number of intentions in a string
    return len(string) - len(string.lstrip())

def strip(string): # Strips indents and linebreaks from a string.
    return string.lstrip().strip("\n").strip(" ")

def listRemove(amount,list): # Removes (n) amount of items from a list, starting from the end.
    return list[:-amount]
