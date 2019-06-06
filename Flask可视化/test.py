import sys
import os
print(os.environ)
for item in os.environ.items():
    print(item[0], item[1])
    # print(item[1])