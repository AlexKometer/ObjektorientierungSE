from my_classes import Subject, Experiment

def test():
    subject = Subject("John Doe", "1994-04-15")
    subject.save()
    print(f"Estimated maximum heart rate for John Doe: {subject.estimate_max_hr()} bpm")
    experiment = Experiment("Heart Rate Test 6.2", "2024-04-15", subject.name)
    experiment.save()

if __name__ == "__main__":
    test()

