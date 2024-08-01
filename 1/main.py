input = open('input.txt', 'r').read().split('\n')

def part1():
    calList = []
    sum = 0
    for i in input:
        if i == '':
            calList.append(sum)
            sum = 0
            continue
        sum += int(i)
    
    calList.sort(reverse=True)
    return calList

def part2():
    threeHighest = part1()[:3]
    return sum(threeHighest)

print('Part1:', part1()[0])
print('Part2:', part2())