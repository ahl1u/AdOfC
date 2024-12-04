

def preprocess(name):
    lines = []
    with open(name, 'r') as file:
        
        for line in file:
            curr = []
            for char in line:
                if char.isalpha():
                    curr.append(char)
            lines.append(curr)
    return lines

def calculate1(data):
    count = 0
    rows, cols = len(data), len(data[0])

    ref = 'XMAS'

    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if r + (3*dr) in range(rows) and c+ (3*dc) in range(cols):
                    if (data[r][c] + data[r+dr][c+dc] + data[r+(2*dr)][c+(2*dc)] + data[r+(3*dr)][c+(3*dc)]) == ref:
                        
                        count+=1
    return count

def calculate2(data):
    count = 0
    rows, cols = len(data), len(data[0])

    ref = 'MAS'

    directions = [[1,1],[-1,1],[1,-1],[-1,-1]]

    for r in range(rows):
        for c in range(cols):
            if ((r+directions[0][0] in range(rows)) and (r+directions[1][0] in range(rows)) and \
                (r+directions[2][0] in range(rows)) and (r+directions[3][0] in range(rows)) and \
                (c+directions[0][1] in range(cols)) and (c+directions[1][1] in range(cols)) and \
                (c+directions[2][1] in range(cols) and (c+directions[3][1] in range(cols)))):

                top_left = data[r+directions[3][0]][c+directions[3][1]]
                top_right =  data[r+directions[1][0]][c+directions[1][1]]
                middle = data[r][c]
                bottom_left = data[r+directions[2][0]][c+directions[2][1]]
                bottom_right = data[r+directions[0][0]][c+directions[0][1]]
                
                if top_left + middle + bottom_right == top_right + middle + bottom_left == ref \
                    or bottom_left + middle + top_right == bottom_right + middle + top_left == ref \
                    or top_left + middle + bottom_right == bottom_left + middle + top_right == ref \
                    or bottom_right + middle + top_left == top_right + middle + bottom_left == ref:
                    
                    count+=1
    return count


def main():
    data = preprocess("input.txt")
    print(calculate1(data))
    print(calculate2(data))

if __name__ == "__main__":
    main()