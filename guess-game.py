import random

x = random.randint(1, 50)
print(x)

while True:
    try:
        y = int(input('請猜一個數字(1~50):'))
        if x == y:
            print('猜對了!')
        else:
            print('猜錯了@@~')

        break
    except Exception as e:
        print('請輸入正確數字')
