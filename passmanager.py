
import hashlib 
username=[]
password=[]
stop= False

while stop==False:
    #username
    username_baru=input("masukkan username: ")
    hashed_username = hashlib.md5(username_baru.encode('utf-8')).hexdigest()
    hashed_username2 = hashlib.sha256(hashed_username.encode('utf-8')).hexdigest()
    username.append(hashed_username2)
    #password
    password_baru=input("masukkan password: ")
    hashed_password = hashlib.sha256(password_baru.encode('utf-8')).hexdigest()
    hashed_password2 = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()
    password.append(hashed_password)
    print(username,password)