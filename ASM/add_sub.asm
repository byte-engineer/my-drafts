
section .data
    num1 dd 10          ; store 10 in memory and name it as "num1"
    num2 dd 20          ; store 20 in memory and name it as "num2"

section .bss
    Aresult dd 1        ; reserve four bytes in memory for storing the addition result.
    Sresult dd 1        ; reserve four bytes in memory for storing the subtraction result.

section .text
    global _start       ; Entry point for the program.

_start:

    mov eax, [num1]    ; load num1 into eax register.
    add eax, [num2]    ; perform addition.
    mov [Aresult], eax ; store the result in Aresult location in memory.

    mov eax, [num1]    ; load num1 into eax register.
    sub eax, [num2]    ; perform subtraction.
    mov [Sresult], eax ; store the result in Sresult location in memory.

    ; Exit the program
    mov eax, 1         ; syscall number for exit.
    xor ebx, ebx       ; return 0 status.
    int 0x80           ; make syscall.
