from PROTOCOLS import Ethernet, Tcp
from PROTOCOLS.analyzer import analyze
from utils import *
import os

if __name__ == "__main__":
    data = reader("Trames/tcp1.txt")
    # print(*data, sep="\n")
    outputfile = "output.txt"
    if os.path.exists(outputfile):
        os.remove(outputfile)

    for d in data:
            result = analyze(d, Ethernet, dict())
            write_result(result)
            write_result(result, outputfile)

