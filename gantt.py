import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import plotly.express as px
from datetime import date
import datetime

import functions
import cpm


def draw():

    event = cpm.events
    action = cpm.actions

    start = 0
    stime = 0
    etime = functions.getCritical(action)
    t1 = 2
    t2 = 2
    tasks = list()
    # for ev in event:
    #     task = ev.id
    #     stask = ev.earliest
    #     # etask = stask + action[action.index(task)].duration
    #     etask = stask + 2
    #     tasks.append(dict(Task=task, Start=stask, End=etask))

    for ac in action:
        task = ac.id
        stask = date.today() + datetime.timedelta(days=ac.startingEvent.earliest)
        etask = stask + datetime.timedelta(days=ac.duration)
        if ac.startingEvent.id < ac.endingEvent.id:
            tasks.append(dict(Task=task, Start=stask, End=etask))

    print(tasks)
    # df = pd.DataFrame(taska)
    # df = pd.DataFrame(
    #     [
    #         dict(Task=0, Start='2008-01-02', End='2008-01-05'),
    #         dict(Task=1,Start='2008-01-05',End='2008-01-11'),
    #     ]
    # )
    fig = px.timeline(tasks, x_start="Start", x_end="End", y="Task")
    fig.update_yaxes(autorange="reversed")
    fig.write_image("./graphs/gnat.png")

    # fig, ax = plt.subplots(1, figsize=(4, 4))

    # plt.show()

