import random
filename1 = '一.txt'
filename2 = '二.txt'
filename3 = '三.txt'

with open(filename1) as file:
    sentences1 = file.readlines()
with open(filename2) as file:
    sentences2 = file.readlines()
with open(filename3) as file:
    sentences3 = file.readlines()