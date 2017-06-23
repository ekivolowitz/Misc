#Dependency: pip install pyqrcode
import pyqrcode as q
import sys

def makeQRCode(payload):
    img = q.create(payload)
    img.svg('qrcode.svg', scale=4)

if __name__ == "__main__":
    value = sys.stdin.read()[:-1]
    if type(value) != str:
        raise Exception("Error: USAGE python qrcodegen <string>")
    makeQRCode(value)
