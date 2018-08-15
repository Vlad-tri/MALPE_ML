import os
from shutil import copy


dest = ""

# a = open("output.txt", "w")
for path, subdirs, files in os.walk('C:\Users\.....\Desktop\crawler' +  "\ ".strip()):
    if path != "C:\Users\......\Desktop\clean":
        for filename in files:
            if filename.endswith('.dll') or filename.endswith('.exe') or filename.endswith('.sys') or filename.endswith('.acm') or filename.endswith('.ax') or filename.endswith('.drv') or filename.endswith('.efi') or filename.endswith('.mui') or filename.endswith('.scr') or filename.endswith('.ocx') or filename.endswith('.tsp'):
                f = os.path.join(path, filename)
                # print "src = ",f
                try:
                    copy(f, dest)
                except Exception as e :
                    print "error",f,e
        #    a.write(str(f) + os.linesep)
