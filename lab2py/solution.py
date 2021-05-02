import loader
from args_parser import args
from resolution import resolution
from util import print_results, print_knowledge
from util import to_string
from cooking import cooker

if __name__ == '__main__':

    if args.action == 'resolution':

        goal, sos, premises = loader.load_clauses(args.path_clauses)
        # print(premises)
        # print(sos)
        result, resolution_d = resolution(premises, sos)

        if result:
            print_results(resolution_d)
        else:
            print_knowledge(premises.union(sos))
        print('[CONCLUSION]: ' + to_string(goal) + ' is ' + ('true' if result else 'unknown'))

    elif args.action == 'cooking':
        clauses, commands = loader.load_commands(args.path_clauses, args.path_user_commands)

        cooker(clauses, commands)

    else:
        exit(1)
