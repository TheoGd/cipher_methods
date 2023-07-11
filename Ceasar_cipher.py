#
#Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 
#
#    For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
#    
#        xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
#   
#    This message has an offset of 10. Can you decode it?
    

#Step 1: Decode Vishal's Message
#In the cell below, use your Python skills to decode Vishal's message and print the result.

# setting the string and creating 2 functions that take two parameters, message and the offset. 1 function for encoding and one for decoding.

def ceasar_decode(message, offset)
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  new_string = ""
  for letter in string:
      if letter.isalpha():
          index = list1.index(letter) + int(offset)
          if index >= (len(list1) - 1):
              index -= len(list1)
              new_string += str(list1[index])
          else:
              new_string += str(list1[index])
      else:
          new_string += letter
  return new_string


def caesar_encode(message, offset):
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_string = ""
    for letter in message:
        if letter.isalpha():
            index = list1.index(letter)-int(offset)
            if index >= (len(list1) - 1):
                index -= len(list1)
                new_string += str(list1[index])
            else:
                new_string += str(list1[index])
        else:
            new_string += letter
    return new_string

print(caesar_encode("paok needs to bring in players", 10))
print(caesar_decode("fqea duuti je rhydw yd fbqouhi", 10))




