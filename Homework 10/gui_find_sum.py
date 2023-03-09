import tkinter
import tkinter.messagebox


class Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Сумма двух чисел')
        self.main_window.geometry("300x150")


        self.number1_frame = tkinter.Frame(self.main_window)
        self.number2_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.label_number1 = tkinter.Label(self.number1_frame, text='Число 1 :')
        self.input1 = tkinter.Entry(self.number1_frame)

        self.label_number2 = tkinter.Label(self.number2_frame, text='Число 2 :')
        self.input2 = tkinter.Entry(self.number2_frame)

        self.label_result_title = tkinter.Label(self.result_frame, text='Результат:')
        self.result = tkinter.StringVar()
        self.label_result_value = tkinter.Label(self.result_frame, textvariable=self.result)

        self.button_sum = tkinter.Button(self.button_frame, text='Суммировать', command=self.convert)
        self.button_quit = tkinter.Button(self.button_frame, text='Выйти', command=self.main_window.destroy)

        self.label_number1.pack(side='left', padx=(0, 5))
        self.input1.pack(side='left')
        self.label_number2.pack(side='left', padx=(0, 5))
        self.input2.pack(side='left')
        self.label_result_title.pack(side='left')
        self.label_result_value.pack(side='left')
        self.button_sum.pack(side='left')
        self.button_quit.pack(side='left', padx=(10, 0))

        self.number1_frame.pack(padx=10, pady=(10, 0))
        self.number2_frame.pack(padx=10, pady=(10, 0))
        self.result_frame.pack(pady=(10, 0))
        self.button_frame.pack(pady=10)

        tkinter.mainloop()

    def convert(self):
        result = float(self.input1.get()) + float(self.input2.get())
        self.result.set(f'{result:g}')


if __name__ == '__main__':
    gui = Gui()
