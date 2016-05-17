# ciphers.py - Tyler Pennebaker
# Functions to encrypt strings using basic ciphers

def caesar (plaintext,key):
	ciphertext = ""
	for letter in plaintext:
		ciphertext += chr((ord(letter)-97+key)%26+97)
	return ciphertext

def vigenere (plaintext,keyword):
	ciphertext = ""
	for i in range(len(plaintext)):
		ciphertext += chr((ord(plaintext[i])+(ord(keyword[i%len(keyword)]))-193)%26+97)
	return ciphertext

def caesardecrypt (plaintext,key):
	ciphertext = ""
	for letter in plaintext:
		ciphertext += chr((ord(letter)-97-key)%26+97)
	return ciphertext

def vigeneredecrypt (plaintext,keyword):
	ciphertext = ""
	for i in range(len(plaintext)):
		ciphertext += chr((ord(plaintext[i])-(ord(keyword[i%len(keyword)]))-1)%26+97)
	return ciphertext
