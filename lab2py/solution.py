import loader
from args_parser import args
from resolution import resolution

if __name__ == '__main__':

    sos, premises = loader.load_clauses(args.path_clauses)

    if args.action == 'resolution':
        print(premises)
        print(sos)
        print(resolution(premises, sos))
    else:
        # load commands
        print(0)
