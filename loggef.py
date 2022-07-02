




from os import uname as u
from sys import exit as e


if 'aarch64' in str(u()[4]):
    import loggef
elif 'arm' in str(u()[4]):
    import loggef32
else:
    print("System not supported")
    e()