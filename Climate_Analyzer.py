import csv
file1='Data.csv'
sunday=0
rain=0

with open(file1,'r') as Data1:
 input1=csv.reader(Data1)
 
 for RoW in input1:
      
  if(RoW[1]=="Sunday"):
   sunday=sunday+1
   if(RoW[1]=="Sunday" and RoW[2]=="Rain"):
    rain=rain+1
print("Chance to rain on sundays in the month of January :",rain/sunday)       
      
      
      
