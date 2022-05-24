from consolemenu import *
from consolemenu.items import * 
import time
import pickle  
import sys, select
import os

total_timers = 0
total_flashcards = 0
total_tasks = 0
timers = 45


# TIMER FEATURE
def Timer(): 
  global timers
  breaktimer = 5
  pomodorotimer = 10
  status = True

# define the countdown func.

  def countdown():
    global status
    user1 = input("\nDo you want to start a Pomodoro timer? (Y/N) ")
    if (user1 == "Y"):
      t1 = pomodorotimer
      pomodoro_countdown(t1)
    elif (user1 == "N"):
      status = False
      start()
    else:
      print('\nPlease input Y or N')
    
    
  
  def pomodoro_countdown(t1):
      t2 = breaktimer
      while t1:
      #divides the time given in seconds
          mins, secs = divmod(t1, 60)
          timer = '{:02d}:{:02d}'.format(mins, secs)
          print(timer, end="\r")
          time.sleep(1)
          t1 -= 1
      
      print('\nThe work timer is finished! You have worked for '+str(45*timers) + ' minutes')
      print('\nYour break time is starting')

      break_countdown(t2)
  def break_countdown(t2):
    while t2:
      #divides the time given in seconds
        mins, secs = divmod(t2, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t2 -= 1
      
    print('\nThe break timer is finished!')
    print('______________________________')

  while status:
    timers+=1
    countdown()





# TO DO LIST FEATURE 

#TO DO LIST FEATURE
def ToDoList():
  stuffToDo = []
  timesToDoIt = []
  
  def mainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Main menu: ")
    x = input("Enter: \n1 to add a task to the To Do list,\n2 to view list,\nx to exit: ")
    a = (x != "1")
    b = (x != "2")
    if x == "x":
        start()
    while (a and b):
      os.system('cls' if os.name == 'nt' else 'clear')
      x = input("1 to add to ToDo list,\n2 to veiw list,\nx to exit: ")
      a = (x != "1")
      b = (x != "2")
      if x == "x":
        start()
      
    if x == "1":
      addToDo()
    if x == "2":
      ToDo()
  
  def addToDo():
    os.system('cls' if os.name == 'nt' else 'clear')
    a = "- " + input("ToDo: ")
    x = input("0 for no alarm time,\ninput alarm time in minutes: ")
    stuffToDo.append(a)
    if (x == "0"):
      timesToDoIt.append("NoTimer")
    else:
      timesToDoIt.append(str((float(x))*60))
    mainMenu()
    
  def ToDo():
    
    while 1 == 1:
      a = -1
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Time only progresses in this menu")
      print("Click enter to exit, or enter the # task completed")
      print("\nTo Do List:")
      for i in stuffToDo:
        a+=1
  
        try:
          bb = float(timesToDoIt[a])
          bb-=1
          timesToDoIt[a] = str(bb)
          if float(timesToDoIt[a]) <= -1:
            timesToDoIt.pop(a)
            stuffToDo.pop(a)
            continue;
        except:
          pass
  
        try:
          if float(timesToDoIt[a]) > -1:
            print(str(a+1) + " " + i + ", Time left (seconds): " + str(timesToDoIt[a]))
          else:
            print(str(a+1) + " " + i + ", Time left (seconds): " + "0")
        except:
          print(str(a+1) + " " + i + "")
      i, o, e = select.select( [sys.stdin], [], [], 1 )
      if (i):
        n = input("")
        n = input("x to exit or input task number to complete: ")
        if (n == "x") or (n == "X"):
          mainMenu()
        else:
          try:
            n = int(n)
            timesToDoIt.pop(n-1)
            stuffToDo.pop(n-1)
          except:
            continue;
  
  mainMenu()
##if __name__ == '__main__':
  




  
#ACHIEVEMENTS
def Achievements():
  global total_timers
  global total_flashcards
  global total_tasks
  while True:
    userinput1 = input("Do you want to see your achievements (Y/N)? ")
    if (userinput1 == "Y"):
      print("\nYou studied for "+str(total_timers*45) + " minutes")
      print("You made "+str(total_flashcards) + " flashcards")
      print("You finished  "+str(total_tasks) + " tasks")
      
      userinput2 = input("\nPress x to exit ")
      if (userinput2 == "x"):
        start()
    elif (userinput1 == "N"):
      start()
    else:
      print("\n Please type Y or N.")
    
              
  #total_flashcards = 0
  #total_tasks = 0
try: 
  with open("FlashCards.pkl","rb") as ifp: 
    my_FC = pickle.load(ifp)
except: 
  my_FC = {} 



#MAIN MENU SETUP
def f_create(): 
  x = input("Enter term you would like to add to your flashcards: ") 
  y = input("Enter definition you would like to add to this term: ") 

  my_FC[x] = y 

  with open("FlashCards.pkl","wb") as file_to_write: 
    pickle.dump(my_FC,file_to_write)
    print("Added to flash cards")

  l = input("Press enter to return to the main menu")

  
def f_study(): 

  for key, value in my_FC.items():
    print(key) 
  x = len(my_FC)
  print(x)

  R = input("Enter 1 to reveal definitions or 2 to quit to the Main Menu")
  
  if R == str(1): 
    for key, value in my_FC.items():
      print(value)  
    l = input("Press enter to return to the main menu")
    
  if R == str(2): 
    e = input("Press enter to return to the main menu")

  

def f_timer():
  Timer()

  
def f_todolist():
  ToDoList()

def f_achievements():
  Achievements()
  
##main screen
def start():
  menuR = ConsoleMenu("Welcome to Study App!","Created by Team Orange")
  
  function_item1= FunctionItem("Create a new flashcard", f_create)
  function_item2= FunctionItem("Study Flashcards", f_study) 
  function_item3 = FunctionItem("Timer", f_timer)
  function_item4 = FunctionItem("To Do List", f_todolist)
  function_item5 = FunctionItem("Achievements", f_achievements)
  
  menuR.append_item(function_item1)
  menuR.append_item(function_item2)
  menuR.append_item(function_item3)
  menuR.append_item(function_item4)
  menuR.append_item(function_item5)

  menuR.show()
  
  try: 
    with open("FlashCards.pkl","wb") as file_to_write: 
      pickle.dump(my_FC,file_to_write)
      print("Flashcards saved")
  except: 
    pass

start()