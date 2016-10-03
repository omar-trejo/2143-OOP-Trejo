"""
Name: Omar Trejo
Email: otrejo0221@my.mwsu.edu
Assignment: Program 2 - Easy Cipher
"""
class ShiftCipher(object):
    """"
    @ Name: __init__
    @ Description: Constructor
    @ Params:
	    None
    """
    def __init__(self):
        self.plainText = None
        self.cipherText = None
        self.cleanText = None
        self.shift = 3
    """
    @ Name: __str__
    @ Description: Nice string representation of class to help debug.
    @ Params:
	    None
    """
    def __str__(self):
        return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
    """
    @ Name: promptUserMessage
    @ Description: Prompts user for message from standard in
    @ Params:
	    None
    """
    def promptUserMessage(self):
        temp = input("Message: ")
        self.setMessage(temp)
    """
    @ Name: setMessage
    @ Description: sets plaintext and then cleans and calls encrypt or decrypt depending on if message has already been encrypted.
    @ Params:
	    message {string}: String message
	    encrypted {bool}: False = plaintext True=ciphertext
    """
    def setMessage(self,message,encrypted=False):
        if(not encrypted):
            self.plainText = message
            self.cleanData()
            self.__encrypt()
        else:
            self.cipherText = message
            self.__decrypt()
    """
    @ Name: getCipherText
    @ Description: Returns cipherText
    @ Params:
	    None
    """
    def getCipherText(self):
        return self.cipherText
    """
    @ Name: getPlainText
    @ Description: Returns plainText
    @ Params:
	    None
    """
    def getPlainText(self):
        return self.plainText
    """
    @ Name: setShift
    @ Description: Sets shift to be used for converting plainText to cipherText or vise versa
    @ Params:
	    None
    """
    def setShift(self,shift):
        self.shift = shift
    """
    @ Name: getShift
    @ Description: Gets shift to be used for converting plainText to cipherText or vise versa
    @ Params:
        None
    """
    def getShift(self):
        return self.shift
    """
    @ Name: cleanData
    @ Description: Cleans plainText by removing any non alphanumeric characters. This is done by
    only including the ascii values that are located in the range of alphanumeric characters.
    @ Params:
	    None
    """
    def cleanData(self):
        self.cleanText = ''
        for letter in self.plainText:
            if ord(letter) < 48:
                continue
            if ord(letter) > 57:
                if ord(letter) < 65:
                    continue
                if ord(letter) > 90:
                    if ord(letter) < 97:
                        continue
                if ord(letter) > 122:
                    continue
            if ord(letter) > 96:
                self.cleanText += chr(ord(letter)-32)
            else:
                self.cleanText += letter
    """
    @ Name: __encrypt
    @ Description: Encrypts plainText no ciphertext
    @ Params:
	    None
    """
    def __encrypt(self):
        self.cipherText = ''
        if(not self.cleanText):
            return
        for letter in self.cleanText:
            self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
    """
    @ Name: __decrypt
    @ Description: Decrypts ciphertext no plainText
    @ Params:
	    None
    """
    def __decrypt(self):
        self.cleanText = ''
        for letter in self.cipherText:
            self.cleanText += chr((((ord(letter)-65) - self.shift) % 26)+65)
if __name__=='__main__':

    alice = ShiftCipher()
    alice.promptUserMessage()
    print(alice)


    bob = ShiftCipher()
    bob.setMessage(alice.getCipherText(),True)
    print(bob)