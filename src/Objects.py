#An object can be a class, id, element, etc, or the contents such as background-color, width, etc.


import Variable
import Error


# processObject parses .syn file contents into a list. The parameter string is one of the lines from the .syn file

global prevString
global prevName
global elements
global element

prevString = ""
currentString = ""
elements = []
prevName = []
element = -1



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
    element = -1


#Process the given line of the file.
def process(string):
    global prevString
    global prevName
    global elements
    global element

    currentIndentation = indentation(string)
    prevIndentation = indentation(prevString)

    if (currentIndentation > prevIndentation): # Previous line must be a parent.
        if (element == None): #Ignore the first element, as it is invalid.
            element = -1

        else:
            prevName.append(prevString) # Register the previous string as a new parent element.
            if (len(elements) > 0):
                elements[element]["children"] = listRemove(1,elements[element]["children"]) # Delete this parent from the children of the previous parent.
            elements.append({"name": " ".join(prevName), "children":[]}) # Put the prev string (the parent) in the list of elements.
            element = lastIndex(elements)



    elif (currentIndentation < prevIndentation): # This means we are not a child of the previous parent(s), and are going down a single or multiple parent.
        # Remove the previous parent(s), and go down a certain amount of elements
        element -= prevIndentation-currentIndentation
        for i in 0,prevIndentation-currentIndentation: # Delete however many elements we went back (counted via indentations)
            if (len(prevName) != 0):
                prevName.pop()


    if (len(elements) > 0): # With the way this parser works, we have to add every line to the children of the previous element.
        elements[element]["children"].append(string)

    prevString  = string # At the end of each cycle, this sets the previous string

# Exports the elements to a CSS file
def export(cssPath):
    global elements
    cssFile = open(cssPath,"w")
    elements = compressList(elements)
    for element in elements: # Go through each element, which is the parents.
        cssFile.write(element["name"] + "{") # Write the parent, followed by a { bracket

        for child in element["children"]: # Go through each child in the elements children.
            var, tok = Variable.processVariable(child)
            tok = list(tok)
            child = (var + ":" + tok[0])
            if tok[1] != None: # A lot of variables don't have an extension, so lets see if it does.
                child += tok[1]
            cssFile.write(child + ";") # Write the children (variables)

        cssFile.write("}") # Close the parent.
    cssFile.close()



#------ Tidbits ------#z
def combineList(sourceList):
    for sourceIndex, sourceElement in enumerate(sourceList, start=0): # Start looping through the first list
        for copyIndex, copyElement in enumerate(sourceList, start=0): # Star looping through the same list, this allows us to compare each element in the list to each other.
            if sourceElement["name"] == copyElement["name"]: # If either of the two have the same name, that means we should delete the copy, and take the children from the copy into the original.
                sourceList[sourceIndex]["children"] += sourceList[copyIndex]["children"]
                sourceList.pop(copyIndex)

    return sourceList

def compressList(sourceList):
    for parentIndex, parent in enumerate(sourceList):
        sourceList[parentIndex]["name"] = strip(parent["name"])
        for childIndex, child in enumerate(parent["children"]):
            sourceList[parentIndex]["children"][childIndex] = strip(child)
    return sourceList

def lastIndex(list): # Returns the last index of a given list.
    return len(list)-1

def indentation(string): # Returns the number of intentions in a string
    return len(string) - len(string.lstrip())

def strip(string): # Strips indents and linebreaks from a string.
    return string.lstrip().strip("\n").strip(" ").strip("\t")

def listRemove(amount,list): # Removes (n) amount of items from a list, starting from the end.
    return list[:-amount]
