import os
import pefile
import pandas as pd
import numpy as np
import pickle
file_path = raw_input("Enter FilePath: ")
def features(filename):
    pe = pefile.PE(filename ,fast_load = True)
    filename = filename
    DebugSize = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
    DebugRVA = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress
    ImageVersion = pe.OPTIONAL_HEADER.MajorImageVersion
    OSVersion = pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
    ExportRVA = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
    ExportSize = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
    IATRVA = pe.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress
    ResSize = pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size
    LinkerVersion = pe.OPTIONAL_HEADER.MajorLinkerVersion
    NumberOfSections = pe.FILE_HEADER.NumberOfSections
    StackReserveSize = pe.OPTIONAL_HEADER.SizeOfStackReserve
    Dll = pe.OPTIONAL_HEADER.DllCharacteristics
    data = {"DebugSize" : DebugSize , "DebugRVA": DebugRVA , "ImageVersion" : ImageVersion , "OSVersion":OSVersion,"ExportSize":ExportSize,"ExportRVA":ExportRVA,
    "IATRVA":IATRVA,"ResSize":ResSize,"LinkerVersion":LinkerVersion,"NumberOfSections":NumberOfSections,"StackReserveSize":StackReserveSize,"Dll":Dll}
    return data

data = features(file_path)
df = pd.DataFrame(data,dtype = float , index = [0])
pickle_in = open('randomforest.pickle','rb')
clf = pickle.load(pickle_in)
X_new = df
X_new = np.asarray(X_new)
X_new = X_new[:,1:]
# print X_new
y_pred=clf.predict(X_new)
if int(y_pred) == 0:
	print "File is malicious"
else:
	print "File is clean"