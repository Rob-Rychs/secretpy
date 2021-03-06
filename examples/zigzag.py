#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Zigzag

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3

chipher = Zigzag()
print(plaintext)

enc = chipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = chipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"wearediscoveredfleeatonce"

print(plaintext)
enc = chipher.encrypt(plaintext, key)
print(enc)
dec = chipher.decrypt(enc, key)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"defendtheeastwallofthecastle"
key = 4

print(plaintext)
enc = chipher.encrypt(plaintext, key)
print(enc)
dec = chipher.decrypt(enc, key)
print(dec)
