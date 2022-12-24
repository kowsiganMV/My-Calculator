from tkinter import*

root=Tk()
input=Entry(root,width=60)
input.grid(row=0, column=0,columnspan=3,padx=10)
input1=Entry(root)
input1.grid(row=0, column=3)
ans=0
ans1=0
head=""
first=0

#Click button Action

def click(num):
  temp=input.get()
  input.delete(0,END)
  input.insert(0,str(temp)+str(num))
  return 

#Ad Action

def add():
  global ans,head,ans1,first
  first+=1
  temp=input.get()
  if "ans"==temp:
    temp=ans
  ans=int(temp)  
  head+="+"
  input.delete(0,END)
  input1.delete(0,END)
  return
#mi Action

def mi():
  global ans,head,ans1,first
  first+=1
  temp=input.get()
  if "ans"==temp:
    temp=ans
  ans=int(temp)  
  head+="-"
  input.delete(0,END)
  input1.delete(0,END)
  return
#Mul Action

def mul():
  global ans,head,ans1,first
  first+=1
  temp=input.get()
  if "ans"==temp:
    temp=ans
  ans=int(temp)  
  head+="*"
  input.delete(0,END)
  input1.delete(0,END)
  return
#Div button

def div():
  global ans,head,ans1,first
  first+=1
  temp=input.get()
  if "ans"==temp:
    temp=ans
  ans=int(temp)  
  head+="/"
  input.delete(0,END)
  input1.delete(0,END)
  return
#AC button Action

def Ac():
  global ans,ans1
  input.delete(0,END)
  input1.delete(0,END)
  ans=0
  ans1=0
  return

#Equels Action
def eq():
  temp=input.get()
  global ans,head,ans1,first
  if head=="+":
    if first==1:
      ans1+=ans
    ans1+=int(temp)
  elif head=="-":
    if first==1:
      ans1+=ans
    ans1-=int(temp)
  elif head=="*":
    if first==1:
      ans1+=ans
    ans1*=int(temp)
  elif head=="/":
    if first==1:
      ans1+=ans
    ans1/=int(temp)
  input.delete(0,END)
  input.insert(0,"ans")
  input1.insert(0,str(ans1))
  head=""
  return
#Buttons

button1=Button(root,text="1",padx=50,pady=25,command=lambda:click(1))
button2=Button(root,text="2",padx=50,pady=25,command=lambda:click(2))
button3=Button(root,text="3",padx=50,pady=25,command=lambda:click(3))
button4=Button(root,text="4",padx=50,pady=25,command=lambda:click(4))
button5=Button(root,text="5",padx=50,pady=25,command=lambda:click(5))
button6=Button(root,text="6",padx=50,pady=25,command=lambda:click(6))
button7=Button(root,text="7",padx=50,pady=25,command=lambda:click(7))
button8=Button(root,text="8",padx=50,pady=25,command=lambda:click(8))
button9=Button(root,text="9",padx=50,pady=25,command=lambda:click(9))
button0=Button(root,text="0",padx=50,pady=25,command=lambda:click(0))
buttonpl=Button(root,text="+",padx=50,pady=25,command=lambda:add())
buttonmi=Button(root,text="-",padx=50,pady=25,command=lambda:mi())
buttonac=Button(root,text="AC",padx=45,pady=25,command=lambda:Ac())
buttondiv=Button(root,text="/",padx=50,pady=25,command=lambda:div())
buttonmul=Button(root,text="*",padx=50,pady=25,command=lambda:mul())
buttoneq=Button(root,text="=",padx=50,pady=25,command=lambda:eq())

#1
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
buttonac.grid(row=1,column=3)
#2
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonmul.grid(row=2,column=3)
#3
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
buttondiv.grid(row=3,column=3)
#4
button0.grid(row=4,column=0)
buttonpl.grid(row=4,column=1)
buttonmi.grid(row=4,column=2)
buttoneq.grid(row=4,column=3)

root.mainloop()
