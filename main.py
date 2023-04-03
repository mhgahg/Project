m = 10
n = 8

player = '1','2'
treasures = 'c'
floor = '#'
exit = 'в'
aisle = " "

field= [["." for i in range(m)] for j in range(n)]


def field_init(field):
    field [1][2] = '#'


def field_show (field):
    height = len(field)
    width = len(field[0])

    print('=' * width)

    for y in range(height):
        line = ""
        for x in range(width):
            line += field[y][x]

        print(line)


def interpret_cmd(cmd):
    ...

field_init(field)
field_show(field)

players = {
    '1': {
        'coordinates': [0, 0],
        'sleeping': False,
        'holding_treasure': False
    },
    '2': {
        'coordinates': [1, 1],
        'sleeping': False,
        'holding_treasure': False
    }
}

current_turn = 1

while True:
    player = players[str(current_turn)]

    # 0 проверка на сон

    # 1
    # move [up/down/left/right] --- подвинуться на одну клетку
    # shoot [up/down/left/right] --- выстрелить
    cmd = input()

    # 2
    interpret_cmd(cmd)

    # 3
    field_show(field)

    # 4
    current_turn %= 2
    current_turn += 1


#player

coordinaties = (0, 0)
holding_treasures:bool
#player_move
#player_shoot


# def move_derection (pleyer_move):
#     if player




