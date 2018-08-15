import os
import pefile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
directory = ''
sample = []
Ds = []
Dr =[]
Iv =[]
Os = []
Es = []
Er = []
Ia = []
Rs = []
Lv = []
Nos = []
Srs = []
dll = []

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
    constructlist(DebugSize,DebugRVA,ImageVersion,OSVersion,ExportSize,ExportRVA,IATRVA,ResSize,LinkerVersion,NumberOfSections,StackReserveSize,Dll)
def constructlist(DebugSize,DebugRVA,ImageVersion,OSVersion,ExportSize,ExportRVA,IATRVA,ResSize,LinkerVersion,NumberOfSections,StackReserveSize,Dll):
    if DebugRVA > 0 and ImageVersion > 0 :
        Ds.append(DebugSize)
        Dr.append(DebugSize)
        Iv.append(ImageVersion)
        Os.append(OSVersion)
        Es.append(ExportSize)
        Er.append(ExportRVA)
        Ia.append(IATRVA)
        Rs.append(ResSize)
        Lv.append(LinkerVersion)
        Nos.append(NumberOfSections)
        Srs.append(StackReserveSize)
        dll.append(Dll)
        # sample.append([DebugSize,DebugRVA,ImageVersion,OSVersion,ExportSize,ExportRVA,IATRVA,ResSize,LinkerVersion,NumberOfSections,StackReserveSize,Dll])
for dir,subdir,files in os.walk(directory):
    for file in files:
        file_path = directory +  "\ ".strip() + file
        try:
            features(file_path)
        except Exception as e:
            print file,e
data = {"DebugSize" : Ds , "DebugRVA": Dr , "ImageVersion" : Iv , "OSVersion":Os,"ExportSize":Es,"ExportRVA":Er,"IATRVA":Ia,"ResSize":Rs,"LinkerVersion":Lv,"NumberOfSections":Nos,"StackReserveSize":Srs,"Dll":dll,"clean":1}
dataset = pd.DataFrame(data,dtype = float)
#dataset = pd.DataFrame(data,columns = ['DebugSize','DebugRVA','ImageVersion','OSVersion','ExportSize','ExportRVA','IATRVA','ResSize','LinkerVersion','NumberOfSections','StackReserveSize','Dll'])
dataset.to_csv('clean1.csv',sep=',', encoding='utf-8',index = False)
