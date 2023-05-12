# # '''Knowledge Pillars Python Coding Specialist Script'''
# # # Use this document to try out python code from the notes
# # # You will add notes linking this script to the notes.
# # # Comment out Examples as you go so old examples do not break new examples.
# # 
# # # I-E: Insert inline and multi-line comments
# # 
# # # use a "#" to comment.
# # 
# # # #----Inline comment----
# # # hats = ['tophat', 'Cowboy', 'baseball'] #this is a list of hats. Not all hats, but some hats
# # # 
# # # #----Multiline Comment ----
# # # # This next section is an example of comment text that describes
# # # #	What will happen in the code below. If you want multiple
# # # #	you have to use a 'B' at the start of each line.
# # 
# # II-A-I Variables Define, use and recognize various types of variables
# #
# # # Declare and initialize a variable usuing the '=' operator
# # # can cast the data type manually or by typing the data
# 
# x = 3
# or
# x = int(3)
# 
# print(x)
# print(type(x))
# 
# x='3'
# or
# x= str(3)
# 
# 
# print(x)
# print(type(x))
# 
# # -----Variable Name Rules
# 
# # 8post = 5 #This is not ok because Rule 1 and 2
# 
# #Spanish characters are not ok
# 
# #food-Man = "good food" ERROR -'s are not allowed
# hat = 1
# Hat = 2
#
# print(hat) rule #4

# ----Assigning more than one variable at a time ----
#
# Many values to the same number of variables using ','
# to seperate be sure to have the same number

# x , y , z = "Al" , "Weird" , "accordian"
# print(f"{y} {x} is a musician that plays the {z}")
# 
# #unpacking from a colection to many seperate variables
# #      be sure to have the same number
# 
# Jazz = ['Gillespi', 'Dizzy', 'trumpet']
# x, y, z = Jazz
# print(f"{y} {x} is a musician that plays the {z}")


# ---- Strings ----
# 
# x = 'Hat'
# print(type(x))
# 
# y = "Hat"
# print(type(y))
# 
# z = '''hat'''
# 
# x = """Barney is a dinosaur from our imagination
# And when he's tall
# He's what we call a dinosaur sensation
# Barney's friends are big and small
# They come from lots of places
# After school they meet to play
# And sing with happy faces
# Barney shows us lots of things
# Like how to play pretend
# ABC's, and 123's
# And how to be a friend
# Barney comes to play with us
# Whenever we may need him
# Barney can be your friend too
# If you just make-believe him!"""
# 
# print(x)

# ---- string slicing ----
#
# Use [ start: end]
# test = "0123456789"
# 
# x = "The quick brown fox jumps over the lazy dog."
# print(test[2:7])
# print(x[4:9]) # note that the end index is not included
# print(test[:5]) # Start is left blank = statst at index 0
# 
# print(test[4:]) # End is left blank = ends at last value
# print(x[:9])
# 
# print(test[-3:-1]) #negative indexing
# print(x[-8:])
# 


# ----operators----

#Arithmatic or math operators
# x = 15/4
# y = 15%4
# z = 15//4
#print(x,y,z)
#
# a = 4**3
# print(a)
#
# String Operators
#x = 'bannana'
#print('ana' in x)
# print('potassium' in x')

# Bitwise operators - they are a bit confusing...
# x = 0b00100011
# y = 0b01100110
# z = x & y
# print(bin(z))
# a = 0
# b = ~a
# print(bin(a))
# print(bin(b))

# a = 0b10001111
# b = a>>a
# c = a<<a
# print(bin(b))
# print(bin(c))

# ---- order of operations ----

# a = 3**2-2/7*3<=12**2**1+2%2&42>4+2/4-3
# print(a)

# x = 1
# while x < 10:
#     print(x)
#     x += 1
# print('and.....')
# print(10)

magicNumber = 4
x = 1
while x <= 10:
    if x == magicNumber:
        continue
    print(x)
    x += 1
y = 1
#while y:
