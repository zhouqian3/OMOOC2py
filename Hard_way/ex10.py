tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
blackslash_cat = "I'm \\ a \\ cat"
# \\this is backblash
# \t is a tab
# \n is a new line

fat_cat = '''
I\'ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# we can use both ''' or """

print tabby_cat
print persian_cat
print blackslash_cat
print fat_cat

print "%r" % fat_cat
print "%s" % fat_cat
# the difference between %r and %s is that r will print the code