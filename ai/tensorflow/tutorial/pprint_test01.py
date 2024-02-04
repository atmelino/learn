import pprint

print("pprint test")
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)



mystring=pprint.pformat(stuff, indent=1, width=200, depth=None)

print(mystring)