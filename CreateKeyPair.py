import os.path as p
from subprocess import check_output
import sys
def getCheckSum():
    if len(sys.argv) != 2:
        raise Exception("Error: Please submit a filepath as a string.")
    elif isinstance(sys.argv[1], str):
        filePath = sys.argv[1]
        if p.exists(filePath):
            if filePath[-3:] in ["png", "jpg"] or filePath[-4:] == '.jpeg':
                print check_output(['shasum', filePath]).split(" ")[0]
            else:
                raise Exception("Please submit a png, jpg, or jpeg image.")
        else:
            raise Exception("Error: File not found.")
if __name__ == "__main__":
    getCheckSum()
