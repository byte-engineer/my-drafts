;ESP --> the pionter
;EIP --> the instruction pionter
;pop --> cut the value that indicated by the pointer to a certain register
;push -> to push a value on the stack (the pointer will be point in it)
;call -> call functions it pushs the first instruction to the stack then it continue the other instruction
;ret --> it returns to main function also is pops next instruction into EIP 


;----------------------------------------------------------------------------------------------

section .date                        ;To define a constant variables.

;could be strings, numbers, termonating strings...

section .bss                         ;To reserve a space in memory to store data later

_start:                              ; from here the code start executing.
main:                                ; main function.

; nasm -f elf64 -g file.asm          ; it outputs file.o
; ld -m alf_x86_64 -o file file.o    ; use dynamic linker to compile the code.(it start executing from _start lable)
; gcc -o output input.s              ; use GCC to compile the code.

; nasm -f elf32 -g file.asm          ; for x32 architecture
; ld -m alf_i3x86 -o file file.o     ; for x32 architecture

; registers : Hardware emplemetation of variables.

int a = 1                            ; define an integer variable.
char[] b = [0, 0, 0]                 ; asign "000" to avariable as a list to create a string. 

;---------------------------------------------------------------------------------------------

; eax  ==> 32 bit register           ;
; rax  ==> 64 bit register           ;

; If we want to get data from memory we put the adderss of data on square brakets.
;                                    |> We can store data or addresses in registers.

;EAX  --> 32 bit  | EAH, EAL 8 bits  |> X prefix for whole register.
;EBX  --> 32 bit  | EBH, EBL 8 bits  |> H prefix for third quarter in the regester.
;ECX  --> 32 bit  | ECH, ECL 8 bits  |> L prefix for last quarter in the regester.
;EDX  --> 32 bit  | EDH, EDL 8 bits  |
;ESI  --> source index
;EDI  --> destination index
;ESP  --> stack pointer              |> It points in top of the stack.
;EBP  --> base pointer               |> It points in the base of the stack.
;                                    |> The stack is empty when ESP and EBP has a same address

;MOV-------------------------------------------------------------------------------------------------------

mov eax, ebx                        ;|> Copies the contents of register EBX to EAX;
mov [memory adderss], eax           ;|> general-purpose instruction used to move data from one location to another.

movzx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, zero-extending the value.
movzx edx, byte ptr [memory adderss];|> Copies the byte from the memory location specified by [source] to the 32-bit register EDX, zero-extending the value.

movsx eax, bx                       ;|> Copies the contents of the 16-bit register BX to the 32-bit register EAX, sign-extending the value 
movsx edx, byte ptr [memory adderss];|> Copies the byte from the memory location specified by [source] to the 32-bit register EDX, sign-extending the value
;                                   ;|> If source +ve we will extand by zeros ,Other wise we will extand with ones.

;EXAMPLE
mov   al , -5           ; AL  = -5                            (11111011) 
movsx eax, al           ; EAX = -5 (11111111 11111111 11111111 11111011) sign-extended to 32 bits.

;-------------------------------------------------------------------------------------------------------

