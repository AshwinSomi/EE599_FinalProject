def main2(n, e, d, message):
    aph_dict={' ':'00', 'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07',
               'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14',
                 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21',
                   'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    numerical_message = ""
    for i in message:
        numerical_message += aph_dict[i.lower()]
    print(numerical_message)
    blocks = []
    n_size =0
    for i in str(n): n_size+=1
    if int("26"*int(n_size/2)) < n:
        for i in range(0, len(numerical_message)-(n_size//2)*2, (n_size//2)*2):
            m=''
            for j in range((n_size//2)*2):
                m += numerical_message[i+j]
            blocks.append(int(m))
        rm=''
        for k in range(i+j+1,len(numerical_message)):
            rm += numerical_message[k]
        blocks.append(int(rm))

    else:
        for i in range(0, len(numerical_message)-((n_size//2)-1)*2, ((n_size//2)-1)*2):
            m=''
            for j in range(((n_size//2)-1)*2):
                m += numerical_message[i+j]
            blocks.append(int(m))
        for k in range(i+j+1,len(numerical_message)):
            rm += numerical_message[k]
        blocks.append(int(rm))
        

    print(blocks)
    #encryption
    encrypted = []
    print("encrypting")
    for i in blocks:
        encrypted.append(encrypt_decrypt(e, n, i))
    print(encrypted)
    #decryption
    decrypted = []
    print("decrypting")
    for i in encrypted:
        decrypted.append(encrypt_decrypt(d, n, i))
    print(decrypted)



def encrypt_decrypt(ed, n, m):
    ed = bin(ed).replace("0b", "")
    C=1
    for i in str(ed):
        C= (C*C) % n
        if i == "1":
            C = (C*m) % n
    #print(f"the encrypted message of {m} is {C}")
    return C
       
#main2(2773, 17 ,157, "Its All greek")     
#main2(943, 191, 751, "Its All greek")
#main2(3713, 1231, 991, "Its All greek")  
main2(3713, 1231, 991, "Its All greek")
