
def parse(input):
    new_input = []
    temp = ''
    for i in [i for i in input.split(' ') if i]:
        if i.isdigit():
            temp += i
        else:
            new_input.append(int(temp))
            new_input.append(i)
            temp = ''
    if temp != '':
        new_input.append(int(temp))
    return new_input


def calculation(array):
    if len(array) == 0:
        return 0
    if str(array[-1]).isdigit():
        return array[-1]
    elif array[-1] in '+-*/':
        if len(array) >= 2:
            return array[-2]
        else:
            return 0
    if array[-1] == '=':
        if array[1] == '+':
            sum = array[0] + array[2]
            return sum
        elif array[1] == '-':
            sum = array[0] - array[2]
            return sum
        elif array[1] == '*':
            sum = array[0] * array[2]
            return sum
        elif array[1] == '/':
            sum = array[0] / array[2]
            return int(sum)

if __name__ == '__main__':
    with open('input.txt', 'r', encoding='UTF-8') as file:
        input = file.read()
    array = parse(input)
    print(array)
    print(calculation(array))

