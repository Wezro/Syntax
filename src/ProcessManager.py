#Class used for transfering lines to the write classes. Ex var assignments go to class Var

import Variable


import Objects
def process(string):
    if string[0] == "@":
        Variable.process(string)
    elif string[0] != "" or string[0] != "\n":
        Objects.processObject(string)
