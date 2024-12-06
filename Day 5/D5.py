from collections import defaultdict

ref = defaultdict(list)

def preprocess(name):
    data = []

    with open(name, 'r') as file:
        for line in file:
            if len(line) == 1:
                break
            curr = line.strip().split('|')
            ref[curr[0]].append(curr[1])
        for line in file:
            nums = line.split(',')
            curr = []
            for i,num in enumerate(nums):
                if i == len(nums)-1:
                    curr.append(str(int(num)))
                else:
                    curr.append(num)
            data.append(curr)
    return data
    
def calculate1(data):
    total = 0
    look = []

    for line in data:
        flag = True
        for i,char in enumerate(line):
            for check in ref[char]:
                if check in line[:i]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            total += int(line[len(line)//2])
    return total

def calculate2(data):
    total = 0
    fixup = []

    for line in data:
        flag = True
        for i,char in enumerate(line):
            for check in ref[char]:
                if check in line[:i]:
                    fixup.append(line)
                    flag = False
                    break
            if not flag:
                break
    for line in fixup:
        flag = True
        
        while True:
            flag = True
            for i,char in enumerate(line):
                for check in ref[char]:
                    for j,char in enumerate(line[:i]):
                        if char == check:
                            line[i],line[j] = line[j],line[i]
                            flag = False
                            break
                    if not flag:
                        break
                if not flag:
                    break
            if flag:
                break
        total += int(line[len(line)//2])
    return total

def main():
    data = preprocess("input.txt")
    print(calculate1(data))
    print(calculate2(data))

if __name__ == "__main__":
    main()