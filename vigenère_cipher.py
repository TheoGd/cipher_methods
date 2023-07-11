### Great work! While you were working on the brute force cracking of the cipher, Vishal sent over another letter. That guy is a letter machine!
#Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us 
#crypto-enthusiasts have had to get more creative and use more complicated ciphers. 
#This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso 
#(cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. 
#What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. 
#The value of the shift for each letter is determined by a given keyword.
#Consider the message:

#barry is the spy

#If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
           
#        dog
               
#Now we repeat the keyword over and over to generate a keyword phrase that is the same length as the message we want to code. 
#So if we want to code the message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are ready to start coding our message. 
#We shift each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth.

#                 message:    b  a  r  r  y    i  s    t  h  e    s  p  y
                
#           keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
                 
#   resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
      
#So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 24, which is "y". Remember to loop back around when we reach either end of the alphabet! Then continue the trend: we shift "a" by the place value of "o", 14, and get "m", we shift "r" by the place value of "g", 15, and get "l", shift the next "r" by 4 places and get "o", and so forth. Once we complete all the shifts we end up with our coded message:
            
#        ymlok cp fbb ejv
                
#As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
            
#        txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!
                
#    and the keyword to decode my message is 
            
#        friends
                
#    Because that's what we are! Good luck friend!
           
#And there it is. Vishal has given you quite the assignment this time! Try to decode his message. It may be helpful to create a function that takes two parameters &mdash; the coded message and the keyword &mdash; then work towards a solution from there.

# Setting 2 functions to decode and encode the message as requested above.

def vigenere_decode(message, keyword):
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_string = ""
    decoded_msg = ""
    counter = 0
    
    for letter in message:
        if counter == len(keyword):
            counter = 0
        if letter.isalpha():
            new_string += str(keyword[counter])
            counter += 1
        else:
            new_string += letter
    
    
    for i in range(len(message)):
        if message[i].isalpha():
            index = list1.index(new_string[i]) + (list1.index(message[i]) - len(list1))
            decoded_msg += list1[index]
        else:
            decoded_msg += message[i]
    return decoded_msg

def vigenere_encode(message, keyword):
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_string = ""
    encoded_msg = ""
    counter = 0
    
    for letter in message:
        if counter == len(keyword):
            counter = 0
        if letter.isalpha():
            new_string += str(keyword[counter])
            counter += 1
        else:
            new_string += letter
    
    
    for i in range(len(message)):
        if message[i].isalpha():
            index = list1.index(message[i]) - list1.index(new_string[i])
            encoded_msg += list1[index]
        else:
            encoded_msg += message[i]
    return encoded_msg


print(vigenere_decode("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!", "friends"))
print(vigenere_encode("well, it seems i am a master right now vishal!!!!", "friends"))



