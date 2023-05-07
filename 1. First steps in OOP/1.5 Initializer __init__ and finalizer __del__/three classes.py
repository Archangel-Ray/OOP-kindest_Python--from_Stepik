# Declare the following few classes in your program:
#
# CPU - class for describing processors;
# Memory - a class for describing memory;
# MotherBoard - a class for describing motherboards.
#
# Provide the ability to create objects of each class with the commands:
#
# cpu = CPU(name, clock speed)
# mem = Memory(name, size of memory)
# mb = MotherBoard(name, processor, memory1, memory2, ..., memoryN)
#
# Please note, when creating an object of the MotherBoard class, you can pass several objects of the Memory class,
# maximum N - according to the number of memory slots on the motherboard (N = 4).
#
# Class objects must have the following local properties:
#
# for CPU class: name - name; fr - clock frequency;
# for the Memory class: name - name; volume - the amount of memory;
# for the MotherBoard class: name - name; cpu - a reference to an object of the CPU class; total_mem_slots = 4 - total
# number of memory slots (the attribute is assigned with this value and does not change); mem_slots - a list of objects
# of the Memory class (maximum total_mem_slots = 4 pieces according to the maximum number of memory slots).
#
# The MotherBoard class must have a get_config(self) method to return the current configuration of the components on
# the motherboard as the following list of four lines:
#
# ['Motherboard: name ',
# 'CPU: name , clock speed ',
# 'Memory slots: total number of memory slots',
# 'Memory: name_1 - volume_1 ; name_2 - volume_2; ...; name_N - volume_N ']
#
# Create an object mb of class MotherBoard with one CPU (object of class CPU)
# and two memory slots (objects of class Memory).
#
# P.S. You do not need to display anything on the screen,
# only create an object according to the specified requirements.


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem[:]

    def get_config(self):
        return [f'Motherboard: {self.name}',
                f'CPU: {self.cpu.name}, {self.cpu.fr}',
                f'Memory slots: {self.total_mem_slots}',
                f'Memory: {"; ".join(map(lambda vol: f"{vol.name} - {vol.volume}", self.mem_slots))}']


my_cpu = CPU('AMD', 1230)
my_mem_1 = Memory('Samsung', 256)
my_mem_2 = Memory('Samsung', 512)

mb = MotherBoard('Asus', my_cpu, my_mem_1, my_mem_2)
print(mb.get_config())
