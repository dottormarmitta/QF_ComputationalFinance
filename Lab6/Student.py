# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# Part 1: the class
# #
class Student:

    # Constructor:
    # name, surname and studyCourse are STRING
    # matriculNumber is an INTEGER
    # exam is a DICTONARY<string, list[mark, credits]>
    def __init__(self, name, surname, matriculNumber, studyCourse, exams):
        self.name = name
        self.surname = surname
        self.matriculNumber = matriculNumber
        self.studyCourse = studyCourse
        self.exams = exams
    
    # Read the object:
    def __str__(self):
        return "This is " + self.name + " " + self.surname
    
    # Add exam
    def addExam(self, matriculationNumber, examName, score, credits):
        if (self.matriculNumber == matriculationNumber):
            self.exams[examName] = [score, credits]
    
    # Get average
    def getAverage(self):
        sumCredits = 0
        weightedSum = 0
        for key in self.exams:
            sumCredits  += self.exams[key][1]
            weightedSum += self.exams[key][0]*self.exams[key][1]
        return weightedSum/sumCredits

# #
# Part 2: some testing
# # 
exams = {
    "Calculus": [25, 12],
    "Econometrics": [28, 6],
    "Statistics": [29, 6],
    "FinMath": [30, 6],
    "Risk managment": [28, 6],
    "Law": [23, 6]
}
studente1 = Student("Rolando", "Foglia", 57483, "QF", exams)
print(studente1)
print("Average is: ", studente1.getAverage())
# Adding Stochastic processes exam:
studente1.addExam(57483, "StochProc", 30, 6)
print("New average is: ", studente1.getAverage())