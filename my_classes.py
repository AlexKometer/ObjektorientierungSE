import json
from datetime import datetime

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self._birthdate = birthdate  # Hidden attribute

    def save(self):
        with open(f'{self.name}.json', 'w') as f:
            json.dump({'name': self.name, 'birthdate': self._birthdate}, f)

    def get_birthdate(self):
        return self._birthdate

class Subject(Person):
    def estimate_max_hr(self):
        birthdate = datetime.strptime(self.get_birthdate(), '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return 220 - age

class Examiner(Person):
    pass

class Experiment:
    def __init__(self, name, date, subject):
        self.name = name
        self.date = date
        self.subject = subject

    def save(self):
        with open(f'{self.name}_experiment.json', 'w') as f:
            json.dump(self.__dict__, f)
