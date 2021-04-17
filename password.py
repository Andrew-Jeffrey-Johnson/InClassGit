import string
from random import *

def password (length):
	password =  "".join(choice(string.ascii_letters + string.punctuation  + string.digits))
