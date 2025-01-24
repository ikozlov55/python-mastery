import importlib
import sys

import simplemod

simplemod.foo()

print(simplemod.x)
simplemod.x = 13
print(simplemod.x)

importlib.reload(simplemod)
print(simplemod.x)

del sys.modules['simplemod']
import importlib
print(simplemod.x)

s = simplemod.Spam()
s.yow()