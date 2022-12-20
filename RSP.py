import array as arr
from tkinter import *
from tkinter import Image
from tkinter import ttk
from tkinter import messagebox


class RSPplay:

    def __init__(self, menu, button, l1, l2):
        global scr
        self.scr = arr.array('i', [0, 0])
        menu.withdraw()
        self.wind = Toplevel(menu)
        self.wind.geometry('525x430+650+300')
        self.wind.resizable(width=False, height=False)
        self.wind.image = PhotoImage(file='F:\\Pictures\\fon.png')
        bg_logo = Label(self.wind, image=self.wind.image)
        bg_logo.grid(row=0, column=0, columnspan=4)
        self.wind.title("Камень, ножницы, бумага")
        self.wind.e1 = Entry(self.wind, width=20, borderwidth=5)
        self.wind.e1.insert(0, 'Ход 1-го игрока')
        self.wind.e1.grid(row=1, column=0, sticky=W + E)
        self.wind.btn3 = Button(self.wind, text="Играть", command=lambda: self.BtnPlayModeFriends(menu, button, l1, l2))
        self.wind.btn3.grid(column=1, row=1, sticky=W + E, columnspan=2)
        self.wind.e2 = Entry(self.wind, width=20, borderwidth=5)
        self.wind.e2.grid(row=1, column=3, sticky=W + E)
        self.wind.e2.insert(0, 'Ход 2-го игрока')
        self.wind.e1.bind('<Enter>', self.Enter1)
        self.wind.e2.bind('<Enter>', self.Enter2)
        self.wind.mainloop()


    def BtnPlayModeFriends(self, menu, button, l1, l2):
        pl1 = self.wind.e1.get()
        pl2 = self.wind.e2.get()
        if pl1.isdigit() == False or pl2.isdigit() == False or int(pl1) > 2 or int(pl1) < 0 or int(pl2) > 2 or int(
                pl2) < 0:
            excpt = Toplevel(self.wind)
            excpt.resizable(width=False, height=False)
            excpt.title("Ошибка")
            excpt.geometry('250x100')
            text = Text(excpt, width=250, height=100, bg='red', fg='white', font="Courier 20")
            text.insert(INSERT, "Неверный формат \nВведите: 0 или 1 или 2")
            text.pack()
        else:
            if self.scr[0] == self.scr[1]:
                result = int(pl1) - int(pl2)
                match result:
                    case 0:
                        self.wind.e1.configure(bg="green")
                        self.wind.e2.configure(bg="green")
                    case 1:
                        self.wind.e1.configure(bg="red")
                        self.wind.e2.configure(bg="green")
                        self.scr[1] = self.scr[1] + 1
                    case 2:
                        self.wind.e1.configure(bg="green")
                        self.wind.e2.configure(bg="red")
                        self.scr[0] = self.scr[0] + 1
                    case -1:
                        self.wind.e1.configure(bg="green")
                        self.wind.e2.configure(bg="red")
                        self.scr[0] = self.scr[0] + 1
                    case -2:
                        self.wind.e1.configure(bg="red")
                        self.wind.e2.configure(bg="green")
                        self.scr[1] = self.scr[1] + 1
            if self.scr[0] != self.scr[1]:
                if self.scr[0] > self.scr[1]:
                    self.wind.destroy()
                    box = messagebox.showinfo('Результат', 'Первым ходит первый игрок')
                    menu.deiconify()
                else:
                    self.wind.destroy()
                    box = messagebox.showinfo('Результат', 'Первым ходит второй игрок')
                    menu.deiconify()
        for i in range(3):
            for j in range(3):
                button[i][j].configure(state=ACTIVE)
        if self.scr[0] != 0:
            l1.configure(state=ACTIVE)
            l1.grid(row=1, column=1)
            l2.configure(state=DISABLED)
            l2.grid(row=2, column=1)
        else:
            l1.configure(state=DISABLED)
            l1.grid(row=1, column=1)
            l2.configure(state=ACTIVE)
            l2.grid(row=2, column=1)

    def Enter1(self, event):
        self.wind.e1.delete(0, END)
        self.wind.e1['show'] = "*"
        self.wind.e1['bg'] = 'white'

    def Enter2(self, event):
        self.wind.e2.delete(0, END)
        self.wind.e2['show'] = "*"
        self.wind.e2['bg'] = 'white'


if __name__ == '__main__':
    wind = RSPplay()
