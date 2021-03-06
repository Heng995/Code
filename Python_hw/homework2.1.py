import random
import time

while(True):
    t = random.randint(1,10)
    input(str(t) + ' 秒時間測試，準備好就按 Enter 鍵開始')

    start = time.time()
    input('開始計時! 按 Enter 鍵結束計時!')
    end = time.time()

    seconds = end - start
    print('你的秒數:', round(seconds, 2))

    error = abs(t - seconds)
    print('誤差秒數:', round(error, 2))

    acc = round(1 - (error / t), 2)
    print('準確度:', acc)

    try_again = input('要再試一次嗎?(yes/no)')
    if(try_again == 'yes'):
        continue
    else:
        break
