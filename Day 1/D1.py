from collections import Counter

def process(name):

    first, second = [], []

    with open(name, 'r') as file:
        for line in file:

            nums = line.strip().split()

            first.append(int(nums[0]))
            second.append(int(nums[1]))
    
    return first, second

def calculate1(first, second):
    first.sort()
    second.sort()

    total = 0

    for num1, num2 in zip(first, second):
        total += abs(num2-num1)
    
    return total

def calculate2(first, second):
    ref = Counter(second)
    total = 0

    for num in first:
        if num in ref:
            total += num * ref[num]
    
    return total

def main():
    first, second = process('input.txt')
    print(calculate1(first, second))
    print(calculate2(first, second))

if __name__ == "__main__":
    main()