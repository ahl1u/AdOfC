from collections import defaultdict


def preprocess(name):

    ref = defaultdict(list)

    with open(name, 'r') as file:
        for line in file:
            nums = line.strip().split()

            for num in nums[1:]:
                ref[int(nums[0][:-1])].append(int(num))

    return ref

def calculate1(data):
    total = [0] * len(data)

    for j,target in enumerate(data):
        nums = data[target]
        i = 0
        sumbob = 0

        def backtrack(i):
            nonlocal sumbob
            if i >= len(nums):
                if sumbob == target:
                    total[j] = target
                return
            sumbob += nums[i]
            backtrack(i+1)
            sumbob -= nums[i]

            sumbob *= nums[i]
            backtrack(i+1)
            sumbob /= nums[i]
        
        backtrack(0)
        
    return sum(total)

def calculate2(data):
    total = [0] * len(data)

    for j,target in enumerate(data):
        nums = data[target]
        i = 0
        sumbob = 0

        def backtrack(i):
            nonlocal sumbob
            if i >= len(nums):
                
                if sumbob == target:
                    total[j] = target
                return
            sumbob += nums[i]
            backtrack(i+1)
            sumbob -= nums[i]
            if sumbob != 0:

                curr = sumbob
                sumbob = int(str(int(sumbob)) + str(nums[i]))
                backtrack(i+1)
                sumbob = curr

            sumbob *= nums[i]
            backtrack(i+1)
            sumbob /= nums[i]
        
        backtrack(0)
    return sum(total)     


    

def main():
    data = preprocess("input.txt")
    print(calculate1(data))
    print(calculate2(data))


if __name__ == "__main__":
    main()