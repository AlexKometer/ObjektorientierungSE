import json
from datetime import datetime
from my_function import build_person, build_experiment
from my_classes import Person, Experiment
from test import test

def main():

    print()
    print("Welcome to the experiment builder!")
    print("You have chosen to input your own information.")
    print("Please enter the following information about the experiment: ")
    print()

    name = input ("Enter the name of the subject: ")
    age = int (input ("Enter the age of the subject : "))
    person = Person (name, age)
    person.save ()
    print (f"Estimated maximum heart rate for {name}: {person.estimate_max_hr ()} bpm")
    experiment_name = input ("Enter experiment name: ")
    while True:
        check = input("Do you want to use the current date? (y/n): ")
        if check == "y":
            experiment_date = datetime.now().strftime("%d-%m-%Y")
            break
        elif check == "n":
            experiment_date = input("Enter the date(dd-mm-yyyy): ")
            break
        else:
            print("Please enter a valid input!")

    experiment = Experiment (experiment_name, experiment_date, person.name)
    experiment.save ()


if __name__ == "__main__":
    while True:
        check = input("Do you want to use test names or input your own information(test/own): ")
        if check == "test" or check == "t" or check == "T" or check == "Test":
            print("You have chosen to use pre defined test names")
            test()
            print("Test completed!")
            break
        elif check == "own" or check == "o" or check == "O" or check == "Own":
            main()
            break
        else:
            print("Please enter a valid input!")
            continue

        
