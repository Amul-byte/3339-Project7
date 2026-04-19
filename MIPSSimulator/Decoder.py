"""
Decoder for MIPS assembly into Instruction objects.
"""

from .Instruction import Instruction, parse_register

class Decoder:
  def_init_(self, filepath: str):
    self.filepath = filepath
    self.instructions: list[Instruction] = []
    self.labels: dict[str, int] = {}

  def decode(self) -> list[Instruction]:
    lines = self._read_file() 

    # First Pass: Collect Labels
    pc = 0
    for line in lines:
      if ":" in line:
        label = line.split(".")[0].strip()
        self.labels[label] = pcline = line.split(":")[1].strip()
        if not line:
          continue
      pc += 1

    # Second Pass: Parse Instructions
    pc = 0
    for line in lines:
      if ":" in line:
        line = line.split(":")[1].strip()
        if not line:
          continue
      
      instr = self._parse_line(line, pc)
      self.instructions.append(instr.with_address(pc))
      pc += 1
    return self.instructions
  
  def _read_file(self):
    with open(self.filepath, "r") as f:
      lines = []
      for line in f:
        line = line.split("#")[0].strip()
        if line:
          lines.append(line)
      return lines
    
  def _parse_line(self, line: str, pc: int) -> Instruction:
    parts = line.replace(",", "").split()
    opcode = parts[0].upper()

    if opcode == "NOP":
      return Instruction(opcode="NOP, source=line")
    
    # R-type Instructions
    if opcode in {"ADD", "SUB", "MUL", "AND", "OR"}:
        rd = parse_register(parts[1])
        rs = parse_register(parts[2])  
        rt = parse_register(parts[3])  
        return Instruction(opcode, line, rs, rt, rd)

    if opcode in {"SLL", "SRL"}:
        rd = parse_register(parts[1]) 
        rt = parse_register(parts[2])
        shamt = int(parts[3])  
        return Instruction(opcode, line, 0, rt, rd, shamt=shamt)

    # I-type Instructions
    if opcode == "ADDI":
        rt = parse_register(parts[1])
        rs = parse_register(parts[2])
        imm = int(parts[3])
        return Instruction(opcode, line, rs, rt, immediate=imm)

    if opcode in {"LW", "SW"}:
      rt = parse_register(parts[1])
      offset, reg = parts[2].split("(")
      rs = parse_register(reg.replace(")", ""))
      imm = int(offset)
      return Instruction(opcode, line, rs, rt, immediate=imm)
    
    if opcode == "BEQ":
      rs = parse_register(parts[1])
      rt = parse_register(parts[2])
      label = parts[3]
      target = self.labels[label]
      return Instruction(opcode, line, rs, rt, target=target)
    
    # J-type Instructions
    if opcode == "J":
      label = parts[1]
      target = se;f.labels[label]
      return Instruction(opcode, line, target=target)
    
    raise ValueError(f"Unsupported instruction: {line}")
