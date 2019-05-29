import os
try:
    DEVELOP = os.environ.get('ENV') in ['DEV',]
except KeyError:
    DEVELOP = False

print (DEVELOP)

if DEVELOP:
    print ('DEVELOP')
    from .develop import *
    print(STATIC_ROOT)
    print(STATIC_ROOT)
else:
    print ('PRO')
    from .prodaction import *