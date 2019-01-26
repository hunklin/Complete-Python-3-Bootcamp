
def display_chess(board):
    for i in range(19):
        print()
    for line in board:
        print(line[0] + line[1] + line[2])

def main():
    board = [['_','_','_'],['_','_','_'],['_','_','_']]
    for i in range(9):
        input_text = input('input your position:\n')
        x, y = input_text.split(',')
        if i%2 == 0:
            board[int(x)][int(y)] = 'X'
        else:
            board[int(x)][int(y)] = 'O'
        display_chess(board)

if __name__ == '__main__':
    main()
