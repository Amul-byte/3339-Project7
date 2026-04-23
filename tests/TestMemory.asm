# TestMemory.asm
#
# Tests memory and control flow instructions in a hazard-free program.
# Shifts two values, stores both to memory, loads them back, then uses
# BEQ (taken) to skip over J and exit.
#
# Expected register state:
#   $t0=4   $t1=8   $t2=3   $t3=3
#   $s0=16  $s1=4
#   $t4=16  $t5=4
#
# Expected memory state:
#   mem[0] = 16
#   mem[4] = 4

        ADDI $t0, $zero, 4
        ADDI $t1, $zero, 8
        ADDI $t2, $zero, 3
        ADDI $t3, $zero, 3
        NOP
        SLL  $s0, $t0, 2
        SRL  $s1, $t1, 1
        NOP
        NOP
        NOP
        SW   $s0, 0($zero)
        SW   $s1, 4($zero)
        LW   $t4, 0($zero)
        LW   $t5, 4($zero)
        BEQ  $t2, $t3, skip
        NOP
        NOP
        NOP
        J    end
        NOP
        NOP
        NOP
skip:
        NOP
end:
        NOP
