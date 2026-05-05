"""
Filename: RegisterFile.py
Description: Register file for MIPS simulator.
Simulates the 32 general-purpose registers in MIPS.
Contributors: Vanny Bundick, Amul Poudel
"""

class RegisterFile:
    def __init__(self):
        self.registers = [0] * 32           # Initialize 32 registers to 0

    def read(self, reg_num: int) -> int:
        return self.registers[reg_num]
    
    def write(self, reg_num: int, value: int):
        # Writes a value to a register.
        if reg_num != 0:
            self.registers[reg_num] = value & 0xFFFFFFFF

    def dump(self):
        # Returns copy of register values.
        return self.registers.copy()
