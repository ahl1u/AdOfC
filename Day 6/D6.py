from copy import deepcopy

start = []

def preprocess(name):
    data = []
    row = 0

    with open(name, 'r') as file:
        for line in file:
            row+=1
            curr = []
            col = 0
            for char in line:
                col+=1
                if char == '.' or char == '^' or char == '#':
                    curr.append(char)
                if char == '^':
                    start = [row, col]
            data.append(curr.copy())
    print(start)
    return data

def calculate1(bob):
    data = deepcopy(bob)
    rows, cols = len(data), len(data[0])
    total = 0

    directions = [[-1,0], [0,1],[1,0],[0,-1]]
    index = 0

    r_i, c_i = 0,0
    flag = True

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '^':
                r_i, c_i = r, c
                break

    while flag:
        dr,dc = directions[index%4][0], directions[index%4][1]
       
        while r_i in range(rows) and c_i in range(cols) and (data[r_i][c_i] == '^' or data[r_i][c_i] == '.' or data[r_i][c_i] == 'X'):
            if data[r_i][c_i] == '.' or data[r_i][c_i] == '^':
                data[r_i][c_i] = 'X'
                total += 1

            r_i, c_i = r_i + dr, c_i + dc
        
        if r_i not in range(rows) or c_i not in range(cols):
            flag = False
        elif data[r_i][c_i] == '#':
            r_i,c_i = r_i - dr, c_i - dc
            index += 1
    
    return total

def calculate2(data):
    rows, cols = len(data), len(data[0])
    total = 0
    maximal = (rows * cols * 4) - 1
    

    directions = [[-1,0], [0,1],[1,0],[0,-1]]
    index = 0

    yup_r, yup_c = 0,0

    print(maximal)
    

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '^':
                yup_r, yup_c = r, c
                break

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '.':
                data[r][c] = '#'
                movements = 0
                r_i, c_i = yup_r, yup_c
                flag = True
                index =0
                while True:
                    if not flag:
                        break

                    dr,dc = directions[index%4][0], directions[index%4][1]
                
                    while r_i in range(rows) and c_i in range(cols) and (data[r_i][c_i] == '^' or data[r_i][c_i] == '.' or data[r_i][c_i] == 'X'):
                        movements +=1
                        r_i, c_i = r_i + dr, c_i + dc
                    
                    if movements > maximal:
                        total += 1
                        break

                    if r_i not in range(rows) or c_i not in range(cols):
                        flag = False
                    elif data[r_i][c_i] == '#': 
                        r_i,c_i = r_i - dr, c_i - dc
                        index += 1
                data[r][c] = '.'

    return total


def main():
    bob = preprocess("input.txt")
    print(calculate1(bob))
    print(calculate2(bob))


if __name__ == "__main__":
    main()