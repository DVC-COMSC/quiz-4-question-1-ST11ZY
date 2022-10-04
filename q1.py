
# ******************************
# Make your Code
# ******************************
x=[]
y=10
i=0
counter=0
sum=0
z=0
while y>0:
    inp=input("Value?")
    num=int(inp)
    x.append(num)
    y=y-1
while z==0:
  if i==9:
    break
  if x[i]%2==0 and x[i+1]%2==0:
    counter=counter+1
    i= i+1
    z=z+1
  else:
    i=i+1
while z>0:
  sum=1
  while sum%2==1:
    i=i+1
    if i>7:
      break
    if x[i]%2==0:
      continue;
    if x[i]%2==1 and x[i+1]%2==1:
      continue;
    if x[i]%2==0 and x[i+1]%2==0 and x[i+2]%2==0:
      continue
    else:
      counter=counter+1
      continue
  if i>7:
    break    
print(counter)    


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
