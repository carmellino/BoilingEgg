import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import cpm
import gantt

counter = 0


class activ:

    def __init__(self, i,t,p):
        self.id = i
        self.time = t
        self.predo = p


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

    table2.grid(row=3, column=0, sticky=tk.W + tk.N)


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
    data.append(activ(id,time,predo))

    # counter += 1

def popup_gunt():
    global gunt
    gun = tk.Toplevel()
    gunt = ImageTk.PhotoImage(Image.open("./graphs/gnat.png"))
    gant = tk.Label(gun, image=gunt)
    gant.grid(column=0, row=0)
    button_close = tk.Button(gun, text="close", command=gun.destroy)
    button_close.grid(row=2, columnspan=4)


def draw_activity_table():
    table3 = ttk.Treeview(frame_two)

    table3['columns'] = ('id', 'Time', 'Predocesors')

    table3.column("#0", width=0)
    table3.column("id", width=40)
    table3.column("Time", width=80)
    table3.column("Predocesors", width=80)

    table3.heading("#0", text='')
    table3.heading("id", text='Event ID')
    table3.heading("Time", text='Time')
    table3.heading("Predocesors", text='Predocesors')
    for x in data:
        table3.insert(parent='', index='end', text='',
                     values=(x.id, x.time, x.predo))
    tit = tk.Label(frame_two, text="Czynnosci")
    tit.grid(row=4, column=0)
    table3.grid(row=5, column=0)



def start_logic():
    global img
    cpm.logic()
    create_second_table()
    title = tk.Label(frame_two, text="Event table")
    title.grid(row=2,column=0)
    img = ImageTk.PhotoImage(Image.open("./test-output/Digraph.gv.png"))
    photo = tk.Label(frame_two, image=img)
    photo.grid(column=3, rowspan=5, row=2, sticky=tk.N)
    gant_button = tk.Button(frame_two, text="gantt graph", command=popup_gunt,width=60)
    gant_button.grid(columnspan=3, row=1)
    start_frame.pack_forget()
    draw_activity_table()
    frame_two.pack()
    gantt.draw()


if __name__ == '__main__':
    global data
    data = list()
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

    window.mainloop()
