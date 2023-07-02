# Previously, you already created validation classes as a hierarchy of the Validator base class and child classes:
#
# StringValidator
# IntegerValidator
# FloatValidator
#
# for validation (checking) the correctness of the data. Let's repeat this functionality with some changes.
#
# So, first you need to declare the base class Validator, which should not have
# an initializer (the magic method __init__) and a method with the following signature is declared:
#
# def _is_valid(self, data): ...
#
# In theory, this method returns a boolean True if the data (data) is correct from the point of view of the validator,
# and False otherwise. But in the base Validator class, it must throw an exception with the command:
#
# raise NotImplementedError('class does not override _is_valid method')
#
# Next, you need to declare a child class FloatValidator to validate real numbers.
# Objects of this class are created by the command:
#
# float_validator = FloatValidator(min_value, max_value)
#
# where min_value is the minimum allowed value; max_value - the maximum allowed value.
#
# FloatValidator class objects are supposed to be used as follows:
#
# res = float_validator(value)
#
# where value is the value to be checked (must be real and be in the range [min_value; max_value]).
# This validator must return True if value passes validation and False otherwise.
#
# An example of using classes (you do not need to write these lines):
#
# float_validator = FloatValidator(0, 10.5)
# res_1 = float_validator(1) # False (integer, not real)
# res_2 = float_validator(1.0) # True
# res_3 = float_validator(-1.0) # False (out of range [0; 10.5])


class Validator:
    def _is_valid(self, data):
        raise NotImplementedError("the _is_valid method is not overridden in the class")


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float:
            return True if self.min_value <= data <= self.max_value else False
        else:
            return False

    def __call__(self, args):
        return self._is_valid(args)


float_validator = FloatValidator(0, 10.5)
print(float_validator(1))  # False (integer, not real)
print(float_validator(1.0))  # True
print(float_validator(-1.0))  # False (out of range [0; 10.5])
