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
