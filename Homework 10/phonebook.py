import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle


class Gui:
    def __init__(self):

        # file which stores list with contacts
        self.filename = 'contacts.dat'
        self.contacts = self.load_contacts()
        # main window
        self.main_window = Tk()
        self.main_window.title('Телефонная книга')
        self.main_window.geometry("400x400")
        # frames
        self.name_frame = Frame(self.main_window)
        self.phone_frame = Frame(self.main_window)
        self.contact_list_frame = Frame(self.main_window)
        self.button_frame = Frame(self.main_window)
        # widgets for inputting of names and phones
        self.label_name = Label(self.name_frame, text='Имя :')
        self.input_name = Entry(self.name_frame)
        self.label_phone = Label(self.phone_frame, text='Номер телефона :')
        self.input_phone = Entry(self.phone_frame)

        # table creating
        self.columns = ('name', 'phone')
        self.tree = ttk.Treeview(columns=self.columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.tree.heading('name', text='Имя')
        self.tree.heading('phone', text='Номер телефона')

        # displaying of saved contacts from file 'contacts.dat'
        for person in self.contacts:
            self.tree.insert("", END, values=person)

        # buttons
        self.button_add = Button(self.button_frame, text='Добавить', command=self.add_record)
        self.button_del = Button(self.button_frame, text='Удалить', command=self.del_record)
        self.button_quit = Button(self.button_frame, text='Выйти и сохранить', command=self.quit)

        # render all widgets
        self.label_name.pack(side='left', padx=(0, 5))
        self.input_name.pack(side='left')
        self.label_phone.pack(side='left', padx=(0, 5))
        self.input_phone.pack(side='left')

        self.button_add.pack(side='left')
        self.button_del.pack(side='left')
        self.button_quit.pack(side='left', padx=(10, 0))

        self.name_frame.pack(padx=10, pady=(10, 0))
        self.phone_frame.pack(padx=10, pady=(10, 0))
        self.button_frame.pack(pady=10)

        mainloop()

    def add_record(self):
        self.contacts.append([self.input_name.get(), self.input_phone.get()])
        for person in [(self.input_name.get(), self.input_phone.get())]:
            self.tree.insert("", END, values=person)
        self.tree.config(height=len(self.tree.get_children()))
        self.input_name.delete(0, END)
        self.input_phone.delete(0, END)
        tkinter.messagebox.showinfo('Уведомление', 'Номер добавлен!')

    def del_record(self):
        # разобраться с неявным преобразованием значений из values!
        row = self.tree.item(self.tree.selection())["values"]
        # доработать !
        correct_row = [str(row[0]), str(row[1])]
        self.contacts.remove(correct_row)
        item = self.tree.selection()[0]
        self.tree.delete(item)
        # self.tree.config(height=len(self.tree.get_children()))

    def load_contacts(self):
        try:
            input_file = open(self.filename, 'rb')
            contact_list = pickle.load(input_file)
            input_file.close()
        except IOError:
            contact_list = []
        return contact_list

    def save_contacts(self):
        output_file = open(self.filename, 'wb')
        pickle.dump(self.contacts, output_file)
        output_file.close()

    def quit(self):
        self.save_contacts()
        self.main_window.destroy()


if __name__ == '__main__':
    gui = Gui()

