# TestArithmetic.asm
#
# Tests all arithmetic and logical instructions in a hazard-free program.
# Initializes three values and applies ADD, SUB, MUL, AND, OR, and ADDI
# operations across them. No memory or branching is used.
#
# Expected register state:
#   $t0=12  $t1=10  $t2=3
#   $t3=22  $t4=2   $t5=36
#   $t6=8   $t7=14
#   $s0=27

        ADDI $t0, $zero, 12
        ADDI $t1, $zero, 10
        ADDI $t2, $zero, 3
        NOP
        NOP
        ADD  $t3, $t0, $t1
        SUB  $t4, $t0, $t1
        MUL  $t5, $t0, $t2
        AND  $t6, $t0, $t1
        OR   $t7, $t0, $t1
        ADDI $s0, $t3, 5
        NOP
