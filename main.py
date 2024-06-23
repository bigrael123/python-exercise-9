age = 61
if(age>60):
    print("You have the right to the benefit.")
else:
    print("You do not have rights to the benefit")
damage = 11
shield = 0
if(damage > 10 and shield==0):
    print("You are dead.")
else:
    print("You survived")
north = True
south = False
east= False
west = False

if(north or south or east or west == True):
    print("You escaped from the prison.")
else:
    print("You did not escape from the prison.")