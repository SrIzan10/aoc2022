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
opponentInv = {
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

        opponent = int(i[0])
        player = int(i[1])

        if isPart2:
            opponent = int(i[1])
            player = int(i[0])

        winner = rockpaperscissors(opponent, player)
        finalPoints = 0
        match winner:
            case 'player':
                finalPoints = player + 6
            case 'tie':
                finalPoints = player + 3
            case 'opponent':
                finalPoints = player

        results.append({ 'opponent': opponent, 'player': player, 'winner': winner, 'finalPoints': finalPoints })
    
    for r in results:
        sum += r['finalPoints']
    
    return { 'results': results, 'sum': sum }


def part2():
    results = part1()['results']
    loss = { "A": "C", "B": "A", "C": "B" }
    wins = { "A": "B", "B": "C", "C": "A" }
    sum = 0
    simInput = []

    # left hand is the player, right hand is the opponent
    for r in results:
        player = r['player']
        opponent = r['opponent']
        # inverted values for better treatment
        player = playerInv[player]
        opponent = opponentInv[opponent]
        
        if opponent == 'X':
            player = loss[player]
        elif opponent == 'Y':
            player = player
        elif opponent == 'Z':
            player = wins[player]

        simInput.append(f"{player} {opponent}")
    
    calc = part1(simInput, True)
    return calc['sum']

def rockpaperscissors(opponent, player):
    opponent = int(opponent)
    player = int(player)
    if opponent == player:
        return "tie"
    elif opponent == 1 and player == 2:
        return "player"
    elif opponent == 2 and player == 1:
        return "opponent"
    elif opponent == 1 and player == 3:
        return "opponent"
    elif opponent == 3 and player == 1:
        return "player"
    elif opponent == 2 and player == 3:
        return "player"
    elif opponent == 3 and player == 2:
        return "opponent"
    else:
        raise ValueError("Make sure opponent and player have right numbers.")

print('Part1:', part1()['sum'])
print('Part2:', part2())