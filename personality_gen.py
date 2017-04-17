import random
from name_data import male_given
from name_data import female_given
from name_data import surname
from character_events import event, birth



x = birth(None,None,None,None,None,None,None)
x.generate()
print(x)