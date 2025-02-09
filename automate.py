import pywhatkit


names= input("please enter the number of the recipeint: ") #enter number of the recipient
message= input("\n please enter the message you want to send to the user: ") #enter the message that needs to be sent

hour= input("\nplease enter the hour in 24 hour format at which you want to send the message: ")
hour=int(hour)

min= input("\nplease enter the minute of the hour at which you want to send the message: ")
min=int(min)


put= pywhatkit.sendwhatmsg(names, message, hour, min) #phone_no: _, message:_, time_hour:_, time_min:_

#the time must be in 24 hour format