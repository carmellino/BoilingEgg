import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import cpm

counter = 0


def create_second_table():
    global table2
    table2 = ttk.Treeview(frame_two)

    table2['columns'] = ('id', 'Earliest', 'Latest', 'Free')

    table2.column("#0", width=0)
    table2.column("id", width=40)
    table2.column("Earliest", width=80)
    table2.column("Latest", width=80)
    table2.column("Free", width=80)

    table2.heading("#0", text='')
    table2.heading("id", text='Event ID')
    table2.heading("Earliest", text='Eariliest start')
    table2.heading("Latest", text='Latest start')
    table2.heading("Free", text="Free")

    for x in cpm.events:
        id = x.id
        ear = x.earliest
        lat = x.latest
        res = x.reserve
        table2.insert(parent='', index='end', text='',
                    values=(id, ear, lat, res))

    table2.grid(row=1, column=0, columnspan=3, sticky=tk.W + tk.N)


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


def start_logic():
    global img
    cpm.logic()
    create_second_table()
    title = tk.Label(frame_two, text="Activity table")
    title.grid(row=0,column=2)
    img = ImageTk.PhotoImage(Image.open("./test-output/Digraph.gv.png"))
    photo = tk.Label(frame_two, image=img)
    photo.grid(column=3, row=1)
    start_frame.pack_forget()
    frame_two.pack()


if __name__ == '__main__':

    window = tk.Tk()
    window.title("CPM")
    window.geometry("800x800")


    start_frame = tk.Frame(window, width=800, height=800)
    start_frame.pack()

    id_label = tk.Label(start_frame, text="ID")
    id_label.grid(row=0, column=0)
    enter_one = tk.Entry(start_frame)
    enter_one.grid(row=1, column=0, padx=5)

    time_label = tk.Label(start_frame, text="Czas trwania")
    time_label.grid(row=0, column=1)
    enter_two = tk.Entry(start_frame)
    enter_two.grid(row=1, column=1, padx=5)

    predocesors_label = tk.Label(start_frame, text="Poprzednicy")
    predocesors_label.grid(row=0, column=3)
    enter_three = tk.Entry(start_frame)
    enter_three.grid(row=1, column=3, padx=5)

    add_button = tk.Button(start_frame, text="Add", command=get_data, width=25)
    # add_button.bind(get_data(enter_one.get(), enter_two.get(), enter_three.get()))
    add_button.grid(row=0, column=4, pady=5, sticky=tk.NS)

    rdy_button = tk.Button(start_frame, text="Start", command=start_logic, width=25)
    rdy_button.grid(row=1, column=4, padx=5, sticky=tk.NS)

    table = ttk.Treeview(start_frame)

    table['columns'] = ('id', 'Time', 'Predocesors')

    table.column("#0", width=0)
    table.column("id", width=40)
    table.column("Time", width=80)
    table.column("Predocesors", width=80)

    table.heading("#0", text='')
    table.heading("id", text='Event ID')
    table.heading("Time", text='Time')
    table.heading("Predocesors", text='Predocesors')

    table.grid(row=3, columnspan=4, sticky=tk.W+tk.E+tk.S)

    frame_two = tk.Frame(window)
    # frame = tk.Frame(frame_two, width=200, height=200)
    # frame.grid(row=3, column=4)

    window.mainloop()
