.model small
.stack 1000
.data
        old dd 0 
		vOldInt LABEL   WORD
.code
.486
        flag dw 0
		
check MACRO schar, char
	cmp  al, schar
	mov dl, char
	je new_handler
ENDM
		
new_handle proc    
; jmp starrt
		; bitmap  db 30,97,  48,98,  46,99,  32,100,  18,101,  33,102
				; db 34,103,  35,104,  23,105,  37,106
				; db 38,107,  50,108,  49,109,  24,110
				; db 25,111,  16,112,  19,113,  31,114
				; db 20,115,  22,116,  30,117,  47,118
				; db 17,119,  45,120,  21,121,  44,122
; starrt:			
        push ds si es di dx cx bx ax 
        
		xor ax, ax 
        in  al, 60h        ;Получаем скан-код символа
		
		cmp al, 2Ah
        je ti
        cmp al, 0AAh
        je to
		
		check 30, 97	;a
		check 48, 98	;b
		check 46, 99	;c
		check 32, 100	;d
		check 18, 101	;e
		check 33, 102	;f
		check 34, 103	;g
		check 35, 104	;h
		check 23, 105	;i
		check 36, 106	;j
		check 37, 107	;k
		check 38, 108	;l
		check 50, 109	;m
		check 49, 110	;n
		check 24, 111	;o
		check 25, 112	;p
		check 16, 113	;q
		check 19, 114	;r
		check 31, 115	;s
		check 20, 116	;t
		check 22, 117	;u
		check 47, 118	;v
		check 17, 119	;w
		check 45, 120	;x
		check 21, 121	;y
		check 44, 122	;z
		JMP old_handler

		ti:


                ;mov ah, 02h 
                ;MOV dl,'-'
                ;int 21h
                mov flag, 1
                ;je exit
                jmp old_handler

        to:

               ; mov ah, 02h 
               ; MOV dl,'+'
               ; int 21h
                mov flag, 0
               ;je exit  
                jmp old_handler
		
		
		
        new_handler: 

                ;inc count ;инкремент счетчика с каждой гласной буквой

               cmp flag, 1
               je lb

               sub dl, 32

               lb:
				
                  mov ah, 02h 
                  int 21h
       
                mov BX, 1
                xor DX, DX
                div BX
                cmp DX, 0

    
                 mov al, 20h
                 out 20h, al
                je exit
        
        old_handler: 
                pop ax bx cx dx di es si ds                       
                jmp dword ptr cs:old        ;вызов стандартного обработчика прерывания
                xor ax, ax
                mov al, 20h
                out 20h, al 
                jmp exit
                
        exit:
                xor ax, ax
                mov al, 20h
                out 20h, al 
                pop ax bx cx dx di es si ds ;восстановление регистров перед выходом из нашего обработчика прерываний
        iret
new_handle endp
 
 
new_end:
 
start:
        mov ax, @data
        mov ds, ax
        
        cli ;сброс флага IF
        pushf 
        push 0        ;перебрасываем значение 0 в DS
        pop ds
        mov eax, ds:[09h*4] 
        mov cs:[old], eax ;сохранение системного обработчика

        mov ax, cs
        shl eax, 16
        mov ax, offset new_handle
        mov ds:[09h*4], eax ;запись нового обработчика
        sti ;Установка флага IF
        
        xor ax, ax
        mov ah, 31h
        MOV DX, (New_end - @code + 10FH) / 16 ;вычисление размера резидентной части в параграфах(16 байт)
        INT 21H 



end start