import Error
storedVariables = {}

extensions = ["px","%","in","cm","mm"]

def process(string):
    newVar, tok = processVariable(string)
    storedVariables[newVar] = tok


def processVariable(string):
    if len(string) > 0:
        tok = ""
        newVar = ""
        for char in string:
            if not char == " " and not char == ":": #Ignore spaces and ";" symbols, as we don't want to read them.
                tok += char
            if char == ":": #If it is a ":" character, than we are assigning the variable.
                newVar = tok # The name of the new var is going to be equal to the token
                tok = "" #Clear the token that way we can find out what we are trying to make it
        if tok[0] == "@": # If it starts with an "@" character, we are probably assigning a variable to another variable.
            tok = getValue(tok) #Make the token equal to the variable's value.
        else:
            tok = getExtension(tok)
        return [newVar,tok] #We return instead of setting because some other classes such as Objects use this function to calculate variables.
    else:
        return None


def getValue(var):
    if var.endswith("\n"):
        var = var[:-1] #Remove \n if the var has it.
    return storedVariables.get(var,None) #Return the value and the type. Ex it would return [15,"px"]


def getExtension(var):
    if var.endswith("\n"):
        var = var[:-1] #Remove \n if the var has it.

    if var[0].isdigit() == True: #Make sure we are dealing with a length here and not somthing like "left", "right", "releative", etc.
        for extension in extensions:
            if var.endswith(extension) == True:
                return [var[:-len(extension)],extension] #Return a array with the variable without the extension, and also the extension.
    else:
        return {var,None}
