"""
Entry point for the MIPS pipeline simulator.
Usage: python main.py <file.asm> [--hex] [--binary] [--debug]
"""

import argparse
from MIPSSimulator.Decoder import Decoder
from MIPSSimulator.Pipeline import Pipeline
from MIPSSimulator.Instruction import R_TYPE_FUNCTS, I_TYPE_OPCODES, J_TYPE_OPCODES


def _format_binary_fields(instr) -> str:
    b = instr.binary
    if instr.opcode in R_TYPE_FUNCTS or instr.opcode == "NOP":
        return (f"opcode={b[0:6]} | rs={b[6:11]} | rt={b[11:16]}"
                f" | rd={b[16:21]} | shamt={b[21:26]} | funct={b[26:32]}")
    if instr.opcode in I_TYPE_OPCODES:
        return f"opcode={b[0:6]} | rs={b[6:11]} | rt={b[11:16]} | imm={b[16:32]}"
    if instr.opcode in J_TYPE_OPCODES:
        return f"opcode={b[0:6]} | target={b[6:32]}"
    return b


def main():
    parser = argparse.ArgumentParser(description="MIPS Pipeline Simulator")
    parser.add_argument("file", help="Path to MIPS assembly file")
    parser.add_argument("--hex",    action="store_true", help="Print hex representation of the program before running")
    parser.add_argument("--binary", action="store_true", help="Print binary fields of the program before running")
    parser.add_argument("--debug",  action="store_true", help="Print pipeline state after each cycle")
    args = parser.parse_args()

    decoder = Decoder(args.file)
    instructions = decoder.decode()

    if args.hex:
        print("\n===== Hex Representation =====")
        for instr in instructions:
            hex_val = f"0x{int(instr.binary, 2):08x}"
            print(f"  {instr.address:02}: {hex_val}  [{instr.source}]")

    if args.binary:
        print("\n===== Binary Representation =====")
        for instr in instructions:
            print(f"  {instr.address:02}: [{instr.source}]")
            print(f"      {_format_binary_fields(instr)}")

    pipeline = Pipeline(instructions)
    pipeline.run(debug=args.debug)


if __name__ == "__main__":
    main()
