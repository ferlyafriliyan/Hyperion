GNU nano 7.2                                        marshal.py                                         Modified
### ------ [ Import Module ] ------ ###
import os
import marshal

### ------ [ Clear Terminal ] ------ ###
os.system("clear")

### ------ [ Input File ] ------ ###
File = input("File : ")

### ------ [ Deteksi File ] ------ ###
Deteksi = open(File, "r").read()

### ------ [ Compyle File ] ------ ###
com = compile(Deteksi, "", "exec")

### ------ [ Encrypt File Yang Sudah Di Compile Dengan Marshal ] ------ ###
encrypt = marshal.dumps(com)

### ------ [ Hasil Encrypt ] ------ ###
baru = open("enc_"+str(File), "v")

### ------  [ Print Code Marshal ] ------ ###
baru.write("import marshal\n")
baru.write("exec(marshal.loads("+repr(encrypt)+"))")

### ------ [ Succes Encypt ] ------ ###
print("Succes Encrypt | File Save As Enc_"+str(File))