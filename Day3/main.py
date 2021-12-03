def day3part1():
    input = open('Day3/input.txt', 'r').read().split('\n')
    gamma = [0] * int(len(input[0]))
    epsilon = [0] * int(len(input[0]))
    for line in input: 
        line = str(line)
        for i in range(len(line)): 
            if line[i] == '1': 
                gamma[i] += 1
                epsilon[i] -= 1
            else: 
                gamma[i] -= 1 
                epsilon[i] += 1
    for i in range(len(gamma)): 
        if int(gamma[i]) > 0: 
            gamma[i] = '1'
        if int(gamma[i]) < 0: 
            gamma[i] = '0'
    for i in range(len(epsilon)): 
        if int(epsilon[i]) > 0: 
            epsilon[i] = '1'
        if int(epsilon[i]) < 0: 
            epsilon[i] = '0'
    gamma = bin2dec(list2int(gamma))
    epsilon = bin2dec(list2int(epsilon))
    print(gamma*epsilon)

def day3part2(): 
    input = open('Day3/input.txt', 'r').read().split('\n')
    inputgamma = input.copy() 
    inputepsilon = input.copy()

    j = int(0)
    while len(inputgamma) != 1:
        gamma = 0
        for i in range(len(inputgamma)): 
            gamma = int(gamma)
            if inputgamma[i][j] == '1':
                gamma += 1
            if inputgamma[i][j] == '0':
                gamma -= 1  
        if gamma > 0 or gamma == 0: 
            gamma = 1 
        if gamma < 0: 
            gamma = 0
    
        i = 0
        while i < len(inputgamma):
            if int(inputgamma[i][j]) != gamma: 
                inputgamma.pop(i)
                i -= 1
            i += 1
        j += 1
    oxygen = bin2dec(list2int(inputgamma))

    j = int(0)
    while len(inputepsilon) != 1:
        epsilon = 0
        for i in range(len(inputepsilon)): 
            epsilon = int(epsilon)
            if inputepsilon[i][j] == '1':
                epsilon += 1
            if inputepsilon[i][j] == '0':
                epsilon -= 1  
        if epsilon > 0 or epsilon == 0: 
            epsilon = 0 
        if epsilon < 0: 
            epsilon = 1
    
        i = 0
        while i < len(inputepsilon):
            if int(inputepsilon[i][j]) != epsilon: 
                inputepsilon.pop(i)
                i -= 1
            i += 1
        j += 1
    co2 = bin2dec(list2int(inputepsilon))
    print(oxygen*co2)
    
def list2int(list):
    integers = list
    strings = [str(integer) for integer in integers]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return(an_integer)

def bin2dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)   
    
if __name__ == "__main__":
    day3part2()