dict1 = {'python':'language','php':'language1'}
word = input("enter a word")
if word in dict1:
    print("The meaning of this word is",dict1[word])
else:
    word_insert = input("u want to insert the word")
    if word_insert == 'y':
        word_meaning = input("write meaning of the word")
        dict1.update({word:word_meaning})
        print(dict1)
        print("the meaning of this word is",dict1[word])