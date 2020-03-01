from random import *
gamelist=[
   [],[],[],
   [],[],[],
   [],[],[]
]

gamelistanswer=[
   [],[],[],
   [],[],[],
   [],[],[]
]
chance=3
correct_ans=0

wronglist=[]
x=0
while x!=3:
    i=randrange(0,9)
    if i not in wronglist:
      gamelistanswer[i]=["*"]
      x+=1
    wronglist.append(i) 
       

print(gamelist)

tricklist=[]
while chance!=0:
   player_input=int(input("enter which: "))
   if player_input in tricklist:
      print("you just waste yor chance \n")
      chance-=1
   elif gamelistanswer[player_input-1]==["*"]:
      gamelist[player_input-1]=["+"]
      correct_ans+=1
      if correct_ans==3:
         break
   else:
      gamelist[player_input-1]=["X"]
      chance-=1
   tricklist.append(player_input)   
   print(gamelist)
   print("\n"+"you have",chance,"chance .Correct answers:",correct_ans ,"of 3")

if correct_ans==3:
   print("YOU WIN!")
else:
   print("YOU LOSE!\n")
   print("look at correct answer:\n")
   print(gamelistanswer)

      
