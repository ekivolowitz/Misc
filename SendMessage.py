import rsa
import sys

def sendMessage(receiverPublicKey, message):
    if type(message) == str:
        return encryptMessage(msg = message.encode('utf-8'), receiverPubKey=receiverPublicKey)

def encryptMessage(msg="", receiverPubKey=None):
    return rsa.encrypt(msg, receiverPubKey)

def signMessage(message=None, senderPrivateKey=None):
    return rsa.sign(message, senderPrivateKey, hash="SHA-1")


if __name__ == "__main__":
    '''
    usage: python3 SendMessage.py <receiver_public_key> <string of message> <private key>
    @param 1 receiver public key filepath
    @param 2 message payload (what  you want to send encrypted)
    @param 3 private key of sender
    '''

    receiverPubKey = sys.argv[1]
    message = sys.argv[2]
    senderPrivateKey = sys.argv[3]
    try:
        with open(sys.argv[1], 'rb') as f:
            bstring = f.read()
            receiver = rsa.PublicKey.load_pkcs1(bstring)
    except:
        raise Exception("ERROR: Could not load public key.")
    receiverPubKey = receiver

    try:
        with open(sys.argv[3], 'rb') as f:
            bstring = f.read()
            sender = rsa.PrivateKey.load_pkcs1(bstring)
    except:
        raise Exception("ERROR: Could not load private key")
    senderPrivateKey = sender

    # receiverPubKey = rsa.PublicKey.load_pkcs1(sys.argv[1], format="PEM")
    # privateKey = rsa.PublicKey.load_pkcs1(sys.argv[3], format="PEM")

    encryptedMessage = sendMessage(receiverPublicKey = receiverPubKey, message = message)
    signedMessage = signMessage(message = encryptedMessage, senderPrivateKey = senderPrivateKey)
    with open("encrypted", 'wb') as f:
        f.write(encryptedMessage)

    with open("signed", 'wb') as f:
        f.write(signedMessage)
