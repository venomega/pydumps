import time
import sys
import random

import rombo
import _rombo
import square
import triangle
import triangle_inv
import triangle_rec

while True:
        _num = random.randint(3,54)
        moon =random.randint(3,54)
        token =random.randint(1,6)
        if token == 1:
            square.main()
        if token == 2:
            rombo.main()
        if token == 3:
            triangle.main()
        if token == 4:
            triangle_rec.main()
        if token == 5:
            triangle_inv.main()
        if token == 6:
                _rombo.main()
