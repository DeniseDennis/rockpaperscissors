#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Human(Player):
    def __init__(self):
        super().__init__()
        self.playstyle = 'human'

    def move(self):
        while True:
            move = input('What Move?\n rock / paper / scissors\n ').lower()
            if move in moves:
                return move
            else:
                print('This move is not valid! Please try again')


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class BoringPlayer(Player):
    def move(self):
        return 'rock'


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            option = moves.index(self.my_move) + 1
            if option == len(moves):
                option = 0
            return moves[option]


def p1_beat(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def p2_beat(one, two):
    return ((one == 'scissors' and two == 'rock') or
            (one == 'paper' and two == 'scissors') or
            (one == 'rock' and two == 'paper'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        if p1_beat(move1, move2) is True and p2_beat(move1, move2) is False:
            self.p1.score += 1
            print('Player 1 Wins\n')
        elif p2_beat(move1, move2) is True and p1_beat(move1, move2) is False:
            self.p2.score += 1
            print('Player 2 Wins\n')
        else:
            print('Tie!\n')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f'Score Player 1: {self.p1.score}  Player 2: {self.p2.score}')

    def play_game(self):
        print("Game start!")
        self.p1.score = 0
        self.p2.score = 0
        for round in range(3):
            print(f"\n \nRound {round + 1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':

    moves = ['rock', 'paper', 'scissors']

    playstyle = {
                'random': RandomPlayer(),
                'human': Human(),
                'slick': CyclePlayer(),
                'reflect': ReflectPlayer(),
                'boring': BoringPlayer()
    }
    while True:
        print('Welcome to Rock Paper Scissors!')
        opponent = input('Who will you play? : random / slick /'
                         ' reflect / boring\n').lower()
        if opponent in playstyle:
            game = Game(playstyle['human'], playstyle[opponent])
            game.play_game()
        else:
            print('Sorry that player is not available')
