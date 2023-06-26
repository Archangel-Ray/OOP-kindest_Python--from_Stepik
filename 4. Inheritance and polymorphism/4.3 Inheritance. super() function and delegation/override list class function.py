# Declare a SoftList class that inherits from the standard list class. In the SoftList class, declare the necessary
# magic methods so that when a non-existent element (by index) is accessed, the False value
# (rather than an Out of Range exception) is returned. For example:
#
# sl = SoftList('python')
# sl[0] # 'p'
# sl[-1] # 'n'
# sl[6] # False
# sl[-7] # False


class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return False


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
