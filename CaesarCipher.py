alphabet = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(plaintext, k):
    result = ''
    plaintext = plaintext.lower()
    k = int(k)
    for i in range(len(plaintext)):
        olet = plaintext[i]
        if olet != ' ':
            oindex = alphabet.index(olet)
            eindex = oindex-k
            if eindex<0:
                eindex = 25-k+oindex+1
            elet = alphabet[eindex]
            result = result+elet
        else:
            result = result + ' '
    return result

def decrypt(ciphertext, k):
    res = ''
    k = int(k)
    for i in range(len(ciphertext)):
        enlett = ciphertext[i]
        if enlett != ' ':
            enindex = alphabet.index(enlett)
            orindex = (enindex + k) % 26
            orlett = alphabet[orindex]
            res = res + orlett
        else:
            res = res + ' '
    return res
string = input('Give me a string to encrypt: ')
key = input('Give me a key: ')
cr = encrypt(string, key)
en = decrypt(cr, key)
print (cr , en)
