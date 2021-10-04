import random

x = random.randint(1, 50)
print(x)

for i in range(5):
    bingo = False
    while True:
        try:
            y = int(input(f'第{i+1}/{5}次，請猜一個數字(1~50):'))
            if x == y:
                print('猜對了!')
                bingo = True
                break
            else:
                print('猜錯了@@~')

            break
        except Exception as e:
            print('請輸入正確數字')

    if bingo:
        break

print(f'正確答案為:{x}')
