import random

class NumError(Exception):
    def __init__(self):
        super().__init__()
    def check(num):
        if num==1 or num==2 or num==3:
            return True
        else:
            return False

global num      
num = 0

def input_num():
    while 1:
        global count
        count=input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
        try:
            count=int(count)
        except ValueError:
            print('정수를 입력하세요')
            continue

        try:
            if not NumError.check(count):
                raise NumError
        except:
            print('1, 2, 3 중 하나를 입력하세요')
            continue
        break

def brGame():
    global count
    global num

    player=['computer','player']
    order=0
    flag=False

    while 1:
        if order==0:
            nowplayer=player[0]
            count=random.randint(1,3)
        else:
            nowplayer=player[1]
            input_num()
        
        for i in range(count):
            num+=1
            print(nowplayer,":", num)
            if num==31:
                flag=True
                break

        if flag:
            if order==0:
                winner = player[1]
            else:
                winner = player[0]
            break
        order=not order
    return winner

def main():
    winner=brGame()

    print(winner,'win!')

main()