import random

print('猜數字遊戲')
x = random.randint(1, 50)
# print(x)

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
                if x > y:
                    print('猜高一點~')
                else:
                    print('猜低一點~')

            break
        except Exception as e:
            print('請輸入正確數字')

    if bingo:
        break

if not bingo:
    print(f'5次結束，正確答案為:{x}')
