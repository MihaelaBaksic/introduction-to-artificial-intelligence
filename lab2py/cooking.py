from resolution import resolution
from loader import negate_goal
from util import print_results, to_string, print_knowledge


def cooker(clauses: set, commands: list):
    print('Constructed with knowledge:')
    print_knowledge(clauses)

    for command in commands:
        print("User's command: {} {}".format(to_string(command[0]), command[1]))
        if command[1] == '+':
            clauses.add(command[0])
            print('Added {}\n'.format(to_string(command[0])))
        elif command[1] == '-':
            clauses.remove(command[0])
            print('Removed {}\n'.format(to_string(command[0])))
        elif command[1] == '?':
            result, resolution_d = resolution(clauses.copy(), negate_goal(command[0]))

            if result:
                print_results(resolution_d)
            print('[CONCLUSION]: ' + to_string(command[0]) + ' is ' + ('true' if result else 'unknown'))
            print('')



