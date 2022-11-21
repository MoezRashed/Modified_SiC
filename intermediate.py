#,x without space
#lines without labels have to start with a -
#lines without addresses add * to the end
# AT end put . instead of end

raw = open("input.txt","r")
intermediate = open ("intermediate.txt","w")

for line in raw.readlines():
    
    x = line.split()
    if x.__len__() == 0:
        continue 
    if(x[1] =="."):
        continue
    if(x[1] =="END" or x[1] == "end"):
        break
    intermediate.write(x[1]+" "+x[2]+" "+x[3]+"\n")
intermediate.write("END")
raw.close()
intermediate.close()

    