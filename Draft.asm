;------------------------------------------------------------------------------------------------
;|> This draft is for learn asembly x86 NASM sytax.
;|> We have to run the code in lunix machine.
;|> If we want to run it in windows we can use (WSL) feature which is built in the system.
;------------------------------------------------------------------------------------------------
;Commands to run the code:
;-sudo apt-get install nasm                   |Download NASM
;-nasm -f elf32 input.asm -o output.o         |convert file from .asm --> .o
;-ld -m elf_i386 input.o -o output            |convert converted file from .o --> .exe //this the linker.
; nasm -f elf32 -g file.asm                   ;for x32 architecture.
; ld -m alf_i3x86 -o file file.o              ;for x32 architecture.
;-./output                                    |run the .exe file
;------------------------------------------------------------------------------------------------


section .date                        ;To define a constant variables.

    var-name dd 10                   ;Declare and initialize a 32-bit integer variable

section .bss                         ;To reserve a space in memory to store data later

section .text                        ; executable code section.
_start:                              ; from here the code start executing.

main:                                ; main function.(not required)
 

;---------------------------------------------------------------------------------------------

; registers : Hardware emplemetation of variables.
; eax  ==> 32 bit register           ;
; rax  ==> 64 bit register           ;

; If we want to get data from memory we put the adderss of data on square brakets.
;                                    |> We can store data or addresses in registers.

;This are some regesters
;EAX  --> 32 bit  | EAH, EAL 8 bits  |> X prefix for whole register.
;EBX  --> 32 bit  | EBH, EBL 8 bits  |> H prefix for third quarter in the regester.
;ECX  --> 32 bit  | ECH, ECL 8 bits  |> L prefix for last quarter in the regester.
;EDX  --> 32 bit  | EDH, EDL 8 bits
;ESI  --> source index
;EDI  --> destination index
;ESP  --> stack pointer              |> It points in top of the stack.
;EBP  --> base pointer               |> It points in the base of the stack.
;                                    |> The stack is empty when ESP and EBP has a same address.

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

;LOGICAL OPERATIONS-----------------------------------------------------------------------------------------

;These operations include AND, OR, XOR, and NOT

;                     ; AND operation for each singel bit
mov eax, 0x0F0F0F0F   ;                                                   |0x0F0F0F0F = 00001111 00001111 00001111 00001111
and eax, 0x33333333   ;       00001111 00001111 00001111 00001111 AND     |0x33333333 = 00110011 00110011 00110011 00110011
;                     ;       00110011 00110011 00110011 00110011
;The result stored in EAX   = 00000011 00000011 00000011 00000011


;                     ; OR operation for each singel bit
mov eax, 0x0F0F0F0F   ;
or  eax, 0x33333333   ;       00001111 00001111 00001111 00001111 OR
;                     ;       00110011 00110011 00110011 00110011
;The result stored in EAX   = 00111111 00111111 00111111 00111111


mov eax, 0x0F0F0F0F   ; XOR operation for each singel bit
xor eax, 0x33333333   ; EAX = 00001111 00001111 00001111 00001111 XOR
;                     ;       00110011 00110011 00110011 00110011
;The result stored in EAX   = 00111100 00111100 00111100 00111100


mov eax, 0x0F0F0F0F   ; EAX = 00001111 00001111 00001111 00001111        |NOT operation for each singel bit
not eax               ; EAX = 11110000 11110000 11110000 11110000


mov  eax, 0x0F0F0F0F  ;
test eax, 0x33333333  ; Perform bitwise AND
;                     ;         00001111 00001111 00001111 00001111 AND
;                     ;         00110011 00110011 00110011 00110011
;                     ; Result: 00000011 00000011 00000011 00000011


;-----------------------------------------------------------------------------------------

