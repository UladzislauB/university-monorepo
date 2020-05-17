# Both Lab 4 and Lab 5 implemented as one

.model tiny
.code
.486
.stack 256
org 100h

start:
JMP initialization


новый обработчик прерывания клавиатуры
newINT9Handle proc
PUSHF
PUSH ES

MOV  AX, 40H
для работы с буфером клавиатуры
MOV  ES, AX

XOR AX, AX
IN  AL, 60H
получаем скан-код клавиши

CMP AL, 1Eh
Сравниваем код с кодом буквы a
JNE b
MOV AL, 7Ah
z
JMP newHandler
b:
    CMP AL, 12h
    Сравниваем код с кодом буквы e
    JNE c
    MOV AL, 64h
    JMP newHandler
    c:
    CMP AL, 17h
    Сравниваем код с кодом буквы i
    JNE d
    MOV AL, 68h
    JMP newHandler
    d:
    CMP AL, 18h
    Сравниваем код с кодом буквы o
    JNE e
    MOV AL, 6Eh
    JMP newHandler
    e:
    CMP AL, 15h
    Сравниваем код с кодом буквы y
    JNE old
    MOV AL, 78h

    jmp newHandler

    u:

        CMP AL, 16h
        Сравниваем код с кодом буквы u

    JNE old

    MOV AL, 74h

    newHandler:
        MOV  BX, 1AH
        MOV  CX, ES: [BX]
        голова буфера
        MOV  DI, ES: [BX]+2
        хвост буфера
        CMP  CX, 60
        голова на вершине?
        JE   CHECK
        INC  CX
        увеличиваем указатель головы на 2
        INC  CX
        CMP  CX, DI
        сравниваем с указателем хвоста
        JE   EXIT
        если равны, то буфер полон
        JMP  INSERT
        иначе вставляем символ
        CHECK:
            CMP  DI, 30
            JE   EXIT
            если буфер полон, то выход
        INSERT:
            MOV  ES: [DI], AL
            помещаем символ в хвост
            CMP  DI, 60
            JNE  NOWRAP
            если хвост не в конце буфера, то добавляем 2
            MOV  DI, 28
            иначе указатель хвоста = 28+2
        NOWRAP:
            ADD  DI, 2
            MOV  ES: [BX]+2, DI
            посылаем его в область данных
        JMP EXIT

    old:
        POP ES
        POPF
        JMP DWORD PTR cs: oldHandler
        вызов стандартного обработчика прерывания
        IRET
    exit:
        XOR AX, AX
        MOV AL, 20h
        OUT 20h, al
        POP ES
        POPF
        IRET
newINT9Handle ENDP

oldHandler dd ?

initialization PROC

копируем адрес предыдущего обработчика в oldHandler
MOV AX, 3509h
INT 21h
MOV WORD PTR oldHandler, BX
MOV WORD PTR oldHandler + 2, ES

устанавливаем новый обработчик
MOV AX, 2509h
MOV DX, offset newINT9Handle
INT 21H

делаем программу резидентной
MOV DX, offset initialization
INT 27H
initialization ENDP
end start
