#THIS IS A Python 3.6.1 PROGRAM; IT SHOULD BE EXECTUABLE IN THE LINUX TERIMNAL DIRECTLY IF THE INTEPRETER IS INSTALLED


#VARIOUS FUNCTIONS AND VARIABLES NEEDED

operators=["-","+","%","/","*"]#["*","/","%","+","-"]
brackets=["(",")"]
digits=["0","1","2","3","4","5","6","7","8","9","."]
leftbracket=["("]
rightbracket=[")"]


#return true if expression stored in string is well formed
def wff(expr):
  stk=[]
  for e in expr:
    #print(e,stk)
    if e in leftbracket:
      stk=[e]+stk
    elif e in rightbracket and len(stk)!=0:
      del stk[0]
    elif e in rightbracket and len(stk)==0:
      print("Expression is not well formed, check your paranthesis\n")
      return False  
    
  if len(stk)==0:
    return True
  else:
    print("Expression is not well formed, check your paranthesis\n")
    return False

#print(wff(")5*(6+2)-12/4"))
#print(wff("(1+1)*13+10/2"))



#return an array with sieved operators and numbers
def getArrayFromInput(string):
  array=list(string)
  l=0
  while l<len(array):
    #print(array[i])
    if array[l] not in brackets+operators:
      while l+1<len(array) and array[l+1] not in brackets+operators:
        array[l]=array[l]+array[l+1]
        del array[l+1]
    l+=1
  return array

#print(getArrayFromInput(mystring))
#print(getArrayFromInput(mystring2))

#return precedence priority, the higher the better
def precedence(operator):
  for index,o in enumerate(operators):
    if o==operator:
      return index

#print(precedence("*")>precedence("%"))

#return a calculated operation based on different operators
def operatorSwitch(operator,operand1,operand2):
    return {
        '*': operand2*operand1,
        '/': operand2/operand1,
        '%': operand2%operand1,
        '+': operand2+operand1,
        '-': operand2-operand1,
        
    }[operator]

#print(operatorSwitch("*",3,2))
#print(operatorSwitch("/",3,2))
#print(operatorSwitch("%",3,2))
#print(operatorSwitch("+",3,2))
#print(operatorSwitch("-",3,2))

#main starts here



#INPUT HERE
print("This program works for well formed real number expressions, and as such only accepts the following symbols:")
print(operators+brackets+digits)
isCompatible=False

while(not isCompatible):
  mystring=input("Please input string, or leave blank for default example:")
  isCompatible=True
  isCompatible=wff(mystring)
  if len(mystring)==0:
    mystring="5*(6+2)-12/4" #"(1+1)*13+10/2"
    isCompatible=True
  else:
    for m in mystring:
      if m not in operators+brackets+digits:
        print("\nSymbol",m,"is not in the accepted list, please try again\n")
        isCompatible=False
  
  
    
  
print("\nYour expression is:",mystring)







#TRANSFORM AN INFIX EXPRESSION TO POSTFIX NOTATION
#basically an application of the Shunting-yard algorithm

stack=[]
postfix=[]
infix=getArrayFromInput(mystring)

#print(infix)

i=0
while i<len(infix):
  if infix[i] not in operators+brackets:
    postfix=postfix+[infix[i]]
  if infix[i] in leftbracket:
    stack=[infix[i]]+stack#PUSH
  if infix[i] in rightbracket:
    while len(stack)>0 and stack[0] not in leftbracket:
      postfix=postfix+[stack[0]]
      del stack[0]#POP
    del stack[0]
  if infix[i] in operators:
    if len(stack)<=0 or stack[0] in leftbracket:
      stack=[infix[i]]+stack
    else:
      while len(stack)>0 and stack[0] not in leftbracket and precedence(infix[i])<=precedence(stack[0]):
        postfix=postfix+[stack[0]]
        del stack[0]
      stack=[infix[i]]+stack
  i+=1

while len(stack)>0:
  postfix=postfix+[stack[0]]
  del stack[0]

#print(postfix)
#print(stack)
result=""

for p in postfix:
  result=result+p+" "
  
print("\nYour expression in postfix notation:",result)

#EVALUATE A POSTFIX EXPRESSION

p=0
while p<len(postfix):
  if postfix[p] not in operators:
    stack=[postfix[p]]+stack
  if postfix[p] in operators:
    a=float(stack[0])
    del stack[0]
    b=float(stack[0])
    del stack[0]
    stack=[operatorSwitch(postfix[p],a,b)]+stack
  p+=1

print("\nYour value is:",stack[0])














