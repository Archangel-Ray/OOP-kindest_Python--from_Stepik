# You need to create a program for the training course. Three classes are declared for this:
#
# Course - the class responsible for managing the course as a whole;
# Module - a class that describes one module (section) of the course;
# LessonItem - class of one lesson (lesson).
#
# The structure of the course at the level of these classes is shown in the figure below:
#
# Objects of the LessonItem class must be created with the command:
#
# lesson = LessonItem(lesson name, number of lessons, total lesson duration)
#
# Accordingly, local attributes must be created in each object of the LessonItem class:
#
# title - lesson title (string);
# practices - number of practical lessons (positive integer);
# duration - the total duration of the lesson (positive integer).
#
# It is necessary to implement the following logic of interaction with objects
# of the LessonItem class using magic methods:
#
# 1. Check the type of data assigned to local attributes. If the types do not meet the requirements,
# then throw an exception with the command:
#
# raise TypeError('Wrong type of data being assigned.')
#
# 2. When accessing non-existent attributes of objects of the LessonItem class, return the value False.
# 3. Prohibit deletion of the title, practices and duration attributes in objects of the LessonItem class.
#
# Objects of the Module class must be created with the command:
#
# module = Module(module name)
#
# Each Module object must contain local attributes:
#
# name - module name;
# lessons - a list of lessons (objects of the LessonItem class) included in the module (the list is empty initially).
#
# Also, the following methods must be implemented in the Module class:
#
# add_lesson(self, lesson) - adding a new lesson (an object of the LessonItem class)
# to the module (at the end of the lessons list);
# remove_lesson(self, indx) - remove lesson by index in lessons list.
#
# Finally, objects of the Course class are created with the command:
#
# course = Course(course name)
#
# And contain the following local attributes:
#
# name - course name (string);
# modules - list of modules in the course (initially the list is empty).
#
# The following methods must also be present in the Course class:
#
# add_module(self, module) - add a new module at the end of the modules list;
# remove_module(self, indx) - remove a module from the modules list by index in this list.
#
# An example of using classes (do not write these lines in the program):
#
# course = Course('Python OOP')
# module_1 = Module('Part one')
# module_1.add_lesson(LessonItem('Lesson 1', 7, 1000))
# module_1.add_lesson(LessonItem('Lesson 2', 10, 1200))
# module_1.add_lesson(LessonItem('Lesson 3', 5, 800))
# course.add_module(module_1)
# module_2 = Module('Part two')
# module_2.add_lesson(LessonItem('Lesson 1', 7, 1000))
# module_2.add_lesson(LessonItem('Lesson 2', 10, 1200))
# course.add_module(module_2)


class LessonItem:
    type_dictionary = {"title": str, "practices": int, "duration": int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.type_dictionary:
            if type(value) != self.type_dictionary[key]:
                raise TypeError("Wrong type of data being assigned.")
            if (key == "practices" or key == "duration") and value <= 0:
                raise TypeError("Wrong type of data being assigned.")

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.type_dictionary:
            raise AttributeError()

        super().__delattr__(item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


course = Course("Python OOP")
module_1 = Module("Part one")
module_1.add_lesson(LessonItem("Lesson 1", 7, 1000))
module_1.add_lesson(LessonItem("Lesson 2", 10, 1200))
module_1.add_lesson(LessonItem("Lesson 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Part two")
module_2.add_lesson(LessonItem("Lesson 1", 7, 1000))
module_2.add_lesson(LessonItem("Lesson 2", 10, 1200))
course.add_module(module_2)
print("Course:", course.name, "\n")
for x in course.modules:
    print("\n", "Course topic:", x.name, "\n")
    for j in x.lessons:
        print(f"Lesson: {j.title} - {j.practices} of practical sessions and lesson duration {j.duration} min")
