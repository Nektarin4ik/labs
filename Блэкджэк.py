import random
suits=('Червы', 'Пики', 'Бубны', 'Трефы')
ranks=('Двойка','Тройка','Четверка','Пятерка','Шестерка','Семерка','Восьмерка','Девятка','Десятка','Валет','Дама','Король','Туз')
values={'Двойка':2,'Тройка':3,'Четверка':4,'Пятерка':5,'Шестерка':6,'Семерка':7,'Восьмерка':8,'Девятка':9,'Десятка':10,'Валет':10,'Дама':10,'Король':10,'Туз':11}

playing=True

class Card():
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
    def __str__(self): 
        return self.rank+' '+self.suit

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp += '\n' +card.__str__()
        return 'В колоде находятся карты:' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):

        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):

        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1


class Chips():

    def __init__(self,total= 100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total-= self.bet

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('Введите ставку которую желаете поставить: '))
        
        except:
            print('Введите целое число')
        else:
            if chips.bet> chips.total:
                print (f'Недостаточно фишек, ваш баланс фишек: {chips.total}')
                continue
        break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    

def hit_or_stand(deck,hand):
    
    global playing

    while True:
        x = input('Хотите ли вы взять еще карту(hit) или остаться при своих (stand), введите h или s соответственно: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
            return hand
        elif x[0].lower() == 's':
            print('Добор карт окончен, ходит диллер')
            playing=False
        break

def player_busts(player, dealer,chips):
    print('Игрок проиграл')
    chips.lose_bet()

def player_wins(player, dealer,chips):
    print('Игрок выиграл')
    chips.win_bet()

def dealer_busts(player, dealer,chips):
    print('Диллер перебрал! Вы выиграли')
    chips.win_bet()

def dealer_wins(player, dealer,chips):
    print('Диллер выиграл!')
    chips.lose_bet()

def push(player, dealer):
    print('Ничья!')

def show_some(player, dealler):
    print('\nКарты диллера')
    print('\n<карта скрыта>')
    print('', dealler.cards[1])
    print('\nКарты игрока:', *player.cards, sep='\n ')

def show_all(player, dealler):
    print('\nКарты диллера', *dealler.cards, sep='\n ')
    print('Карты диллера =', dealler.value)
    print('\nКарты игрока:', *player.cards, sep='\n ')
    print('Карты игрока =', player.value)
    

while True:


    print ('Добро пожаловать в Блэкджэк!')

    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    dealer_hand=Hand()
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    chips_player = Chips(1000)

    take_bet(chips_player)

    show_some(player_hand, dealer_hand)

    while playing: 

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    if player_hand.value <=21: 
        while dealer_hand.value <17: 
            hit (deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21: 
            dealer_busts(player_hand, dealer_hand, chips_player)
        elif dealer_hand.value > player_hand.value: 
            dealer_wins(player_hand, dealer_hand, chips_player)
        elif dealer_hand.value < player_hand.value: 
            player_wins(player_hand, dealer_hand, chips_player)
        else:
            push(player_hand, dealer_hand)

    print (f'\n Количество фишек игрока: {chips_player.total}')

    new_game = input('Хотите ли вы сыграть снова? y -да, n - нет: ')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        break


