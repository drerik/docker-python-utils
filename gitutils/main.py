import os
import sys
import gitcheck


def main():
    """
    Commandline tool for gitcheck.check_repos
    Syntax: main.py <repo dir 1>, <repo dir 2> ... <repo dir N>
    """
    print("#")
    print("#   [\u2713] = Committed [\u2717] = Dirty  [?] = Not a git repository")
    print("#")
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            print("# Checking {}".format(path))
            gitcheck.check_repos(path)
    else:
        print("# Checking {}".format(os.getcwd()))
        gitcheck.check_repos(os.getcwd())


if __name__ == '__main__':
    main()
