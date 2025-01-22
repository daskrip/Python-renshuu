from typing import *

class Student():
    def __init__(self, id: str, name: str, lab_1: str, lab_2: str, assignment: str, midterm: str, final_exam: str) -> None:
        self._id = id
        self._name = name
        self._lab_1 = lab_1
        self._lab_2 = lab_2
        self._assignment = assignment
        self._midterm = midterm
        self._final_exam = final_exam
        self._average = self.average()
        self._stats = [self._id, self._name, self._lab_1, self._lab_2, self._assignment, self._midterm, self._final_exam, self._average]

    def __lt__(self, other: 'Student') -> bool:
        return self._id < other._id

    def __str__(self) -> str:
        return f"id: {self._id}, name: {self._name}, lab1: {self._lab_1}, lab2: {self._lab_2}, assignment: {self._assignment}, midterm: {self._midterm}, final: {self._final_exam}"

    def average(self) -> float:
        assessments = [float(self._lab_1), float(self._lab_2), float(self._assignment), float(self._midterm), float(self._final_exam)]
        Sum = sum(assessments)
        assessment_amount = len(assessments)
        average = Sum/assessment_amount
        return average

class ComputerScienceClass():
    def __init__(self, students: List[Student], stat_names: List[str]) -> None:
        self._students = students
        self._stat_names = stat_names

    def sort_students(self) -> None:
        self._students.sort()

    def __str__(self) -> str:
        print_students = []
        for student in self._students:
            print_students.append(student.__str__())
        string_print_students = "\n".join(print_students)
        return string_print_students

    def append_average_to_stats(self) -> None:
        self._stat_names.append("Average")


with open("student_records.csv", 'r') as records:
    content = records.readlines()
    students = []
    stat_names = []
    for i in range(len(content)):
        row = content[i].split(",")
        if i == 0:
            stat_names = row
            stat_names[len(stat_names)-1] = (stat_names[len(stat_names)-1][0:len(stat_names[len(stat_names)-1])-1])
        else:
            current_student = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6][0:len(row[6])-1])
            students.append(current_student)
        eecs1015 = ComputerScienceClass(students, stat_names)

eecs1015.sort_students()
eecs1015.append_average_to_stats()

with open("student_records_reformatted.csv", 'w') as new_records:
    for i in range(len(stat_names)):
        new_records.write(str(eecs1015._stat_names[i])+",")
        for x in range(len(eecs1015._students)):
            new_records.write(str(eecs1015._students[x]._stats[i])+",")
        new_records.write("\n")

with open("student_records_reformatted.csv", 'r') as new_records:
    line = new_records.readline()
    while line != '':
        print(line)
        line = new_records.readline()