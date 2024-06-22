class ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        if(ship.draft - (ship.crew * 1.5) > 20):
            return True
        else:
            return False