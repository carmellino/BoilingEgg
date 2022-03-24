class event:
    id = None
    earliest = None
    latest = None
    reserve = None
    def __init__(self, id):
        self.id = id

    def show(self):
        print(self.id, self.earliest, self.latest, self.reserve)