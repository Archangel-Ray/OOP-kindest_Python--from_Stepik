# Declare an exception class named StringException that is derived from the Exception base class.
# After that, declare two more exception classes:
#
# NegativeLengthString - error if length is negative;
# ExceedLengthString - error if length exceeds given value;
#
# inherited from the base class StringException.
#
# Then, in the try block (see the program), write the exception generation command
# to go to the ExceedLengthString exception handling block.


class StringException(Exception):
    """Line errors"""


class NegativeLengthString(StringException):
    """error if length is negative"""


class ExceedLengthString(StringException):
    """error if length exceeds given value"""


try:
    raise ExceedLengthString()
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
