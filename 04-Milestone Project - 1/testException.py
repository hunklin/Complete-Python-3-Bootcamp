import sys

def main():
    print(len(sys.argv))
    print(sys.argv[0])
    try:
        f = open('**a.txt', 'r')
        f.write('hunk')
    except FileNotFoundError:
        f = open('a.txt', 'w')
    except OSError:
        print('IOerror')
    finally:
        print("finally here")


if __name__ == '__main__':
    main()
