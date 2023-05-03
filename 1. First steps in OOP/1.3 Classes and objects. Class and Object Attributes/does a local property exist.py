# Declare a class named Person and attributes:
#
# name: 'Sergey Balakirev'
# job: 'Programmer'
# city: 'Moscow'
#
# Create an instance p1 of this class and check if it has a local property named job.
# Print True if it is present in the p1 object and False if it is absent.


class Person:
    name = 'Sergey Balakirev'
    job = 'Programmer'
    city = 'Moscow'


p1 = Person()
print(True if 'job' in p1.__dict__ else False)
