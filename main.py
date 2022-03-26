from Action import action
from Event import event
from functions import getCritical
from functions import replaceParallel
from functions import getAllpredecessorss
from functions import getEvents
from functions import GetEventsEarliest
from functions import GetEventsLatest
from functions import GetEventsReserve
from functions import getNotPredecessors
from functions import printActions
from functions import printEvents
from functions import printCritical

actions = []
events = []

#input
#1
actions.append(action('A'))
actions[0].duration = 5
#2
actions.append(action('B'))
actions[1].duration = 3
actions[1].predecessorsId.append('A')
#3
actions.append(action('C'))
actions[2].duration = 4
#4
actions.append(action('D'))
actions[3].duration = 6
actions[3].predecessorsId.append('A')
#5
actions.append(action('E'))
actions[4].duration = 4
actions[4].predecessorsId.append('D')
#6
actions.append(action('F'))
actions[5].duration = 3
actions[5].predecessorsId.append('B')
actions[5].predecessorsId.append('C')
actions[5].predecessorsId.append('D')

getAllpredecessorss(actions)
getEvents(events, actions)

GetEventsEarliest(events, actions)
GetEventsLatest(events, actions)
GetEventsReserve(events, actions)

replaceParallel(events,actions)

lasts = getNotPredecessors(actions)
critical = getCritical(lasts)

printActions(actions)
printEvents(events)
printCritical(critical)