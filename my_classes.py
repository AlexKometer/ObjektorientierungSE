import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        with open(f'{self.name}.json', 'w') as f:
            json.dump(self.__dict__, f)

    def estimate_max_hr(self):
        return 220 - self.age

class Experiment:
    def __init__(self, name, date, subject):
        self.name = name
        self.date = date
        self.subject = subject

    def save(self):
        with open(f'{self.name}_experiment.json', 'w') as f:
            json.dump(self.__dict__, f)
