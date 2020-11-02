import time
from timeit import timeit


def split(content): 
    
    fileR_array= [] 
    for line in content:
        stripped_line = line.strip()
        fileR_array.append(stripped_line)
    return logic(fileR_array)

def logic(array):
    aux=[]
    level=-1
    for line in array:
        if(line=="{"):
            level+=1
        elif(line=="},"):
            level-=1
        elif(line=="}"):
            break
        else:
            aux.append([level, line.replace(",","")])
    return aux

def addSpace(stringElement,level):
    string_length=len(stringElement)+level   # will be adding level extra spaces
    string_revised=stringElement.rjust(string_length)
    return string_revised

def construct(arrayWithLevels):
    outArrAux=[]
    for elem in arrayWithLevels:
        numLevel = elem[0]
        strElem = elem[1]
        outArrAux.append(addSpace(strElem,numLevel))
    return outArrAux

def parsing():
    with open('timetable.json', 'r') as rf:
        with open('timetableY.yaml', 'w') as wf:
            rf_content=rf.readlines()
            string_without_line_breaks = ""
            arrayBlock=[]
            outputArray=[]

            arrayBlock=split(rf_content)
            outputArray=construct(arrayBlock)
            for element in outputArray:
                element=element+'\n'
                wf.write(element)


start_time = time.time()
parsing()
print("%.6f" % (time.time() - start_time))


    
            
                
        
        