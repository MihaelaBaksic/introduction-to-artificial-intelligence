import loader
from args_parser import args

if __name__ == '__main__':

    clauses = loader.load_clauses(args.path_clauses)

    if args.action == 'resolution':
        print(clauses)
    else:
        # load commands
        print(0)
