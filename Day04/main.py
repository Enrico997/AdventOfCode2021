def day4part1(): 
    with open('Day04/input.txt') as f:
        drawn = list([int(x) for x in f.readline().strip('\n').split(',')])
        cards = [] 
        while f.readline(): 
            card = []
            for i in range(5): 
                card.append([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
            cards.append(card)

    checks = []
    for i in range(len(cards)): 
        check = [] 
        for j in range(5): 
            check.append([0] * int(len(cards[0])))
        checks.append(check)

    for item in drawn: 
        for k in range(len(cards)): 
            for i in range(len(cards[0])): 
                for j in range(len(cards[0][0])): 
                    if cards[k][i][j] == item: 
                        checks[k][i][j] = 1
        for z in range(len(cards)): 
            for x in range(len(cards[0])):
                if checks[z][x][0] + checks[z][x][1] + checks[z][x][2] + checks[z][x][3] + checks[z][x][4] == 5:
                    sum = int(0)
                    for q in range(len(checks[0])): 
                        for w in range(len(checks[0][0])):
                            if checks[z][q][w] != 1:
                                sum += cards[z][q][w]
                    print(sum*item)
                    return
              
                        
            
if __name__ == "__main__":
    day4part1()

