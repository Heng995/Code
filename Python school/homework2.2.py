import math
pet = input('你的寵物是「狗」還是「貓」?')
if(pet == '狗'):
    dog_age = input('狗幾歲了?')
    human_age = 16 * math.log(int(dog_age))
