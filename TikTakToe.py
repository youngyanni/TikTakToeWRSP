# Игра Крестики-нолики с графическим интерфейсом
# с помощью tkinter
# импорт всех необходимых библиотек
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import array as arr

import RSP
from RSP import *

button = []
# Создает пустую доску
global board
board = [[" " for x in range(3)] for y in range(3)]


# Проверить l(O/X) выиграл матч или нет по правилам игры
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


# текст на кнопке во время игры с другим игроком
def get_text(i, j, gb, l1, l2):
    if board[i][j] == ' ':
        if l1['state'] == ACTIVE:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Победа", "Игрок 1 выиграл")

    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Победа", "Игрок 2 выиграл")

    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("Ничья", "Ничья")


# Проверяем, может ли игрок нажать на кнопку или нет
def isfree(i, j):
    return board[i][j] == " "


# Проверяем, заполнена доска или нет
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


# Создайте графический интерфейс игрового поля для игры вместе с другим игроком
def gameboard_pl(game_board, l1, l2):
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8, state=DISABLED)
            button[i][j].grid(row=m, column=n)


# Инициализировать игровое поле для игры с другим игроком
def withplayer(game_board1):
    game_board1.destroy()
    global game_board, button
    game_board = Tk()
    game_board.resizable(width=False, height=False)
    game_board.title("Крестики-нолики")
    l1 = Button(game_board, text="Игрок 1 : X", width=10)
    l2 = Button(game_board, text="Игрок 2 : O", width=10)
    choose_pl = Button(game_board, text="Кто ходит первый?", width=20, command=lambda: (
    game_board.withdraw(), choose_pl.grid_forget(), RSP.RSPplay(game_board, button, l1, l2)))
    choose_pl.grid(row=2, columnspan=3)
    gameboard_pl(game_board, l1, l2)
    game_board.mainloop()


# главная функция
def play():
    menu = Tk()
    menu.geometry("325x113")
    menu.title("Крестики-нолики")
    wpl = partial(withplayer, menu)

    head = Button(menu, text="---Добро пожаловать---",
                  activeforeground='red',
                  activebackground="yellow", bg="grey",
                  fg="black", width=500, font='summer', bd=5)

    B2 = Button(menu, text="Многопользовательский режим", command=wpl,
                activeforeground='red',
                activebackground="yellow", bg="gray", fg="black",
                width=500, font='summer', bd=5)

    B3 = Button(menu, text="Выход", command=menu.quit,
                activeforeground='red',
                activebackground="yellow", bg="grey", fg="black",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


if __name__ == '__main__':
    play()
    SystemExit(1)
