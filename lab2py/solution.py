import loader
from args_parser import args

if __name__ == '__main__':

    goal_clause, clauses = loader.load_clauses(args.path_clauses)

    if args.action == 'resolution':
        print(clauses)
        print(goal_clause)
    else:
        # load commands
        print(0)
