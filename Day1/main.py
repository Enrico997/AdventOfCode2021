def day1part1(): 
    input = open('input.txt', 'r').read().split('\n')
    input = [int(x) for x in input]
    count = 0
    for i in range (len(input)-1): 
        a = input[i-1] 
        b = input[i]
        if b > a: 
            count += 1
    print(count)

def day1part2(): 
    input = open('input.txt', 'r').read().split('\n')
    input = [int(x) for x in input]
    count = 0 

    for i in range(len(input)-3): 
        a = input[i] + input[i+1] + input[i+2]
        b = input[i+1] + input[i+2] + input[i+3]
        if b > a: 
            count += 1
    print(count)

if __name__ == "__main__":
    day1part1()
    day1part2()

