# programmed in python 
# by  josemaj 
#Copyright 2016 josemaj
# published 27-5-2016 
#everything is under  GNU General Public License
#http://www.gnu.org/licenses/gpl-3.0.html
# read the license.txt and README.md 
life = 60
money = 50 
food = 50 
print "if you need help write sos"
while (life >= 0): 
 print " ^^^^^ "
 print "( 0 0 )"
 print "   !   "
 print " |___| "
 print " |   | "      
 
 question = raw_input("Order me something or ask something :" )
 
 if question == "eat": 
  print " eating "
  print " delicious " 
  food -=1 
  life +=2    
 if question == "buy":  
   print "buying"
   money -=1
   food +=2  
 if question == "work": 
   print "working" 
   em = 5  
   while(em >=0 ): 
    em -=1 
    print em  
   money +=5 
   life -=2 
   print " finished work "
   print " do you have " 
   print  money  
 if question == "status":   
     print " ^^^^^"
     print "( 0 0 )"
     print "   !  " 
     print " |___|"  
     print " |___|"
   
     print "my state is:" 
     print "life:"  
     print  life
     print "money:"
     print  money
     print "food: " 
     print  food
 if question == "life":
   print life 
 if question == "sos":   
  print " command "
  print "life shows you your life "
  print " status : tells you how are you all -_- "
  print " works : work to get money &_&"
  print " buy : buy food T_T "
  print "eat"
 if question == "sleep": 
    
   print " ^^^^^ "
   print "( _ _ ) "
   print "   !    z " 
   print " |___| z "  
   print " |___|z "  
   life +=5  
   z = 0 
   while(z <= 0):
     a = raw_input(":") 
     if a == "up":
       z += 2  
     if a == "help": 
      print "write up" 
 if question == "suicide": 
  life -=10000    
 
 
 life -=1 

print " ___ "
print "[   ]" 
print "|RIP|"
print "|   |" 
print "|___|"
         
