#An object can be a class, id, element, etc, or the contents such as background-color, width, etc.


import Variable
import Error


outputFile = open("../example.css","w")




# processObject parses .syn file contents into a list. The parameter string is one of the lines from the .syn file

def init(): #This is caled to reinitalise the variables before each process.
    global prevString
    global prevName
    global elements
    global element

    prevString = ""
    currentString = ""
    elements = []
    prevName = []
    element = None

def process(string):
    global prevString
    global prevName
    global elements
    global element

    currentIndentation = indentation(string)
    prevIndentation = indentation(prevString)

    if (currentIndentation > prevIndentation): # Previous one must be a parent.
        if (element == None):
            element = -1

        else:
            prevName.append(prevString)
            if (len(elements) > 0):
                elements[element]["children"] = listRemove(1,elements[element]["children"]) # Delete this parent from the children of the previous parent.
            elements.append({"name": " ".join(prevName), "children":[]})
            element = lastIndex(elements)



    elif (currentIndentation < prevIndentation): # This means we are not a child of the previous parent(s).
        # Remove the previous parent(s), and go down a certain amount of elements
        element -= prevIndentation-currentIndentation
        for i in 0,prevIndentation-currentIndentation:
            prevName.pop()


    if (len(elements) > 0): # With the way this system works, we have to add every real line to the children of the previous element.
        elements[element]["children"].append(string)


    #print "---------------------------------"
    #print elements

    prevString  = string

# Exports the elements to a CSS file
def export(cssPath):
    cssFile = open(cssPath,"w")
    for element in elements:
        cssFile.write(element["name"] + "{")

        for child in element["children"]:
            cssFile.write(child + ";")

        cssFile.write("}")
    cssFile.close()



#------ Tidbits ------#z
def combineList(sourceList):
    for sourceIndex, sourceElement in enumerate(sourceList, start=0):
        for copyIndex, copyElement in enumerate(sourceList, start=0):
            if sourceElement["name"] == copyElement["name"]:
                sourceList[sourceIndex]["children"] += sourceList[copyIndex]["children"]
                sourceList.pop(copyIndex)

    return sourceList

def lastIndex(list): # Returns the last index of a given list.
    return len(list)-1

def indentation(string): # Returns the number of intentions in a string
    return len(string) - len(string.lstrip())

def strip(string): # Strips indents and linebreaks from a string.
    return string.lstrip().strip("\n").strip(" ")

def listRemove(amount,list): # Removes (n) amount of items from a list, starting from the end.
    return list[:-amount]
