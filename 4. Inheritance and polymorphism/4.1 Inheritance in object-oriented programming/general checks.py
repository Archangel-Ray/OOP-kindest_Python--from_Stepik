# You need to create many classes to validate (check) the correctness of the data.
# To do this, your immediate supervisor (Senior) suggests that you declare a base class in the program with the name:
#
# Validator
#
# providing basic functionality for checking the correctness of data. In particular,
# the following method must be declared in this class:
#
# def _is_valid(self, data): ...
#
# By design, this method should return a boolean True if the data (data) is correct and False otherwise.
#
# Since the Validator base class is a generic class for all kinds of validation,
# the _is_valid() method will simply return True.
# In addition, objects of the Validator class:
#
# v = Validator() # no need to write an initializer in the Validator class
#
# should be called like functions:
#
# v(data)
#
# and if the data (data) is incorrect, then throw an exception:
#
# raise ValueError('data not validated')
#
# Validation is performed using the _is_valid() method. After that, the program needs to declare two child classes:
#
# IntegerValidator - to check that data is an integer in the given range;
# FloatValidator - to check that data is a real number in the given range.
#
# Objects of these classes are supposed to be created by the commands:
#
# integer_validator = IntegerValidator(min_value, max_value)
# float_validator = IntegerValidator(min_value, max_value)
#
# where min_value, max_value - valid range of numbers [min_value; max_value]
#
# Also in these classes you need to override the method:
#
# def _is_valid(self, data): ...
#
# which would return True if data is a number of the correct type (either int or float depending on the validator)
# and is in the given range [min_value; max_value]. Otherwise, False is returned.
#
# An example of using classes (you do not need to write these lines in the program):
#
# integer_validator = IntegerValidator(-10, 10)
# float_validator = FloatValidator(-1, 1)
# res1 = integer_validator(10) # no exception thrown (validation passes)
# res2 = float_validator(10) # ValueError exception


class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if self._is_valid(args[0]):
            return args[0]
        else:
            raise ValueError("data has not been validated")


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == int and self.min_value <= data <= self.max_value:
                return True
        else:
            return False


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float:
            if self.min_value <= data <= self.max_value:
                return True
        else:
            return False


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)
# res2 = integer_validator(1.2)
# res3 = float_validator(1)
res4 = float_validator(0.5)
print(res1, res4)
