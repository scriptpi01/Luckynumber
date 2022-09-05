luckynumber = 69
number = int(input("Enter a number (0-100) : "))
if number >= 0 and number < 100:
  if number == luckynumber:
    print("-"*40)
    print("You found lucky number")
    print("%s %s %s"%("-"*6, "End.","-"*6))
  elif number < luckynumber:
    print("-"*40)
    print("The number is less than lucky number")
    print("Please try again.")
    print("%s %s %s"%("-"*6, "End.","-"*6))
  elif number > luckynumber:
    print("-"*40)
    print("The number is more than lucky number")
    print("Please try again.")
    print("%s %s %s"%("-"*6, "End.","-"*6))
else:
  print("-"*40)
  print("Oops!. I found negative numbers.")
  print("%s %s %s"%("-"*6, "End.","-"*6))