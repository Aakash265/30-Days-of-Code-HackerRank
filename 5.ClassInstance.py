class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        newAge = self.initialAge
        if (newAge < 0):
            self.initialAge = newAge = 0
            print("Age is not valid, setting age to 0.")
            print("You are young.")
        elif (newAge < 13):
            print("You are young.")
        elif (newAge >= 13 and newAge < 18):
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge = self.initialAge + 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

