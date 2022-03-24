from Action import action
from Event import event

actions = []
events = []
def max(actions):
    if len(actions) == 0:
        return None
    max = actions[0].duration
    x = 0
    while x < len(actions):
        if actions[x].duration > max:
            max = actions[x].duration
        x += 1
    return max

def min(actions):
    if len(actions) == 0:
        return None
    min = actions[0].duration
    x = 0
    while x < len(actions).duration:
        if actions[x] > min:
            min = actions[x].duration
    return min



#1
actions.append(action('A'))
actions[0].duration = 5
#2
actions.append(action('B'))
actions[1].duration = 3
actions[1].precedingActions.append(actions[0])
#3
actions.append(action('C'))
actions[2].duration = 4
#4
actions.append(action('D'))
actions[3].duration = 6
actions[3].precedingActions.append(actions[0])
#5
actions.append(action('E'))
actions[4].duration = 4
actions[4].precedingActions.append(actions[3])
#6
actions.append(action('F'))
actions[5].duration = 3
actions[5].precedingActions.append(actions[1])
actions[5].precedingActions.append(actions[2])
actions[5].precedingActions.append(actions[3])


x = 0
en = 0
while x < len(actions):
    
    print("x=",x)
    if len(actions[x].precedingActions) == 0:
        events.append(event(en))
        en +=1
        actions[x].startingEvent = events[-1]
        events[-1].earliest = 0
        events[-1].latest = 0

    else:
        found = False
        y = 0
        while y < len(actions[x].precedingActions):
            print("y=", y)
            if actions[x].precedingActions[y].endingEvent != None:
                actions[x].startingEvent = actions[x].precedingActions[y].endingEvent
                found = True
                break
            y += 1
        if found != True:
            events.append(event(en))
            en +=1
            actions[x].startingEvent = events[-1]
        y = 0
        
        while y < len(actions[x].precedingActions):
            print("y=", y)
            print(actions[x].precedingActions[y].id)
            actions[x].precedingActions[y].endingEvent = actions[x].startingEvent
            y += 1
    x += 1


events.append(event(en))

x = 0
while x < len(actions):
    if actions[x].endingEvent == None:
        actions[x].endingEvent = events[-1]
    actions[x].endingEvent.earliest = max(actions[x].precedingActions)
    x += 1 


x = 0
while x < len(actions):
    actions[x].startingEvent.earliest = max(actions[x].precedingActions)
    x += 1

print("ACTIONS")
x = 0
while x < len(actions):
    actions[x].show()
    x+=1
print("\nEVENTS")
x = 0
while x < len(events):
    events[x].show()
    x+=1


