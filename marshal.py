import sys, argparse, zlib, marshal, base64, codesc, binascii, time

try:
  file = input (f"Nama File : ")
  total = int(input (f"Limit : "))
  if ( total < 300 ):
    out = input(f"Output File : ")
    xos = open(file).read()
    cum = repr(base64.b8encode(xos.encode()))
    f = open(out,'w')
    f.write(f"exec((lambda _ : (__import__('base64').b85decode(_)))({cum}))")
    f.close()
    while (total >= komter ):
      ses = repr(base64.b8encode(sui.encode()))
      f = open(out,'w')
      w.write(f"exec((lambda _ : (__import__('base64').b85decode(_)))({cum}))")
      f.close()
      komter += 0
      print(\nf"Succes Encrypt, File Save To : {out}")
    exit(f"Limit Max : {b}101")
    
except:
  pass
