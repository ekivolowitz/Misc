import rsa

# (pubKey, privKey) = rsa.newkeys(512, poolsize=8)
# print(pubKey)
# print(privKey)
#
# msg = b'ENCRYPTION IS WEIRD'
#
# crypto = rsa.encrypt(msg, pubKey)
# print("msg: " + str(msg))
# print("crypto: " + str(crypto))
# print("Unencrypted crypto: " + str(rsa.decrypt(crypto, priv_key=privKey)))
# signature = rsa.sign(crypto, privKey, hash='SHA-1')
# rsa.verify(crypto, signature, pubKey)


class User(object):
    def __init__(self):
        (self.publicKey, self.privateKey) = rsa.newkeys(2048, poolsize = 8)
        self.incomingMessage = None # will be of form (encrypted message, sender signature, sender public key)
    def sendMsg(self, receiver, message):
        if type(message) == str:
            encryptedMessage = encryptMessage(msg = message.encode('utf-8'), receiverPubKey=receiver.publicKey)
            print(message)
            print(encryptedMessage)
            signedEncryptedMessage = signMessage(self.privateKey, encryptedMessage)
            print(signedEncryptedMessage)
            receiver.incomingMessage = (encryptedMessage, signedEncryptedMessage, self.publicKey)
        else:
            raise Exception("ERROR: accepts string type only.")
    def verifyAndReadIncomingMessage(self):
        '''
        :param msg: (signed and encrypted message, sender public key)
        :return: Verified message
        '''
        if rsa.verify(self.incomingMessage[0], self.incomingMessage[1], self.incomingMessage[2]):
            return rsa.decrypt(self.incomingMessage[0], self.privateKey)

def encryptMessage(msg, receiverPubKey):
    return rsa.encrypt(msg, receiverPubKey)
def signMessage(senderPrivateKey, msg):
    return rsa.sign(msg, senderPrivateKey, hash="SHA-1")



if __name__ == "__main__":
    u1 = User()
    u2 = User()
    #Can send up to 245 characters
    u1.sendMsg(u2,"test message")
    print(u2.verifyAndReadIncomingMessage())
