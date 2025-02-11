;------------------------------------------------------------------------------------------------
;|> This draft is for learning assembly x86 NASM syntax.
;|> We have to run the code on a Linux machine.
;|> If we want to run it on Windows, we can use the (WSL) feature which is built into the system.
;------------------------------------------------------------------------------------------------
;Commands to run the code:
;--> sudo get-install nasm      | for first time
;--> sudo apt install binutils  | for first time
;--> sudo apt install gcc
;--> nasm -f elf32 in.asm -o out.o
;--> ld -m elf_i386 in.o -o out | the linker.
;--> gcc -m32 -o out in.o       | We can use GCC as alinker instead of "ld".
;------------------------------------------------------------------------------------------------

section .data                        ;To define constant variables

    var_name dd 10                   ;Declare and initialize a 32-bit integer variable

section .bss                         ;To reserve space in memory to store data later

test resb 1                          ; Reserve 1 byte for the test
subresult resb 1                     ; Reserve 1 byte for the subtraction result
addresult resb 1                     ; Reserve 1 byte for the addition result
imulresult resb 1                    ; Reserve 1 byte for the addition result

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
;
; AL, BL, CL, DL ---------------->   |8-bit, lowest bytes of the above.
;
;
;
;MOV-------------------------------------------------------------------------------------------------------

mov eax, ebx                        ;|> Copies the contents of register EBX to EAX.
mov [memory_address], eax           ;|> Moves data from EAX to the memory location specified by memory_address.

movzx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, zero-extending the value.
movzx edx, byte ptr [memory_address];|> Copies the byte from the memory location specified by [memory_address] to the 32-bit register EDX, zero-extending the value.

movsx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, sign-extending the value.
movsx edx, byte ptr [memory_address];|> Copies the byte from the memory location specified by [memory_address] to the 32-bit register EDX, sign-extending the value.
;                                   ;|> If the source is positive, it will be extended by zeros; otherwise, it will be extended with ones.
;- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
;EXAMPLES

mov [test], 10h                     ; Store 10 in the result variable.

mov al, -5                          ; AL = -5                              (11111011) 
movsx eax, al                       ; EAX = -5   (11111111 11111111 11111111 11111011) sign-extended to 32 bits.

;LOGICAL OPERATIONS-----------------------------------------------------------------------------------------

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
mov eax, 0x0F0F0F0F   ; EAX =  00001111 00001111 00001111 00001111 NOT
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

;MATH OPERATION---------------------------------------------------------------------------------------------

;|> Addition

mov al, [num1]        ; Load the value of num1 into AL.
add al, [num2]        ; Add the value of num2 to AL.              |AL= AL + num2
mov [addresult], al   ; Store the result in the result variable.

;|> Subtraction

mov al, [num1]        ; Load the value of num1 into AL.
sub al, [num2]        ; Add the value of num2 to AL.              |AL= AL - num2
mov [subresult], al   ; Store the result in the result variable.

;See example_for_add_sub.asm
- - - - - - - - - - - - - - - - - - - - - - 

;multiplication

mov  eax, [num1]      ; Load num1 into EAX register
mov  ebx, [num2]      ; Load num2 into EBX register
imul eax, ebx         ; Perform multiplication (EAX * EBX) ,if we don't write "eax" the result will be same.
mov [mulresult], eax  ; Store the result in the result variable

mov  ebx, [num2]      ; Load num1 into EBX register
mov  eax, [num1]      ; Load num1 into EAX register
imul ebx              ; Perform multiplication (EBX * EAX) result => EBX = EBX * EAX
mov [mulresult], eax  ; Store the result in the result variable

