# Script to copy all xml files in different folders to a common folder All_xmlData.
import os
from os import path
import shutil
import time

#place this file with all NCT folders in main Directory.

start_time = time.time()

# To get Current directory.
Current_dir = os.getcwd()
directories = [i for i in os.listdir(Current_dir) if path.isdir(path.join(Current_dir, i))]

# To make new Directory. Which will contain all xml files.
os.mkdir("All_xmlData")

dst = os.path.join(Current_dir, "All_xmlData")

try:
	for f in directories:
		paths = os.path.join(Current_dir, f)
		files = os.listdir(f)
		for file in files:

			shutil.copy(path.join(paths,file), dst)

except Exception:
	pass

print("Total time = {}".format(time.time()-start_time))

