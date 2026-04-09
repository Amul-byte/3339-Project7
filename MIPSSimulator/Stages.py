'''
MIPSSimulator/Stages.py
Defines the 5 pipeline stages as methods of Pipeline class in Pipeline
Contributors: Samantha Hanna
'''

class IF_ID_Latch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instruction = NOP
        self.pc = 0
    

class ID_EX_Latch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instruction = NOP
        self.pc = 0
        self.rs_value = 0
        self.rt_value = 0
        self.control_signals = ControlSignals()

class EX_MEM_Latch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instruction = NOP
        self.pc = 0
        self.alu_result = 0
        self.rt_value = 0
        self.control_signals = ControlSignals()

class MEM_WB_Latch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instruction = NOP
        self.pc = 0
        self.alu_result = 0
        self.mem_data = 0
        self.control_signals = ControlSignals()