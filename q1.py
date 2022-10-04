
# ******************************
# Make your Code
# ******************************
list=[]
totalnums=10
i=0
counter=0
sum=0
firstcount=0
while totalnums>0:
    inp=input("Value?")
    num=int(inp)
    list.append(num)
    totalnums=totalnums-1
while firstcount==0:
  if i==9:
    break
  if list[i]%2==0 and list[i+1]%2==0:
    counter=counter+1
    i= i+1
    firstcount=firstcount+1
  else:
    i=i+1
while firstcount>0:
  sum=1
  while sum%2==1:
    i=i+1
    if i>7:
      break
    if list[i]%2==0:
      continue;
    if list[i]%2==1 and list[i+1]%2==0 and list[i+2]%2==0:
      counter=counter+1
      continue;
  if i>7:
    break    
print(counter)       


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
