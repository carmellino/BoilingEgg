

class action:
    id = None
    duration = None
    startingEvent = None
    endingEvent = None
    
    def __init__(self, id):
        self.id = id
        self.precedingActions = list()

    def showid(self):
        print(self.id)

    def show(self):
        print(self.id, self.duration, self.startingEvent.id, self.endingEvent.id)
        x = 0
        while x < len(self.precedingActions):
            print(self.precedingActions[x].id)
            x+=1
    
