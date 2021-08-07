import card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def set_hands(self, cards):
        self.cards = cards
    
    def set_exchange(self, left, across, right):
        self.selected = [
            self.cards[left], 
            self.cards[across],
            self.cards[right],
            ]

    def __repr__(self):
        return "Player('{}')".format(self.name)
    def __str__(self):
        return "Player "+ self.name

class Game:
    def __init__(self):
        self.players = [
            Player("A"),
            Player("B"),
            Player("C"),
            Player("D"),
        ]
        self.team=[]
        self.field=None

    def make_team(self):
        """팀 나누기
        """
        self.team.append([self.players[0], self.players[1]])
        self.team.append([self.players[2], self.players[3]])

    def draw(self):
        """카드 나눠주기
        """
        deck = card.Deck()
        deck.shuffle()
        for i in range(len(self.players)):
            self.players[i].set_hands(sorted(deck[i*14:(i+1)*14]))

    def who_has_MahJong(self):
        for player in self.players:
            if 1 in player.cards[:2]:
                return player

    def exchange(self):
        """카드교환
        top: team[0][0]
        right: team[1][0]
        bottom: team[0][1]
        left: team[1][1]
        """

        me = self.team[0][0]
        self.team[1][0].cards.append(me.selected[0])
        self.team[0][1].cards.append(me.selected[1])
        self.team[1][1].cards.append(me.selected[2])
        for i in range(3):
            me.cards.remove(me.selected[i])

        me = self.team[1][0]
        self.team[0][1].cards.append(me.selected[0])
        self.team[1][1].cards.append(me.selected[1])
        self.team[0][0].cards.append(me.selected[2])
        for i in range(3):
            me.cards.remove(me.selected[i])

        me = self.team[0][1]
        self.team[1][1].cards.append(me.selected[0])
        self.team[0][0].cards.append(me.selected[1])
        self.team[1][0].cards.append(me.selected[2])
        for i in range(3):
            me.cards.remove(me.selected[i])

        me = self.team[1][1]
        self.team[0][0].cards.append(me.selected[0])
        self.team[1][0].cards.append(me.selected[1])
        self.team[0][1].cards.append(me.selected[2])
        for i in range(3):
            me.cards.remove(me.selected[i])

    def init(self):
        self.make_team()
        self.draw()

    def start(self):
        starter = self.who_has_MahJong()
        print(starter.cards)

if __name__=="__main__":
    game = Game()
    game.init()

    player_A = game.players[0]
    player_B = game.players[1]
    player_C = game.players[2]
    player_D = game.players[3]

    # print(player_A.cards)
    # print(player_B.cards)
    # print(player_C.cards)
    # print(player_D.cards)

    player_A.set_exchange(1, 2, 3)
    player_B.set_exchange(1, 2, 3)
    player_C.set_exchange(1,2,3)
    player_D.set_exchange(1,2,3)

    game.exchange()

    game.start()