from dis import Instruction
import re
from tkinter import W

def checkr(l):
    rfile=open("r.txt","r")
    lines=rfile.readlines()
    rfile.close()

    k=0
    first=""
    for w in l.split():
        if k==0:
            first=w
        k+=1

    for line in lines:
        for word in line.split():
            if re.fullmatch(word,first):
                return True
    return False

def checki(l):
    ifile=open("i.txt","r")
    lines=ifile.readlines()
    ifile.close()

    k=0
    first=""
    for w in l.split():
        if k==0:
            first=w
        k+=1

    for line in lines:
        for word in line.split():
            if re.match(word,first):
                return True
    return False

def i(l):
    number = ""
    instruction = ""
    order = ""
    #open i file and read lines
    file = open("i.txt","r")
    lines = file.readlines()
    file.close()

    k=0
    first=""
    for w in l.split():
        if k==0:
            first=w
        k+=1

    for line in lines:
        for word in line.split():
            if re.fullmatch(word,first):
                #use split line from prog text to get instruction
                for word in l.split():
                    if re.match(word,line):
                        number += getFunction(word)
                    else:
                        instruction += word
                #get order of instruction from i file
                i = 0
                for word in line.split():
                    if i==1:
                        order += word
                    i+=1
                break
                
    #call function to get instruction binary
    getI(number,instruction,order)

def getI(number,instruction,order):
    fullLine = number #i op code is number
    first = ""
    second = ""
    third = ""
    label = ""

    if not re.search("\(",instruction):
        w = order.split(",")[0]
        if w == "rs":
            first = instruction.split(",")[0]
        elif w == "rt":
            second = instruction.split(",")[0]
        elif w == "imm":
            third = instruction.split(",")[0]
        elif w == "label":
            label = instruction.split(",")[0]

        w = order.split(",")[1]
        if w == "rs":
            first = instruction.split(",")[1]
        elif w == "rt":
            second = instruction.split(",")[1]
        elif w == "imm":
            third = instruction.split(",")[1]
        elif w == "label":
            label = instruction.split(",")[1]
        
        w = order.split(",")[2]
        if w == "rs":
            first = instruction.split(",")[2]
        elif w == "rt":
            second = instruction.split(",")[2]
        elif w == "imm":
            third = instruction.split(",")[2]
        elif w == "label":
            label = instruction.split(",")[2]
    else:
        w = order.split(",")[0]
        if w == "rs":
            first = instruction.split(",")[0]
        elif w == "rt":
            second = instruction.split(",")[0]
        elif w == "imm":
            third = instruction.split(",")[0]
        elif w == "label":
            label = instruction.split(",")[0]

        instruction = instruction[len(second)+1:]
        for letter in instruction:
            if letter == "(":
                break
            else:
                third += letter
        instruction = instruction[len(third)+1:]
        for letter in instruction:
            if letter == ")":
                break
            else:
                first += letter

    fullLine+=getBinary(first)
    fullLine+=getBinary(second)
    if third != "":
        if abs(int(third)) > 65536: #if imm is too big for 16 bits
            print("invalid input")
            return
    if label != "":
        if abs(int(label)) > 65536: #if label is too big for 16 bits
            print("invalid input")
            return

    if label == "":
        if int(third)>=0:
            fullLine+=toBi(int(third))
        else:
            fullLine+=twoComp(toBi(abs(int(third)))) #absolute value of negative number to get 2's complement from binary
    else:
        new = int(label)//4
        if new>=0:
            fullLine+=toBi(new)
        else:
            fullLine+=twoComp(toBi(abs(new))) #absolute value of negative number to get 2's complement from binary

    #print binary conversion from first instruction
    print(fullLine)

def twoComp(input):
    length = len(input)
 
    i = length - 1

    #find first 1
    while(i >= 0):
        if (input[i] == '1'):
            break
        i -= 1
    
    #if all 0s
    if (i == -1):
        return '1'+input
 
    o = i - 1
    while(o >= 0):
         
        if (input[o] == '1'):
            input = list(input)
            input[o] = '0'
            input = ''.join(input)
        else:
            input = list(input)
            input[o] = '1'
            input = ''.join(input)
 
        o -= 1
    return input

def toBi(n):
    binary = bin(n).replace("0b", "")
    while len(binary) < 16:
        binary = "0" + binary
    return binary

