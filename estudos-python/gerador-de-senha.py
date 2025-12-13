import string
import random
print('Password: ', ''.join(random.choice(string.ascii_letters + string.digits) for _ in range (8)))
