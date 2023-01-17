from pyDes
import *
ac = "1478000129000000234800005E6BC66300000000B4DE98F14555450EE2B87CF33A74D064E155564A27A094D40545779FA166F7CB9FF4F85EAE70CF988FBF09073D67EDAADB5BB60F50148A8E48A10DE35942C959B9C9A2463FCC63C7B9C9A2463FCC63C7B9C9A2463FCC63C7B9C9A2463FCC63C7B9C9A2463FCC63C7B9C9A2463FCC63C777E1697DC051EB52"
ac = bytes().fromhex(ac)
key1 = ac[4: 20] + b '\x00\x00\x00\x00\x00\x00\x00\x00'
print("key1  hex: %r" % key1.hex())
key2 = ac[20: ]
print("key2  hex: %r" % key2.hex())
key3 = triple_des(key1, ECB, pad = None, padmode = PAD_PKCS5)
key4 = key3.decrypt(key2)
print("key4  bytes:  %r" % key4)
key5 = key4[48: 72]
print("key5 len: %r" % len(key5))
print("key5  hex: %r" % key5)
str = "test"
strbytes = str.encode("UTF-8")
strlen = bytes([len(strbytes)])
randbytes = b '\x00\x00\x00\x00\x00\x00\x00\x00'
#8 bytes
timebytes = b '\x00\x00\x00\x99\x00\x00'
regc = key5 + b "\x0e" + timebytes + strlen + b '\x00' + strbytes print("reginner  len: %r" % len(regc))
print("reginner  hex: %r" % regc.hex())
print("reginner  bytes: %r" % regc) key8 = randbytes + key4[64: 72]
print("key8  len: %r" % len(key8))
key6 = triple_des(key8 + randbytes, ECB, pad = None, padmode = PAD_PKCS5)
key7 = key6.encrypt(regc)
regclen = bytes([len(key7)])
reg = regclen + b '\x00\x01' + key8 + key7
print("reg  hex: %r" % reg.hex())
print("reg  len: %r" % len(reg.hex()))
print("reg  bytes: %r" % reg) ~
