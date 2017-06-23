import rsa
import sys

def verifyAndReadIncomingMessage(message, signatureOfSender, senderPublicKey, privateKey=None):
    '''
    USAGE: python3 VerifyAndReadMessage.py <message as bytestring> signatureOfSender senderPublicKey receiverPrivateKey
    :param msg: (signed and encrypted message, signature, sender public key)
    :return: Verified message
    '''
    if rsa.verify(message, signatureOfSender, senderPublicKey):
        return rsa.decrypt(message, privateKey)
    else:
        raise Exception("ERROR: SIGNATURE OF SENDER DOES NOT MATCH!")


if __name__ == "__main__":
    message = sys.argv[1]
    sigSender = sys.argv[2]
    senderPublic = sys.argv[3]
    receiverPrivate = sys.argv[4]

    with open(message, 'rb') as f:
        message = f.read()
    with open(sigSender, 'rb') as f:
        sigSender = f.read()
        # sigSender = rsa.PrivateKey.load_pkcs1(sigSender)
    with open(senderPublic, 'rb') as f:
        senderPublic = f.read()
        senderPublic = rsa.PublicKey.load_pkcs1(senderPublic)
    with open(receiverPrivate, 'rb') as f:
        receiverPrivate = f.read()
        receiverPrivate = rsa.PrivateKey.load_pkcs1(receiverPrivate)
    print(verifyAndReadIncomingMessage(message, sigSender, senderPublic, receiverPrivate))