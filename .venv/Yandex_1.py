
money = input()
papers = int(money.split()[0])
coins = int(money.split()[1])
vending_machine = input()
bottle_price = int(vending_machine.split()[0])
coins_4_change = int(vending_machine.split()[1])

wallet = papers * 1000000 + coins
payment_paper = bottle_price // 1000000
payment_coins = bottle_price - payment_paper * 1000000

def purchase(payment_paper, payment_coins):
    global papers, coins
    papers -= payment_paper
    coins -= payment_coins
    return papers, coins

count = 0
flag = True

while wallet >= bottle_price and flag == True:
    if coins >= bottle_price:
        papers, coins = purchase(0, bottle_price)
        coins_4_change += bottle_price
        count += 1
        wallet -= bottle_price
        continue
    elif payment_paper == 0 and papers > 1 and coins < bottle_price and coins_4_change >= (1000000 - bottle_price):
        papers, coins = purchase(1, 0)
        change = 1000000 - bottle_price
        coins += change
        coins_4_change -= change
        count += 1
        wallet -= bottle_price
        continue
    elif coins < payment_coins and papers > 1 and coins_4_change >= (1000000 - bottle_price):
        papers, coins = purchase(payment_paper + 1, 0)
        change = (payment_paper + 1) * 1000000 - bottle_price
        coins += change
        coins_4_change -= change
        count += 1
        wallet -= bottle_price
        continue
    elif coins < bottle_price and payment_paper >= 1 and papers >= 1:
        papers, coins = purchase(payment_paper, payment_coins)
        count += 1
        coins_4_change += payment_coins
        wallet -= bottle_price
        continue
    else:
        flag = False
print (count)