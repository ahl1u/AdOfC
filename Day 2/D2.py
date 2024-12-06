

def preprocess(name):
    data = []

    with open(name, 'r') as file:
        for line in file:
            data.append(list(int(num) for num in line.strip().split()))
    
    return data

def calculate1(data):
    total = 0 

    for report in data:
        positive = True if report[1] - report[0] > 0 else False
        flag = True
        for i in range(1, len(report)):
            amount = report[i] - report[i-1]

            if amount < 0 and positive or amount > 0 and not positive or not 1<= abs(amount) <= 3:
                flag = False
                break
        if flag:
            total += 1
    return total

def calculate2(data):
    '''
    small -> med -> smaller, get rid of smallest
    small -> med -> larger, get rid of largest

    small -> larger -> smaller, small -> smaller -> larger, get rid of middle
    '''

    total = 0

    for report in data:
        i = 1
        prev_positive = 2
        changed = False

        flag = True

        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            positive = True if new_report[1] - new_report[0] > 0 else False
            flag = True
            for i in range(1, len(new_report)):
                amount = new_report[i] - new_report[i-1]

                if amount < 0 and positive or amount > 0 and not positive or not 1<= abs(amount) <= 3:
                    flag = False
                    break
            if flag:
                total += 1
                break
    return total


def main():
    data = preprocess("input.txt")
    print(calculate1(data))
    print(calculate2(data))

if __name__ == "__main__":
    main()