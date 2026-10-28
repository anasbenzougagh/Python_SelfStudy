# to read add these imports:
import json
import csv
import os

# path = 'C:\\Users\Anas Benzougagh\PycharmProjects\Python_Bootcamp\day04\\files\\file.txt'

print('--------------------Read a file-------------------')
path = 'files/file.txt'
text_file = open(path, 'r')
print(text_file.read())             # whole text

# print(text_file.readline())       # first line
# print(text_file.readline(1))      # first char

text_file.close()

print('--------------------Create a file-------------------')
path = 'files/file2.txt'
text_file2 = open(path, 'w')

text_file2.write('This is a new text file \nPython created this file')

text_file2.close()

print('--------------------Delete a file-------------------')
os.remove(path)