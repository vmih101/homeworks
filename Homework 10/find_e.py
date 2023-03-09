from tkinter import *
from tkinter import messagebox


class Gui:
    def __init__(self):
        # main window initialization
        self.main_window = Tk()
        self.main_window.geometry('400x100')
        self.main_window.title('Find "E"')
        # frames
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        # top frame widgets
        self.entry_descr = Label(self.top_frame, text='Введите список слов :')
        self.string_input = Entry(self.top_frame, width=50)
        # bottom frame widgets
        self.button = Button(self.bottom_frame, text='Найти "E"', width=15, command=self.find_e)
        # widgets rendering
        self.entry_descr.pack()
        self.string_input.pack()
        self.button.pack()
        self.top_frame.pack(pady=(10, 0))
        self.bottom_frame.pack(pady=10)

        mainloop()

    def find_e(self):
        count = 0
        s = self.string_input.get().lower().split()
        for word in s:
            if (word.find('е') and word.find('e')) != -1:
                count += 1
        messagebox.showinfo('Результат', f'Обнаружено {count} слов(a) содержащих символ "E"')


if __name__ == '__main__':
    gui = Gui()

