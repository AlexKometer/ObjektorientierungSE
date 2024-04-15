from my_classes import Person, Experiment

def test():
    person = Person("John Doe", 30)
    person.save()
    print(f"Estimated maximum heart rate for John Doe: {person.estimate_max_hr()} bpm")
    experiment = Experiment("Heart Rate Test", "2024-04-15", person.name)
    experiment.save()

if __name__ == "__main__":
    test()
