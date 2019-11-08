import os
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import dh

P = 99494096650139337106186933977618513974146274831566768179581759037259788798151499814653951492724365471316253651463342255785311748602922458795201382445323499931625451272600173180136123245441204133515800495917242011863558721723303661523372572477211620144038809673692512025566673746993593384600667047373692203583
G = 44157404837960328768872680677686802650999163226766694797650810379076416463147265401084491113667624054557335394761604876882446924929840681990106974314935015501571333024773172440352475358750668213444607353872754650805031912866692119819377041901642732455911509867728218394542745330014071040326856846990119719675

conn_port = 8888
max_msg_size = 9999

pn = dh.DHParameterNumbers(P, G)
parameters = pn.parameters(default_backend())
# peer_public_numbers = dh.DHPublicNumbers(genKey(P), pn)

def key2bytes(key):
    return key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def bytes2key(bts):
    return serialization.load_pem_public_key(
        bts,
        backend=default_backend()
    )

def genSharedSecret(skey,pkey):
    return skey.exchange(pkey)

def genSKey():
    # k=random.randint(1,p)
    # print(type(k))

    private_key = parameters.generate_private_key()
    # peer_public_key = private_key.public_key()

    return private_key #peer_public_key

def genPKey(skey):
    return skey.public_key()


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

backend = default_backend()

#Key utilizada pelo algoritmo
# key = int_to_bytes(genKey(P))
key = os.urandom(32)

#Vetor de inicialização
iv = os.urandom(16)

### CBC -> cipher block chain mode -> onde é gerado a sequencia inicial IV
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)




def cipher2(k):
    return Cipher(algorithms.AES(k), modes.CBC(iv), backend=backend)

def encrypt2(m,k):
    encryptor = cipher2(k).encryptor()
    ct = encryptor.update(pad(m).encode()) + encryptor.finalize()
    return ct 

def decrypt2(ct,k):
    decryptor = cipher2(k).decryptor()
    pt_padded=decryptor.update(ct) + decryptor.finalize()
    pt=pt_padded.decode('utf-8') #bytes to str

    #unpad
    l=pt.count('{')
    return pt[:len(pt)-l]


#Pad: Adiciona uma sequencia de { no fim da string para fazer pacotes de tamanho 16, e assim de tamanho divisivel
def pad(s):
    return s + ((16-len(s)%16)* '{')


def encrypt(m):
    encryptor = cipher.encryptor()
    ct = encryptor.update(pad(m).encode()) + encryptor.finalize()
    return ct 

def decrypt(ct):
    decryptor = cipher.decryptor()
    pt_padded=decryptor.update(ct) + decryptor.finalize()
    pt=pt_padded.decode('utf-8') #bytes to str

    #unpad
    l=pt.count('{')
    return pt[:len(pt)-l]



# def main():
#     message=str(input("Mensagem para encriptar:\n"))
#     ct=encrypt(message)
#     print(ct)
#     pt=decrypt(ct)
#     print(pt)


# if __name__ == "__main__":
#     main()    