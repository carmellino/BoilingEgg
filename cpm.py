# import main
# from Action import action
# from Event import event
from Graph import DrawGraph
# from functions import getCritical
# from functions import replaceParallel
# from functions import getAllpredecessorss
# from functions import getEvents
# from functions import GetEventsEarliest
# from functions import GetEventsLatest
# from functions import GetEventsReserve
# from functions import getNotPredecessors
# from functions import printActions
# from functions import printEvents
# from functions import printCritical
from Graph import DrawGraph
from functions import *
#kurwa jaki ty mądry jesteś <3

actions = []
events = []


def process_data(id, time, predo):

    # TODO:
    #  Cast data to make them operable by the rest of algorithm

    actions.append(action(id))
    actions[-1].duration = int(time)
    '''
    str = predo.split(',')

    for x in str:
        actions[main.counter].predecessorsId.append(str)
    main.counter += 1
    '''
    str = predo
    x=0
    while x<len(str):
        actions[-1].predecessorsId.append(str[x])
        x+=1

def hardcode_data():
    # input
    # 1
    actions.append(action('A'))
    actions[0].duration = 5
    # 2
    actions.append(action('B'))
    actions[1].duration = 3
    actions[1].predecessorsId.append('A')
    # 3
    actions.append(action('C'))
    actions[2].duration = 4
    # 4
    actions.append(action('D'))
    actions[3].duration = 6
    actions[3].predecessorsId.append('A')
    # 5
    actions.append(action('E'))
    actions[4].duration = 4
    actions[4].predecessorsId.append('D')
    # 6
    actions.append(action('F'))
    actions[5].duration = 3
    actions[5].predecessorsId.append('B')
    actions[5].predecessorsId.append('C')
    actions[5].predecessorsId.append('D')


def logic():
    getAllpredecessorss(actions)
    #printActions(actions)
    getEvents(events, actions)
    printEvents(events)
    GetEventsEarliest(events, actions)
    GetEventsLatest(events, actions)
    GetEventsReserve(events, actions)

    replaceParallel(events, actions)
    global critical
    lasts = getNotPredecessors(actions)
    critical = getCritical(lasts)

    printActions(actions)
    printEvents(events)
    printCritical(critical)

    DrawGraph.draw(actions)