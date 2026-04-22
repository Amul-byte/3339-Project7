"""
Entry point for the MIPS pipeline simulator.
Usage: python main.py <file.asm> [--debug]
"""

import argparse
from MIPSSimulator.Decoder import Decoder
from MIPSSimulator.Pipeline import Pipeline


def main():
    parser = argparse.ArgumentParser(description="MIPS Pipeline Simulator")
    parser.add_argument("file", help="Path to MIPS assembly file")
    parser.add_argument("--debug", action="store_true", help="Print pipeline state after each cycle")
    args = parser.parse_args()

    decoder = Decoder(args.file)
    instructions = decoder.decode()

    pipeline = Pipeline(instructions)
    pipeline.run(debug=args.debug)


if __name__ == "__main__":
    main()
