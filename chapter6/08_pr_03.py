#a spam comment is defined as a text containing following keyword write a program to detect these spam

text = input("Enter a text \n")

if ("make a lot of money" in text):
    spam = True
elif("buy now " in text):
    spam = True
elif("click this " in text):
    spam = True
elif("subscribe this " in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is spam")
else:
    print('this is not spam')
