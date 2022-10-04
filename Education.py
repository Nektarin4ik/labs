#with open('myfile.txt',mode='r+') as f:
    #f.write ('Первая строка\nВторая строка\nТретья строка\nЧетвертая строка')
    #f.read()
    #f.seek(0)
    #f.write ('Нулевая строка\n')
    #f.seek(0)
    #print (f.read())

#name = 'Alexey'

#if name == 'Nikita':
#    print ('Welcome my Boss')
#elif name == 'Sasha':
#    print ('Welcome brother our Bosses')
#else: 
#    print ('Go out!')

#mylist = [1,2,3,4,5,6,7,8,9,10]
#list_sum = 0
#for num in mylist:
#    if num % 2 ==0:
#        list_sum=list_sum+num
#    else:
#        list_sum=list_sum*num
#print (list_sum)
#with open('myfile.txt', mode='w') as f:
#    f.write ('list_sum')
#result = 50/12
#print (f'Результат: {result:1.3}')
#list(range(0,11,2))
#print(list(range(0,11,2)))
#result = input('What is your name?')
#print (f'Приветствую, {result}')
#for num in range(0,11):
#    if num%2 ==0:
#        print(num)
#list=[x for x in range (1,51) if x%3==0]
#print(list)
#st='Print every word in this sentence that has an even number of letters'
#for list in st.split():
#    if len(list) %2 ==0:
#        print (list + ' имеет четную длину')
#for list in range(1,101):
#    if list%3==0 and list%5==0:
#        print('FizzBuzz')
#    elif list%3==0:
#        print('Fizz')
#    elif list%5==0:
#        print('Buzz')
#    else:
#        print(list)
#st='Create a list of the first letters of every word in the list'
#letters=[list[0] for list in st.split()]
#print(letters)

from re import L


def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            result = b
        else:
            result = a
    else:
        if a>b:
            result = a
        else:
            result = b
    return result

def animal_crackers(text):
    wordlist=text.split()
    return wordlist[0][0]==wordlist[1][0]


def makes_twenty(n1,n2):
    if n1+n2==20 or n1==20 or n2==20:
        return True
    else:
        return False

def old_macdonald(name):
    letter1=name[0]
    inbetween=name[1:3]
    letter4=name[3]
    rest=name[4:]

def vol(rad):
    V=(4/3)*3.14*rad**3
    print(V)

def played_screen(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
test_board=('','O','X','X','O','O','O','X','O','O')
played_screen(test_board)
def choose_symbol():
    marker=''
    while marker !='X' and marker !="O":
        marker=input('Выберите символ за который будете играть: ').upper()
    if marker=='X':
        return ('X','O')
    else: 
        return ('O','X')

#player1_marker, player2_marker = choose_symbol()
#print ('Игрок 1 играет за символ {}, Игрок 2 играет за символ {}'.format (player1_marker,player2_marker))
def place_marker(board,marker,position):
    board[position]=marker
def win_check(board, mark):
    def helpme(board,mark):
        for i in board:
            if i==mark*3:
                return True 
        return False
    hor=["".join(map(str,board[1:4])),"".join(map(str,board[4:7])),"".join(map(str,board[7::]))]
    vert=["".join(map(str,board[1:8:3])),"".join(map(str,board[2:9:3])),"".join(map(str,board[3::3]))]
    diag=["".join(map(str,board[1::4])),"".join(map(str,board[3:8:2]))]
    mass=hor+vert+diag
    return helpme(mass,mark)
#        return True
#    return False
print(win_check(test_board, 'X'))

#win_check(test_board, 'X')
#    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # горизонталь сверху
#    (board[4] == mark and board[5] == mark and board[6] == mark) or # горизонталь в середине
#    (board[1] == mark and board[2] == mark and board[3] == mark) or # горизонталь снизу
#    (board[7] == mark and board[4] == mark and board[1] == mark) or # вертикаль слева
#    (board[8] == mark and board[5] == mark and board[2] == mark) or # вертикаль в середине
#    (board[9] == mark and board[6] == mark and board[3] == mark) or # вертикаль справа
#    (board[7] == mark and board[5] == mark and board[3] == mark) or # диагональ
#    (board[9] == mark and board[5] == mark and board[1] == mark)) # диагональ
#    while not (board[1-4]==mark) or (board[4-7]==mark) or (board[4-7]==mark):
#        pass
#    else:
#        return True
#print(win_check(test_board, 'X'))

import random 
def choosi_who_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board):
        position=int(input('Укажите поле: (1-9)'))
    return position
def replay():
    choice= input('Хотите сыграть снова? Введите Yes или No')
    return choice == 'Yes'


 
