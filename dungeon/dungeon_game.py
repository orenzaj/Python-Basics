"""Dungeon Game
Explore a dungeon to find a hidden door and escape. But be careful!
The grue is hiding somewhere inside!

Created: 2014
Updated: 2015
Author: John Flipsie
"""
import random
import os
import sys

def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y

    
def get_moves(player, length, width):
    x, y = player
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    if x == 0:
        moves.remove("LEFT")
    if x == length - 1:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == width - 1:
        moves.remove("DOWN")
    return moves

def get_cell_size(length, width):
    cells = []
    for y in range(0, width):
        for x in range(0, length):
            cells.append((x, y))
    return cells


def get_position(cells):
    return random.sample(cells, 3)


def clear_screen():
    """Clear the screen"""
    os.system('cls') if os.name == 'nt' else os.system('clear')
    return ("\n"*50)

def draw_grid(player, monster, door, cells):
    print(" _"*5)
    tile = "|{}"
    
    for cell in cells:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    cells = get_cell_size(5, 5)
    player, monster, door = get_position(cells)
    
    while True:
        clear_screen()
        draw_grid(player, monster, door, cells)
        valid_moves = get_moves(player, 5, 5)


        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter 'QUIT' to quit")

        move = input("> ").upper()

        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player,move)

            if player == monster:
                print("You encountered a monster and got eaten! You lose!")
                break
            if player == door:
                print("You escaped the dungeon! Congratulations!")
                break
            
        else:
            input("\n ** Don't run into walls! **\n")
            continue

clear_screen()
print("Welcome to the dungeon!")
input("Press 'Enter' to start!")
clear_screen()
game_loop()
    