def r(l):
    number = ""
    instruction = ""
    order = ""
    #open r file and read lines
    file = open("r.txt","r")
    lines = file.readlines()
    file.close()

    k=0
    first=""
    for w in l.split():
        if k==0:
            first=w
        k+=1

    for line in lines:
        for word in line.split():
            if re.fullmatch(word,first):
                #use split line from prog text to get instruction
                for word in l.split():
                    if re.match(word,line):
                        number += getFunction(word)
                    else:
                        instruction += word
                #get order of instruction from r file
                i = 0
                for word in line.split():
                    if i==1:
                        order += word
                    i+=1
                break
                
    #call function to get instruction binary
    getR(number,instruction,order)
                    

def getR(number,instruction,order):
    fullLine = "000000" #r op code is 000000
    shamt = "00000" #shamt is 00000
    first = ""
    second = ""
    third = ""

    w = order.split(",")[0]
    if w == "rs":
        first = instruction.split(",")[0]
    elif w == "rt":
        second = instruction.split(",")[0]
    elif w == "rd":
        third = instruction.split(",")[0]

    w = order.split(",")[1]
    if w == "rs":
        first = instruction.split(",")[1]
    elif w == "rt":
        second = instruction.split(",")[1]
    elif w == "rd":
        third = instruction.split(",")[1]
    
    w = order.split(",")[2]
    if w == "rs":
        first = instruction.split(",")[2]
    elif w == "rt":
        second = instruction.split(",")[2]
    elif w == "rd":
        third = instruction.split(",")[2]

    fullLine+=getBinary(first)
    fullLine+=getBinary(second)
    fullLine+=getBinary(third)
    fullLine+=shamt
    fullLine+=number

    #print binary conversion from first instruction
    print(fullLine)
    
        
def getBinary(input):
    if input == "$zero":
        return "00000"
    elif input == "$at":
        return "00001"
    elif input == "$v0":
        return "00010"
    elif input == "$v1":
        return "00011"
    elif input == "$a0":
        return "00100"
    elif input == "$a1":
        return "00101"
    elif input == "$a2":
        return "00110"
    elif input == "$a3":
        return "00111"
    elif input == "$t0":
        return "01000"
    elif input == "$t1":
        return "01001"
    elif input == "$t2":
        return "01010"
    elif input == "$t3":
        return "01011"
    elif input == "$t4":
        return "01100"
    elif input == "$t5":
        return "01101"
    elif input == "$t6":
        return "01110"
    elif input == "$t7":
        return "01111"
    elif input == "$s0":
        return "10000"
    elif input == "$s1":
        return "10001"
    elif input == "$s2":
        return "10010"
    elif input == "$s3":
        return "10011"
    elif input == "$s4":
        return "10100"
    elif input == "$s5":
        return "10101"
    elif input == "$s6":
        return "10110"
    elif input == "$s7":
        return "10111"
    elif input == "$t8":
        return "11000"
    elif input == "$t9":
        return "11001"
    elif input == "$k0":
        return "11010"
    elif input == "$k1":
        return "11011"
    elif input == "$gp":
        return "11100"
    elif input == "$sp":
        return "11101"
    elif input == "$fp":
        return "11110"
    elif input == "$ra":
        return "11111"
    elif re.search(r"[0-9]+",input):
        input = re.sub('[$]','',input)
        return toBinary(int(input))
    else:
        print("invalid register")

def toBinary(n):
    binary = bin(n).replace("0b", "")
    i=0
    for number in binary:
        if i > 5:
            binary = binary[1:]
        i+=1
    if i<5:
        for i in range(5-i):
            binary = "0"+binary
    return binary
    
def getFunction(word):
    if word == "add":
        return "100000"
    elif word == "sub":
        return "100010"
    elif word == "j":
        return "000010"
    elif word == "addi":
        return "001000"
    elif word == "sll":
        return "000000"
    elif word == "srl":
        return "000010"
    elif word == "lw":
        return "100011"
    elif word == "sw":
        return "101011"
    elif word == "beq":
        return "000100"
    elif word == "bne":
        return "000101"
    else:
        print("invalid instruction")


def main():
    print("Prog1")
    file1=open("Prog1.txt","r")
    lines=file1.readlines()
    file1.close()
    for line in lines:
        if not checkr(line):
            if not checki(line):
                print("invalid input")
                break
            else:
                i(line)
        else:
            r(line)
    
    print("Prog2")
    file2=open("Prog2.txt","r")
    lines=file2.readlines()
    file2.close()
    for line in lines:
        if not checkr(line):
            if not checki(line):
                print("invalid input")
                break
            else:
                i(line)
        else:
            r(line)

    print("Prog3")
    file3=open("Prog3.txt","r")
    lines=file3.readlines()
    file3.close()
    for line in lines:
        if not checkr(line):
            if not checki(line):
                print("invalid input")
                break
            else:
                i(line)
        else:
            r(line)


if __name__ == "__main__":
    main()