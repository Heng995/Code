import random

file1 = '一.txt'
file2 = '二.txt'
file3 = '三.txt'

with open(file1) as file:
    sentences1 = file.readlines()
with open(file2) as file:
    sentences2 = file.readlines()
with open(file3) as file:
    sentences3 = file.readlines()

sentences1 = [sentences.strip() for sentences in sentences1]
sentences2 = [sentences.strip() for sentences in sentences2]
sentences3 = [sentences.strip() for sentences in sentences3]

random.choice(sentences1) + '，' + random.choice(sentences2) + '，' + random.choice(sentences3) + '。'