# -- coding: utf-8 --
name = '周谦'
age = 26 # not a lie
height = 168 # centimeters
weight =  69 # kilograms
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %f centimeters tall." % height
print "He's %f kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %.2f, %.2f, and %.2f I get %d." % (
    age, height, weight, age + height + weight)