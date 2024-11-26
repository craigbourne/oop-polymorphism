class WorkerBot:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def info(self):
        print(f"I am a worker bot. My name is {self.name}. My task is {self.task}.")

    def perform_task(self):
        print("Performing factory work: assembling parts")


class CompanionBot:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def info(self):
        print(f"I am a companion bot. My name is {self.name}. My task is {self.task}.")

    def perform_task(self):
        print("Performing care work: checking on patient")


# Create instances
worker1 = WorkerBot("RoboWorker", "assembly")
companion1 = CompanionBot("CareBot", "patient monitoring")

# Demonstrate polymorphism
for robot in (worker1, companion1):
    robot.info()
    robot.perform_task()
    print()