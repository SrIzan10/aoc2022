input = open('input.txt', 'r').read().split('\n')

# play
p = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}
playerInv = {
    1: 'A',
    2: 'B',
    3: 'C'
}
oponentInv = {
    1: 'X',
    2: 'Y',
    3: 'Z'
}

def part1(input=input,isPart2=False):
    results = []
    sum = 0

    for i in input:
        for pointsKey in p:
            i = i.replace(pointsKey, str(p[pointsKey]))
        i = i.split()

        oponent = int(i[0])
        player = int(i[1])

        if isPart2:
            oponent = int(i[1])
            player = int(i[0])

        winner = rockpaperscissors(oponent, player)
        finalPoints = 0
        match winner:
            case 'player':
                finalPoints = player + 6
            case 'tie':
                finalPoints = player + 3
            case 'oponent':
                finalPoints = player

        results.append({ 'oponent': oponent, 'player': player, 'winner': winner, 'finalPoints': finalPoints })
    
    for r in results:
        sum += r['finalPoints']
    
    return { 'results': results, 'sum': sum }


def part2():
    results = part1()['results']
    loss = { "A": "C", "B": "A", "C": "B" }
    wins = { "A": "B", "B": "C", "C": "A" }
    sum = 0
    simInput = []

    # left hand is the player, right hand is the oponent
    for r in results:
        player = r['player']
        oponent = r['oponent']
        # inverted values for better treatment
        player = playerInv[player]
        oponent = oponentInv[oponent]
        
        if oponent == 'X':
            player = loss[player]
        elif oponent == 'Y':
            player = player
        elif oponent == 'Z':
            player = wins[player]

        simInput.append(f"{player} {oponent}")
    
    calc = part1(simInput, True)
    return calc['sum']

def rockpaperscissors(oponent, player):
    oponent = int(oponent)
    player = int(player)
    if oponent == player:
        return "tie"
    elif oponent == 1 and player == 2:
        return "player"
    elif oponent == 2 and player == 1:
        return "oponent"
    elif oponent == 1 and player == 3:
        return "oponent"
    elif oponent == 3 and player == 1:
        return "player"
    elif oponent == 2 and player == 3:
        return "player"
    elif oponent == 3 and player == 2:
        return "oponent"
    else:
        raise ValueError("Make sure oponent and player have right numbers.")

print('Part1:', part1()['sum'])
print('Part2:', part2())