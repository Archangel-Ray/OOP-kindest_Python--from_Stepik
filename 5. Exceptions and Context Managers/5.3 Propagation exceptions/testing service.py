# You start developing your testing service. To do this, you are instructed to develop a base class Test for all kinds
# of tests, the objects of which are created by the command:
#
# test = test(descr)
#
# where descr is the wording of the test (string).
# If the length of the string descr is less than 10 or more than 10,000 characters,
# then throw an exception with the command:
#
# raise ValueError('test wording must be between 10 and 10,000 characters')
#
# An abstract method must be declared in the Test class itself:
#
# def run(self): ...
#
# which must be overridden in the child class.
# If this is not the case, then an exception should be thrown with the command:
#
# raise NotImplementedError
#
# Next, declare a child class named TestAnsDigit to test the correct numerical answer entered for the test question.
# Objects of the TestAnsDigit class must be created with the command:
#
# test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
#
# where ans_digit is the correct numerical answer to the test; max_error_digit - maximum error in specifying
# a numeric answer (required to check the correctness of real numbers, default value is 0.01).
#
# If the argument ans_digit or max_error_digit is not a number (also check that max_error_digit is greater
# than or equal to zero), then throw an exception with the command:
#
# raise ValueError('invalid test argument values')
#
# In the TestAnsDigit class, override the method:
#
# def run(self): ...
#
# which should read a line from the input stream (user response) with the command:
#
# ans = float(input()) # just such a command, write it in the run() method
#
# and return boolean True if the input numeric answer ans is in the range
# [ans_digit-max_error_digit; ans_digit+max_error_digit]. Otherwise, the boolean value False is returned.
#
# Now we need to use the TestAnsDigit class. To do this,
# the test itself is first read in the program using the commands:
#
# descr, ans = map(str.strip, input().split('|')) # ex: What is the value of 2+2? | 4
# ans = float(ans) # here, for simplicity, we assume that ans is exactly a number and there can be no errors
#                    in the conversion
#
# Next, you need to create an object of the TestAnsDigit class with the descr, ans arguments, and the max_error_digit
# argument should take a default value of 0.01.
#
# Run the test with the run() command and display the result of its work (True or False value).
# If exceptions occur during the creation of an object of the TestAnsDigit class or during the operation
# of the run() method, they must be processed and the message contained in the exception is displayed on the screen.


class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError("the wording of the test should be between 10 and 10,000 characters")

        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError("invalid test argument values")

        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)
try:
    test = TestAnsDigit(descr, ans)
    res = test.run()
    print(res)
except ValueError as e:
    print(e)
