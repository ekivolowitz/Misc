import rsa
def generateKeyPair():
    '''
    Generates a public and private keypair in that order in a tuple.
    :return: Tuple(rsa.key.PublicKey, rsa.key.PublicKey)
    '''
    return rsa.newkeys(2048, poolsize=8)
if __name__ == "__main__":
    print("running")
    (pubKey, privateKey) = generateKeyPair()
    with open("pubkeyReceiver.pem", 'wb') as f:
        bstring = pubKey.save_pkcs1(format="PEM")
        f.write(bstring)
    with open('privkeyReceiver.pem', 'wb') as f:
        bstring = privateKey.save_pkcs1(format="PEM")
        f.write(bstring)

    (pubKey, privateKey) = generateKeyPair()
    with open("pubkeySender.pem", 'wb') as f:
        bstring = pubKey.save_pkcs1(format="PEM")
        f.write(bstring)
    with open('privkeySender.pem', 'wb') as f:
        bstring = privateKey.save_pkcs1(format="PEM")
        f.write(bstring)
