import tkinter as tk

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
    # main.counter += 1


if __name__ == '__main__':

    window = tk.Tk()

    id_label = tk.Label(text="ID")
    id_label.pack()
    enter_one = tk.Entry()
    enter_one.pack()

    time_label = tk.Label(text="Czas trwania")
    time_label.pack()
    enter_two = tk.Entry()
    enter_two.pack()

    predocesors_label = tk.Label(text="Poprzednicy")
    predocesors_label.pack()
    enter_three = tk.Entry()
    enter_three.pack()

    add_button = tk.Button(text="Add", command=get_data)
    # add_button.bind(get_data(enter_one.get(), enter_two.get(), enter_three.get()))
    add_button.pack()

    rdy_button = tk.Button(text="Start", command=cpm.logic)
    rdy_button.pack()

    window.mainloop()
