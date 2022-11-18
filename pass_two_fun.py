from pass_one_fun import sym , instruction_map1 , instruction_map3 ,adr , start

hte   = open("HTE.txt","w")
pass1 = open("out_pass1.txt","r")
pass2 = open("out_pass2.txt","w")
st    = open("symbTable.txt","r")

line_1   = pass1.readline()
x        = line_1.split()
progName = x[1]
x.append("OBCODE") 
pass2.write(" ".join(x)+"\n")

progLength = hex(int(adr,16)-int(start,16))
progLength     = progLength.replace('0x','')
if len(progLength) < 6:
     for i in range(6-len(progLength)):
        progLength = "0"+progLength
bola = start
if len(bola) < 6:
     for i in range(6-len(bola)):
        bola = "0"+bola
hrecord    = "H, " + progName + ", " +bola+ ", " + progLength
hte.write(hrecord+"\n")

tstart = 0
tlimit = 0

for i in pass1.readlines():
    x = i.split()

    # if x[3] == "*":
    #     x[3] = "\t"
    # if x[1]== "-":
    #     x[1] = "\t\t"
    if x[2] == "RESW" or x[2] == "RESB":
        x.append("   -")
        pass2.write(" ".join(x)+"\n")
        continue
    elif x[2] in instruction_map1.keys():
        x.append(instruction_map1[x[2]])
        pass2.write(" ".join(x)+"\n")
        continue
    elif x[2] == "BYTE":
        if x[3][0] == 'X':
            hexa=""
            for i in (2,len(x[3])-2):
                hexa = hexa + x[3][i]
            if len(hexa) == 1:
                hexa = "0" + hexa
            x.append(hexa)
            pass2.write(" ".join(x)+"\n")
        elif x[3][0] == 'C':
            char = ""
            for i in range(2,len(x[3])-1):
                char = char + hex(ord(x[3][i]))
            char = char.replace('0x','')
            x.append(char)
            pass2.write(" ".join(x)+"\n")
    elif x[2] == "WORD":
        wordval = ""
        wordval = wordval + str(hex(int(x[3])))
        wordval = wordval.replace('0x','') 
        if len(wordval) < 6:
            for i in range(6-len(wordval)):
                wordval = "0"+wordval
            x.append(wordval)
            pass2.write(" ".join(x)+"\n")
    elif x[2] in instruction_map3.keys():
        if x[2] == "RSUB":
            opcode = instruction_map3[x[2]]+"0000"
            x.append(opcode)
            pass2.write(" ".join(x)+"\n")
        elif x[3] in sym.keys():
            char   = sym[x[3]]
            char   = char.replace('0x','')
            opcode = instruction_map3[x[2]] + char
            x.append(opcode)
            pass2.write(" ".join(x)+"\n")
        elif x[3][0] == "#":
            opcode = hex(int(instruction_map3[x[2]],16)+1)
            opcode = opcode.replace('0x','')
            if len(opcode) < 2:
                for i in range(2-len(opcode)):
                    opcode = "0"+opcode
            addr = x[3][1:]
            addr = hex(int(addr))
            addr = addr.replace('0x','')
            if len(addr) < 4:
                 for i in range(4-len(addr)):
                    addr = "0"+addr
            opcode = opcode + addr
            x.append(opcode)
            pass2.write(" ".join(x)+"\n")
        elif  x[3][len(x[3])-2] == ",":
            label   = x[3][0:(len(x[3])-2)]
            loc     = sym[label]
            loc     = loc.replace('0x','')
            sus     = str(8000)
            addr    = hex(int(sus,16)+int(loc,16))
            addr    = addr.replace('0x','')
            opcode  = instruction_map3[x[2]]
            objcode = opcode + addr
            x.append(objcode)
            pass2.write(" ".join(x)+"\n")

pass2.close()

pass2    = open("out_pass2.txt","r")
line_11  = pass2.readline()

tstart   = 0
tlimit   = 0
n        = 0
flag     = 1
flagos   = 0 
flagetos = 0
flagnos  = 0
kamba    = ""
zozo     = ""
flagtos  = 0
for i in pass2.readlines():
    x = i.split()
    n+=1
    zozo    =''
    flagtos = 0
    if flagetos == 1:
        tstart = int(x[0],16)
        flagetos = 0
    if start == x[0]:
        hte.write("T")
        tstart = int(start,16)
        hamody = str(hex(tstart)).replace('0x','')
        if len(hamody) < 6:
                for i in range(6-len(hamody)):
                    hamody = "0"+hamody
        hte.write(", " + hamody)

    if x[2] =="RESB" or x[2]=="RESW":
        tstart = int(x[0],16)
        mody   = str(hex(tlimit+3))
        if len(mody) < 4:
                for i in range(4-len(mody)):
                    mody = "0"+mody
        zozo = ", "+mody
        zozo = zozo.replace('0x','')
        zozo = zozo + kamba
        if len(zozo) >=6:
            hte.write(zozo)
        tlimit = 0
        flagos = 0
        flagetos = 1
        zozo = ''
        kamba= ''
        continue
    if tlimit >= 27:
        tstart = int(x[0],16)
        zozo = ", "+str(hex(tlimit+3))
        zozo = zozo.replace('0x','')
        zozo = zozo + kamba
        hte.write(zozo)
        zozo = ''
        kamba= ''
        tlimit = 0
        flagos = 0 
        flagtos = 1
    
    if tlimit < 27:
        if tlimit == 0  and n > 2 and flagos == 0 :
            hte.write("\nT")
            hamody = str(hex(tstart)).replace('0x','')
            if len(hamody) < 6:
                for i in range(6-len(hamody)):
                    hamody = "0"+hamody
            hte.write(", " + hamody)
            flagos = 1
            # print (x[0],x[4])
        mody = str(hex(tlimit+3))
        if len(mody) < 4:
                for i in range(4-len(mody)):
                    mody = "0"+mody
        zozo = ", "+mody
        zozo = zozo.replace('0x','')
        kamba += (str(", "+x[4]))
        tlimit = int(x[0],16) - tstart
if flagtos != 1:
    hte.write(zozo+kamba)

erecord    = "E, "+bola
hte.write("\n"+erecord+"\n")

hte.close()
pass1.close()
pass2.close()
st.close()