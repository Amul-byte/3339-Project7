        ADDI $t0, $zero, 8
        ADDI $t1, $zero, 3
        ADDI $t2, $zero, 4
        ADDI $s0, $zero, 0
        ADDI $t8, $zero, 0
        ADD  $t3, $t0, $t1
        SUB  $t4, $t0, $t1
        MUL  $t5, $t0, $t1
        AND  $t6, $t0, $t1
        OR   $t7, $t0, $t1
        SLL  $s1, $t1, 1
        SRL  $s2, $t0, 1
        SW   $t3, 0($s0)
        LW   $s3, 0($s0)
        ADD  $s4, $t3, $t4
        BEQ  $s2, $t2, match
        # branch resolves in MEM stage, 3 NOPs fill pipeline delay slots
        NOP
        NOP
        NOP
        J    done
        NOP
        NOP
        NOP
match:
        SW   $s4, 4($s0)        # mem[4] = sum+diff = 16
        SLL  $s5, $s4, 1        # (sum+diff) << 1 = 32
        SRL  $s6, $s4, 1        # (sum+diff) >> 1 = 8
        LW   $s7, 4($s0)        # $s7 = mem[4] = 16 (verify store)
done:
        ADD  $t9, $t3, $t5      # final result: sum + product = 11 + 24 = 35


# Description:
# Exercises all 13 MIPS opcodes with label targets
# Given a=8, b=3: computes arithmetic and logical results, stores
# the sum to memory, then branches on whether (a >> 1) equals the
# expected value (4 == 4, always taken)
#
# match: stores sum+diff, computes left/right shifts of it, reloads
#        the stored value to verify the store
# done:  computes a final result combining the sum and product
#
# Expected registers after execution:
#   $t0=8   $t1=3   $t2=4   $t3=11  $t4=5   $t5=24
#   $t6=0   $t7=11  $t8=0   $t9=35
#   $s0=0   $s1=6   $s2=4   $s3=11
#   $s4=16  $s5=32  $s6=8   $s7=16
#
# Expected memory: mem[0]=11, mem[4]=16