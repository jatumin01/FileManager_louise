import sys
import getpass
userProfile = "C:/Users/"+getpass.getuser() + "/Documents/FileManager_louise"
if not userProfile in sys.path:
    sys.path.append(userProfile)

import fileManagerPackage.FM_gui as gui
reload(gui)
