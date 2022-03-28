from Action import action
from Event import event

def ispredecessors(actions, action):
    x = 0
    while x < len(actions):
        y = 0
        while y < len(actions[x].predecessors):
            if action == actions[x].predecessors[y]:
                return True
            y += 1
        x += 1
    return False

def getCritical(actions):
    critical = [0]
    x=0
    while x<len(actions):
        if len(actions[x].predecessors) == 0:
            if critical[0] < actions[x].duration:
                critical[0] = actions[x].duration
                critical.append(actions[x])
        else:
            temp = getCritical(actions[x].predecessors)
            if critical[0] < (temp[0] + actions[x].duration):
                critical = temp
                critical[0] += actions[x].duration
                critical.append(actions[x])
        x+=1
    return critical

def replace(events, actions, act):
    actions.append(action(chr(ord(actions[-1].id) + 1)))
    actions[-1].duration = 0
    actions[-1].predecessors.append(act)
    x=0
    while x<len(actions)-1:
        y=0
        while y<len(actions[x].predecessors):
            if actions[x].predecessors[y] == act:
                actions[x].predecessors[y] = actions[-1]
            y+=1
        x+=1
    events.append(event(events[-1].id + 1))
    events[-1].earliest = act.endingEvent.earliest
    events[-1].latest = act.endingEvent.latest
    events[-1].reserve = act.endingEvent.reserve
    actions[-1].startingEvent = events[-1]
    actions[-1].endingEvent = act.endingEvent
    act.endingEvent = events[-1]

def replaceParallel(events, actions):
    pn=0
    x=0
    while x<len(actions):
        y=0
        while y+1 < len(actions[x].predecessors):
            z=y+1
            while z<len(actions[x].predecessors):
                if actions[x].predecessors[y].startingEvent == actions[x].predecessors[z].startingEvent:
                    replace(events, actions, actions[x].predecessors[z])
                z+=1
            y+=1
        x+=1

    np = getNotPredecessors(actions)
    x=0
    while x<len(np):
        y=0
        while y+1 <len(np):
            if x!=y:
                if np[x].startingEvent == np[y].startingEvent:
                    replace(events,actions,np[x])
            y+=1
        x+=1

def getpredecessorss(actions, a):
    x=0
    while x < len(a.predecessorsId):
        y=0
        while y<len(actions):
            if(actions[y].id == a.predecessorsId[x]):
                a.predecessors.append(actions[y])
            y+=1
        x+=1

def getAllpredecessorss(actions):
    x=0
    while x< len(actions):
        getpredecessorss(actions,actions[x])
        x+=1

def getEvents(events, actions):
    x = 0
    en = 0
    while x < len(actions):
        if len(actions[x].predecessors) == 0:
            events.append(event(en))
            en +=1
            actions[x].startingEvent = events[-1]
        else:
            found = False
            y = 0
            while y < len(actions[x].predecessors):
                if actions[x].predecessors[y].endingEvent != None:
                    actions[x].startingEvent = actions[x].predecessors[y].endingEvent
                    found = True
                    break
                y += 1
            if found != True:
                events.append(event(en))
                en +=1
                actions[x].startingEvent = events[-1]
            y = 0
            while y < len(actions[x].predecessors):
                actions[x].predecessors[y].endingEvent = actions[x].startingEvent
                y += 1
        x += 1
    events.append(event(en))
    x = 0
    while x < len(actions):
        if actions[x].endingEvent == None:
            actions[x].endingEvent = events[-1]
        x += 1 

def GetEventsEarliest(events, actions):
    x = 0
    while x < len(actions):
        if len(actions[x].predecessors) == 0:
            actions[x].startingEvent.earliest = 0
        else:
            y = 0
            while y < len(actions[x].predecessors):
                if actions[x].predecessors[y].duration + actions[x].predecessors[y].startingEvent.earliest > actions[x].startingEvent.earliest:
                    actions[x].startingEvent.earliest = actions[x].predecessors[y].duration + actions[x].predecessors[y].startingEvent.earliest
                y += 1
        x += 1
    x = 0
    while x < len(actions):
        if ispredecessors(actions, actions[x]) == False:
            if actions[x].duration + actions[x].startingEvent.earliest > actions[x].endingEvent.earliest:
                actions[x].endingEvent.earliest = actions[x].duration + actions[x].startingEvent.earliest
                actions[x].endingEvent.latest = actions[x].endingEvent.earliest
        x += 1

def GetEventsLatest(events, actions):
    x = 1
    while x <= len(actions):
        if actions[len(actions) - x].startingEvent.latest == None:
            actions[len(actions) - x].startingEvent.latest = actions[len(actions) - x].endingEvent.latest - actions[len(actions) - x].duration
        else:
            if actions[len(actions) - x].startingEvent.latest < actions[len(actions) - x].endingEvent.latest - actions[len(actions) - x].duration:
                actions[len(actions) - x].startingEvent.latest = actions[len(actions) - x].endingEvent.latest - actions[len(actions) - x].duration
        x += 1

def GetEventsReserve(events, actions):
    x = 0
    while x < len(actions):
        if ispredecessors(actions, actions[x]) == False:
            actions[x].endingEvent.reserve = actions[x].endingEvent.latest - actions[x].endingEvent.earliest
        actions[x].startingEvent.reserve = actions[x].startingEvent.latest - actions[x].startingEvent.earliest
        x += 1

def getNotPredecessors(actions):
    notpredecessors = []
    x = 0
    while x < len(actions):
        if ispredecessors(actions, actions[x]) == False:
            notpredecessors.append(actions[x])
        x += 1
    return notpredecessors

def printActions(actions):
    print("\nACTIONS")
    x = 0
    while x < len(actions):
        actions[x].show()
        x+=1

def printEvents(events):
    print("\nEVENTS")
    x = 0
    while x < len(events):
        events[x].show()
        x+=1

def printCritical(critical):
    print("\nCRITICAL (lenght = ",critical[0],")")
    x = 1
    while x < len(critical):
        critical[x].show()
        x+=1