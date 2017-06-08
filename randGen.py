#! /usr/bin/python3
# rendGen.py - random whatever generator
import random

SPseasons = {
    '1': 13,
    '2': 18,
    '3': 17,
    '4': 17,
    '5': 14,
    '6': 17,
    '7': 15,
    '8': 14,
    '9': 14,
    '10': 14,
    '11': 14,
    '12': 14,
    '13': 14,
    '14': 14,
    '15': 14,
    '16': 14,
    '17': 10,
    '18': 10,
    '19': 10,
    '20': 10
}
SunnySeasons = {
    '1': 7,
    '2': 10,
    '3': 15,
    '4': 13,
    '5': 12,
    '6': 14,
    '7': 13,
    '8': 10,
    '9': 10,
    '10': 10,
    '11': 10
}

roommates = [
    'CJ',
    'Emily',
    'Jordan',
    'Bryce',
    'Anthony'
]


def rand_main(*args):
    if len(args) < 1:
        message = 'There needs to be a command after random like:\n' \
                  'sp\n' \
                  'sunny\n' \
                  'roommate\n' \
                  'choice or order of any # of names\n' \
                  'any # for a random choice between 0 and that number'
    else:
        if len(args) == 1:
            command = args[0]
        else:
            command = args[0]
            sec_args = list(args[1:])
        if command == 'sp':
            message = SP()
        elif command == 'roommate':
            message = rand_roommate()
        elif command == 'sunny':
            message = sunny()
        elif command.isdigit():
            num = int(command)
            message = str(random.randint(0, int(num)))
        elif command == 'choice':
            message = random.choice(sec_args)
            if message == 'cj':
                message = 'CJ'
            else:
                message = message.capitalize()
        elif command == 'order':
            random.shuffle(sec_args)
            for i in range(0, len(sec_args)):
                if sec_args[i] == 'cj':
                    sec_args[i] = sec_args[i].upper()
                else:
                    sec_args[i] = sec_args[i].capitalize()
            message = '\n'.join(sec_args)
        else:
            message = 'I couldn\'t find the correct command\n here is the list of command:' \
                  'sp\n' \
                  'sunny\n' \
                  'roommate\n' \
                  'any # of names\n' \
                  'any # for a random choice between 0 and that number'
    return message


def SP():
    global SPseasons
    seas = str(random.randint(1, len(SPseasons)))
    ep = str(random.randint(1, SPseasons[seas]))
    answer = 'Season {} episode {}'.format(seas, ep)
    return answer


def sunny():
    global SunnySeasons
    seas = str(random.randint(1, len(SunnySeasons)))
    ep = str(random.randint(1, SunnySeasons[seas]))
    answer = 'Season {} episode {}'.format(seas, ep)
    return answer


def rand_roommate():
    global roommates
    return random.choice(roommates)

# Blank Comment