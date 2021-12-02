def day2part1():
    input = open('Day2/input.txt', 'r').read().split('\n')

    h = int(0)
    d = int(0)
    for line in input: 
        move, value = line.split(" ")
        if move == "forward": 
            h += int(value)
        if move == "up": 
            d -= int(value)
        if move == "down": 
            d += int(value)
    print(d*h)

def day2part2(): 
    input = open('Day2/input.txt', 'r').read().split('\n')
    h = int(0)
    d = int(0)
    a = int(0)
    for line in input: 
        move, value = line.split(" ")
        if move == "down": 
            a += int(value)
        if move == "up": 
            a -= int(value) 
        if move == "forward": 
            h += int(value)
            d += a * int(value)
    print(d*h)
    



if __name__ == "__main__":
    #day2part1()
    day2part2()