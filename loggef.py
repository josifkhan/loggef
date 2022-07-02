
import os

if "aarch64" in os.uname():
	import loggef
elif "arm" in os.uname():
	import loggef32
else:
	print("system not supported")
	sys.exit()
