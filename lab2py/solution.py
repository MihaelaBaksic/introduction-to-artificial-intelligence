import loader
from args_parser import args
from resolution import resolution
from util import print_results
from util import to_string

if __name__ == '__main__':

    goal, sos, premises = loader.load_clauses(args.path_clauses)

    if args.action == 'resolution':
        # print(premises)
        # print(sos)
        result, resolution_d = resolution(premises, sos)
        print_results(resolution_d)

        print('[CONCLUSION]: ' + to_string(goal) + ' is ' + ('true' if result else 'unknown'))
    else:
        # load commands
        print(0)
