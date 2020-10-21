import random as rn
import string as st

upper1 = rn.choice(st.ascii_letters).upper()
upper2 = rn.choice(st.ascii_letters).upper()

lower1 = rn.choice(st.ascii_letters).lower()
lower2 = rn.choice(st.ascii_letters).lower()

digit1 = rn.choice(st.digits)
digit2 = rn.choice(st.digits)

punt1 = rn.choice(st.punctuation)
punt2 = rn.choice(st.punctuation)

password = [upper1, upper2, lower1, lower2, digit1, digit2, punt1, punt2]
rn.shuffle(password)

print(password)