def preprocess(name):
    data = []

    with open(name, 'r') as file:
        for line in file:
            data.append(line)
        
    return data

def calculate1(data):
    total = 0
    ref = 'mul('
    flag = True

    for line in data:
        i = 3
        while i < len(line): 
            if line[i-3:i+1] == ref:
                i+=1
                start = i
                while i < len(line) and (line[i].isnumeric() or line[i] == ','):
                    i+=1
                if line[i] == ')':
                    parts = line[start:i].split(',')
                    if len(parts) == 2 and parts[0].isnumeric() and parts[1].isnumeric():
                        total += int(parts[0]) * int(parts[1])
            i+=1
    return total

def calculate2(data):
    total = 0
    ref = 'mul('
    ref1 = "don't()"
    ref2 = "do()"
    flag = True

    for line in data:
        i = 0
        while i < len(line):
            if i > 3 and line[i-3:i+1] == ref and flag:
                i+=1
                start = i
                while i < len(line) and (line[i].isnumeric() or line[i] == ','):
                    i+=1
                if line[i] == ')':
                    parts = line[start:i].split(',')
                    if len(parts) == 2 and parts[0].isnumeric() and parts[1].isnumeric():
                        total += int(parts[0]) * int(parts[1])
            elif i > 6 and line[i-6:i+1] == ref1:
                flag = False
            elif i > 3 and line[i-3:i+1] == ref2:
                flag = True
            i+=1
    return total

def main():
    data = preprocess("input.txt")
    print(calculate1(data))
    print(calculate2(data))

if __name__ == "__main__":
    main()