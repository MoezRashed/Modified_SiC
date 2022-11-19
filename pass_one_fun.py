#length of project name

intermediate = open ("intermediate.txt","r")
pass1 = open ("out_pass1.txt","w")
st = open ("symbTable.txt","w")
sym = {}
instruction_map3 = {
    "ADD":"18",
    "AND":"40",
    "COMP":"28",
    "DIV":"24",
    "J":"3C",
    "JEQ":"30",
    "JGT":"34",
    "JLT":"38",
    "JSUB":"48",
    "LDA":"00",
    "LDCH":"50",
    "LDL":"08",
    "LDX":"04",
    "MUL":"20",
    "OR":"44",
    "RD":"D8",
    "RSUB":"4C",
    "STA":"0C",
    "STCH":"54",
    "STL":"14",
    "STSW":"E8",
    "STX":"10",
    "SUB":"1C",
    "TD":"E0",
    "TIX":"2C",
    "WD":"DC"
    }
instruction_map1 ={
    "FIX": "C4",
    "FLOAT":"C0",
    "HIO":"F4",
    "NORM":"C8",
    "SIO": "F0",
    "TIO":"F8"
}
line_1 = intermediate.readline()
pass1.write("Addr ")
pass1.write("".join(line_1))
base = line_1.split()
start = base[2]
adr = base[2]
if len(base[0])> 6:
    print("Program name too big !!")
    exit()


for i in intermediate.readlines():
        
        x = i.split()
        if x[0] == "end" or x[0] == "END":
            break
        pass1.write(adr+" ")
        pass1.write("".join(i))     
        if x[0]!="-":
            st.write(x[0]+" "+adr+"\n")
            sym[x[0]] = adr
        if x[1] in instruction_map3.keys() or x[1]=="WORD":
            adr = str(hex(int(adr,16)+(3)))
        elif x[1] in instruction_map1.keys():
            adr = str(hex(int(adr,16)+1))
        elif x[1]=="RESW":
            temp = int(x[2],16)
            adr = str(hex(int(adr,16)+(temp)*3))
        elif x[1]=="RESB":
            adr = str(hex(int(adr,16)+int(x[2])))
        elif x[1]=="BYTE":
            if x[2][0]=="X":
                adr = str(hex(int(adr,16)+int((len(x[2])-3)/2)))
            elif x[2][0]=="C":
                adr = str(hex(int(adr,16)+(len(x[2])-3)))
        adr = adr.replace('0x','')
                
intermediate.close()
pass1.close()
st.close()