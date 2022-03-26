class action:
    id = None
    duration = 0
    startingEvent = None
    endingEvent = None
    
    def __init__(self, id):
        self.id = id
        self.predecessors = list()
        self.predecessorsId = list()

    def showid(self):
        print(self.id)

    def show(self):
        print("id", self.id, " duration", self.duration, " start", self.startingEvent.id, " end", self.endingEvent.id)
        if len(self.predecessors) > 0:
            print("predecesors:")
            x = 0
            while x < len(self.predecessors):
                print(self.predecessors[x].id)
                x+=1
        print()
