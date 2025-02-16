#version 1
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
#version 2
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    if alien_color == 'yellow':
        print("You just earned 10 points!")
#version 3
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    if alien_color == 'red':
        print("You just earned 15 points!")