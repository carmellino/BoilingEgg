import tkinter as tk
from tkinter import ttk

import cpm

counter = 0


def get_data():
    print('xd')
    id = enter_one.get()
    time = enter_two.get()
    predo = enter_three.get()
    print(id)
    print(time)
    print(predo)
    cpm.process_data(id, time, predo)
    enter_one.delete(0, tk.END)
    enter_two.delete(0, tk.END)
    enter_three.delete(0, tk.END)
    table.insert(parent='', index='end', text='',
                 values=(id, time, predo))
    # counter += 1


if __name__ == '__main__':

    window = tk.Tk()
    window.title("CPM")
    # window.grid()

    id_label = tk.Label(text="ID")
    id_label.grid(row=0, column=0)
    enter_one = tk.Entry()
    enter_one.grid(row=1, column=0, padx=5)

    time_label = tk.Label(text="Czas trwania")
    time_label.grid(row=0, column=1)
    enter_two = tk.Entry()
    enter_two.grid(row=1, column=1, padx=5)

    predocesors_label = tk.Label(text="Poprzednicy")
    predocesors_label.grid(row=0, column=3)
    enter_three = tk.Entry()
    enter_three.grid(row=1, column=3, padx=5)

    add_button = tk.Button(text="Add", command=get_data, width=25)
    # add_button.bind(get_data(enter_one.get(), enter_two.get(), enter_three.get()))
    add_button.grid(row=0, column=4, pady=5, sticky=tk.NS)

    rdy_button = tk.Button(text="Start", command=cpm.logic, width=25)
    rdy_button.grid(row=1, column=4, padx=5, sticky=tk.NS)

    table = ttk.Treeview()

    table['columns'] = ('id', 'Time', 'Predocesors')

    table.column("#0", width=0)
    table.column("id", width=40)
    table.column("Time", width=80)
    table.column("Predocesors", width=80)

    table.heading("#0", text='')
    table.heading("id", text='Event ID')
    table.heading("Time", text='Time')
    table.heading("Predocesors", text='Predocesors')

    table.grid(row=3, columnspan=3)



    window.mainloop()
