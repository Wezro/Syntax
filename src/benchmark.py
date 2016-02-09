import ProcessManager
import Objects

def execute(fileName):
    ProcessManager.init()
    with open(fileName,"r") as syntaxLines:
        for line in syntaxLines:
            if not line.strip(): #Skip empty lines
                continue
            else:
                ProcessManager.process(line)

    Objects.export(fileName.replace(".syntax","").replace(".syn","") + ".css")
    syntaxLines.close()


execute("../benchmark/syntax/benchmark.syn")
