#This is used for outputting errors to the user.

errors = []

ERROR_FILE = open("../error.html","w")
ERROR_HEADER = open("res/error_header.html","r").read()
LEVELS = ["WARNING","FAIL"]

def processError(level,line,title,message):
    errors.append([level,line,title,message])


def showErrors():
    ERROR_FILE.write(ERROR_HEADER)
    for error in errors:
        ERROR_FILE.write(formatError(error[0],error[1],error[2],error[3]))


def formatError(level,line,title,message):
    return "<div class=" + level + "> <h1>" + title + "</h1> <p>" + message + "<i>" + "On line:" + line + "</i></p></div>"
