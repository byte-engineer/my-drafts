;------------------------------------------------------------------------------------------------
;|> This draft is for learning assembly x86 NASM syntax.
;|> We have to run the code on a Linux machine.
;|> If we want to run it on Windows, we can use the (WSL) feature which is built into the system.
;------------------------------------------------------------------------------------------------
;Commands to run the code:
;-> sudo apt-get install nasm                   |Download NASM
;-> nasm -f elf32 input.asm -o output.o         |convert file from .asm to .o
;-> ld -m elf_i386 output.o -o output           |convert the .o file to an executable using the linker
;-> nasm -f elf32 -g file.asm                   ;for x32 architecture.
;-> ld -m elf_i386 -o file file.o               ;for x32 architecture.
;-> ./output                                    |run the executable file
;------------------------------------------------------------------------------------------------

section .data                        ;To define constant variables

    var_name dd 10                   ;Declare and initialize a 32-bit integer variable

section .bss                         ;To reserve space in memory to store data later

section .text                        ;Executable code section
_start:                              ;From here the code starts executing

;---------------------------------------------------------------------------------------------

; registers : Hardware implementation of variables.
; eax  ==> 32-bit register
; rax  ==> 64-bit register

; If we want to get data from memory, we put the address of the data in square brackets.
; We can store data or addresses in registers.

;These are some registers:
;EAX  --> 32 bit  | EAH, EAL 8 bits  |> E prefix for whole register.
;EBX  --> 32 bit  | EBH, EBL 8 bits  |> H suffix for the higher 8 bits, L suffix for the lower 8 bits.
;ECX  --> 32 bit  | ECH, ECL 8 bits
;EDX  --> 32 bit  | EDH, EDL 8 bits
;ESI  --> source index
;EDI  --> destination index
;ESP  --> stack pointer              |> Points to the top of the stack.
;EBP  --> base pointer               |> Points to the base of the stack.
;                                    |> The stack is empty when ESP and EBP have the same address.

;MOV-------------------------------------------------------------------------------------------------------

mov eax, ebx                        ;|> Copies the contents of register EBX to EAX.
mov [memory_address], eax           ;|> Moves data from EAX to the memory location specified by memory_address.

movzx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, zero-extending the value.
movzx edx, byte ptr [memory_address];|> Copies the byte from the memory location specified by [memory_address] to the 32-bit register EDX, zero-extending the value.

movsx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, sign-extending the value.
movsx edx, byte ptr [memory_address];|> Copies the byte from the memory location specified by [memory_address] to the 32-bit register EDX, sign-extending the value.
;                                   ;|> If the source is positive, it will be extended by zeros; otherwise, it will be extended with ones.

;EXAMPLE
mov al, -5            ; AL = -5                              (11111011) 
movsx eax, al         ; EAX = -5   (11111111 11111111 11111111 11111011) sign-extended to 32 bits.

;LOGICAL OPERATIONS-----------------------------------------------------------------------------------------

;Also known as Bitwise operations.
;These operations include AND, OR, XOR, and NOT

; AND operation for each single bit
mov eax, 0x0F0F0F0F   ;                                                   |0x0F0F0F0F = 00001111 00001111 00001111 00001111
and eax, 0x33333333   ;        00001111 00001111 00001111 00001111 AND    |0x33333333 = 00110011 00110011 00110011 00110011
;                     ;        00110011 00110011 00110011 00110011
;The result stored in EAX   =  00000011 00000011 00000011 00000011

; OR operation for each single bit
mov eax, 0x0F0F0F0F   ;
or  eax, 0x33333333   ;        00001111 00001111 00001111 00001111 OR
;                     ;        00110011 00110011 00110011 00110011
;The result stored in EAX   =  00111111 00111111 00111111 00111111

; XOR operation for each single bit
mov eax, 0x0F0F0F0F   ;
xor eax, 0x33333333   ; EAX =  00001111 00001111 00001111 00001111 XOR
;                     ;        00110011 00110011 00110011 00110011
;The result stored in EAX   =  00111100 00111100 00111100 00111100

; NOT operation for each single bit
mov eax, 0x0F0F0F0F   ; EAX =  00001111 00001111 00001111 00001111
not eax               ; EAX =  11110000 11110000 11110000 11110000

; "test" performs an AND operation but does not store the result.
mov  eax, 0x0F0F0F0F  ;
test eax, 0x33333333  ; It just updates the flags.
;                     ;        00001111 00001111 00001111 00001111 AND
;                     ;        00110011 00110011 00110011 00110011
;                     ; Result:00000011 00000011 00000011 00000011
    
;|flag name           | function                                                       | value in this state for the result
;|ZF (zero flag)      | set to 1 if the result of the last update is zero              | set to 0
;|SF (sign flag)      | set to 1 if the result of the last update is negative          | set to 0      // number in decimal = 50,332,427
;|PF (parity flag)    | set to 1 if the result of the last update has even parity      | set to 0
;|CF (carry flag)     | set to 1 if the result in the last update caused a carry       | cleared to 0 in test command
;|OF (overflow flag)  | set to 1 if the number is too high or too low to be represented| cleared to 0 in test command
;|                    | in the bytes or space reserved for it.          // Example: 127 + 1 = -128 causes an overflow.
;-----------------------------------------------------------------------------------------------------------------------------------------

