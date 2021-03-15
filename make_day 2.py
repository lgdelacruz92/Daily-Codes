#!/usr/bin/env python
from datetime import date
import os

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")
os.system('mkdir {d1}'.format(d1=d1))
