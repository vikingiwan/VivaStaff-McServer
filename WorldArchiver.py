### World Archiver ###
### By: Iwan ###

import shutil
import datetime
from pathlib import Path

# VARIABLES #
worldName = "vivaland"

def getName():
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	name = "backups/" + timestamp
	return name

# MAIN LOOP #
Path("backups").mkdir(parents=True, exist_ok=True)
print("This will create an archive of the folder in the current directory called " + worldName)
_ = input("Press Enter to continue")
shutil.make_archive(getName(), 'zip', root_dir=worldName)