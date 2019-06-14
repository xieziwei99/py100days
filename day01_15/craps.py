'''
Created on 2019年06月08日
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
@author: xieziwei99
'''
import random

money = 1000
while money > 0:
    print('Your total account: ', money)
    needs_go_on = False
    while True:
        debt = int(input('please bet: '))
        if debt > 0 and debt <= money:
            break
    first = random.randint(1, 6) + random.randint(1, 6)     # 1 2 3 4 5 6
    print('The player choose %d' % first)
    if 7 == first or 11 == first:
        print('The player wins')
        money += debt
    elif 2 == first or 3 == first or 12 == first:
        print('The banker wins')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = random.randint(1, 6) + random.randint(1, 6)
        print('The player choose %d' % current)
        if 7 == current:
            print('The banker wins')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('The player wins')
            money += debt
            needs_go_on = False

print('You lose all your money, game is over!!!')