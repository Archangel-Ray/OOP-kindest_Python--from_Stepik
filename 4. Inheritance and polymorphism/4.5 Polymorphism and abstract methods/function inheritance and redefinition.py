# The program declares two classes:
#
# classStudent:
#     def __init__(self, fio, group):
#         self._fio = fio # student name (string)
#         self._group = group # group (string)
#         self._lect_marks = [] # lecture marks
#         self._house_marks = [] # homework marks
#
#     def add_lect_marks(self, mark):
#         self._lect_marks.append(mark)
#
#     def add_house_marks(self, mark):
#         self._house_marks.append(mark)
#
#     def __str__(self):
#         return f'Student {self._fio}: lecture grades: {str(self._lect_marks)}; house marks: {str(self._house_marks)}'
#
#
# class Mentor:
#     def __init__(self, fio, subject):
#         self._fio = fio
#         self._subject = subject
#
# The first class describes the students and the second class describes the mentors.
# You are instructed to develop two more child classes based on the Mentor base class:
#
# Lector - to describe lecturers;
# Reviewer - for the description of experts.
#
# Objects of these classes must be created with the commands:
#
# lecturer = lecturer(fio, subject)
# reviewer = reviewer(fio, subject)
#
# where fio - full name (string); subject - subject (string).
# The initialization of these parameters (fio, subject) must be done by the Mentor base class.
#
# In the Lector and Reviewer classes themselves, you need to declare a method:
#
# def set_mark(self, student, mark): ...
#
# for marking a student (student). Moreover, in the Lector class, grades are added to the _lect_marks list
# of the Student class object, and in the Reviewer class, to the _house_marks list. Use the add_lect_marks()
# and add_house_marks() methods of the Student class for this.
#
# Also, the magic method must be overridden in the Lector and Reviewer classes:
#
# __str__()
#
# to generate the following information about objects:
#
# - for Lector class objects: Lecturer Full name: subject subject
# - for objects of the Reviewer class: Expert Full name: subject subject
#
# An example of using classes (you do not need to write these lines in the program):
#
# lecturer = Lector('Balakirev S.M.', 'Informatics')
# reviewer = Reviewer('Gates B.', 'Computer Science')
# students = [Student('Ivanov A.B.', 'EVMd-11'), Student('Gavrilov S.A.', 'EVMd-11')]
# persons = [lecturer, reviewer]
# lecturer.set_mark(students[0], 4)
# lecturer.set_mark(students[1], 2)
# reviewer.set_mark(students[0], 5)
# reviewer.set_mark(students[1], 3)
# for p in persons + students:
#     print(p)
# # in the console will be displayed:
# # Lecturer Balakirev S.M.: subject Informatics
# # Expert Gates B.: Computer Science subject
# # Student Ivanov A.B.: lecture grades: [4]; grades for d/z: [5]
# # Student Gavrilov SA: lecture grades: [2]; grades for d/z: [3]


class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # grades for lectures
        self._house_marks = []  # homework grades

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Student {self._fio}: " \
            f"grades for lectures: {str(self._lect_marks)}; " \
            f"homework grades: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f"Lecturer {self._fio}: {self._subject} subject"


class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f"Expert {self._fio}: {self._subject} subject"


lector = Lector("Balakirev S.M.", "Computer Science")
reviewer = Reviewer("Bill Gates", "Computer Science")
students = [Student("Ivanov A.B.", "EVMd-11"), Student("Gavrilov S.A.", "EVMd-11")]
persons = [lector, reviewer]
lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)
for p in persons + students:
    print(p)
# in the console will be displayed:
# Lecturer Balakirev S.M.: Computer Science subject
# Expert Bill Gates: Computer Science subject
# Student Ivanov A.B.: grades for lectures: [4]; homework grades: [5]
# Student Gavrilov S.A.: grades for lectures: [2]; homework grades: [3]
