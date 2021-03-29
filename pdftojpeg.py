#pip install pdf2image
#http://blog.alivate.com.au/poppler-windows/

from pdf2image import convert_from_path,convert_from_bytes
import os
import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

poppler_path = r"C:\poppler\Library\bin"

yes = {'yes','y'}
no = {'no','n'}
pdfcounter = 0

def start():
    while True:
        directorypdf = input("Directory PDF : ")
        if directorypdf != '':
            checkPathPDF(directorypdf)
            break
        else:
            continue
    
    outputDir = directorypdf + "/JPEG/"
    print("\ndefault Path Output: ",outputDir)
    outputDir = input("Directory Output : ")
    if outputDir == '':
        outputDir = directorypdf + "/JPEG"

    while True:
        print("\nIs Directory PDF Path : ",directorypdf)
        print("Is Directory Output Path : ",outputDir)
        confirm = input("Confirm Y/n : ").lower()
        if confirm in yes:
            selectfile(directorypdf,outputDir)
            break
        elif confirm in no:
            start()
            break
        else:
            print("Please respond with 'yes' or 'no'")
            continue


def convert(pdfpath,pdfname,outputDir):
    outputDir = outputDir +'/'+str(os.path.splitext(pdfname)[0]) + '/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    counter = 0
    name = str(os.path.splitext(pdfname)[0])+"_"
    pages = convert_from_path(pdfpath,output_folder=outputDir,output_file=name,dpi=500,fmt='jpeg',thread_count=4,paths_only=True,use_cropbox=True,poppler_path=poppler_path)
    for page in pages:
        counter = counter + 1
        print("Save Image ",page)
    print("Convert ",pdfname,"Completed. Image Total",counter)

    # pages = convert_from_path(pdfpath,dpi=500,thread_count=4,single_file=True,first_page=2)
    # counter = 0
    # for page in pages:
    #     counter = counter + 1
    #     myfile = outputDir + str(os.path.splitext(pdfname)[0]) +'-'+ str(counter) +'.jpg'
    #     page.save(myfile, "JPEG")
    #     print("Save Image ",myfile)
    # print("Convert ",pdfname,"Completed. Image Total",counter)


def selectfile(directorypdf,outputDir):
    process_start = time.process_time()
    convertcounter = 0
    for filename in os.listdir(directorypdf):
        if filename.endswith(".pdf"):
            convertcounter = convertcounter+1
            print("\n[",convertcounter,"/",pdfcounter,"]","Convert ",filename," To JPEG...",)
            convert(os.path.join(directorypdf, filename),filename,outputDir)
        else:
            continue

    process_stop = time.process_time()
    processtime = process_stop - process_start
    print("\nProcess Time : ",processtime)
    print("Convert ",pdfcounter," File Completed.")
    confirm = input("Continue?  Y/n : ").lower()
    if confirm in yes:
        start()
    else:
        return False


def checkPathPDF(directorypdf):
    global pdfcounter
    pdfcounter = 0
    for filename in os.listdir(directorypdf):
        if filename.endswith(".pdf"):
            pdfcounter = pdfcounter+1
            print("[",pdfcounter,"]",filename)
        else:
            continue
    print("File PDF Total : ",pdfcounter)
        
try:
    start()
except Exception as ex:
    print("\nError :",ex)
    input("Press Enter key to exit...")


# gui = Tk()
# gui.geometry("800x500")
# gui.title("PDF2IMAGES")

# folderInputPath = StringVar()
# InputLabel = Label(gui ,text="Input Folder")
# InputLabel.grid(row=0,column = 0)
# InputEntry = Entry(gui,textvariable=folderInputPath)
# InputEntry.grid(row=0,column=1)
# InputbtnFind = ttk.Button(gui, text="Browse Folder",command=getFolderInputPath)
# InputbtnFind.grid(row=0,column=2)

# folderOutputPath = StringVar()
# OutputLabel = Label(gui ,text="Output Folder")
# OutputLabel.grid(row=2,column = 0)
# OutputEntry = Entry(gui,textvariable=folderOutputPath)
# OutputEntry.grid(row=2,column=1)
# OutputbtnFind = ttk.Button(gui, text="Browse Folder",command=getFolderOutputPath)
# OutputbtnFind.grid(row=2,column=2)


# c = ttk.Button(gui ,text="Convert", command=doStuff)
# c.grid(row=4,column=0)
# gui.mainloop()

# def getFolderInputPath():
#     folder_selected = filedialog.askdirectory()
#     folderInputPath.set(folder_selected)

# def getFolderOutputPath():
#     folder_selected = filedialog.askdirectory()
#     folderOutputPath.set(folder_selected)

# def doStuff():
#     folderInput = folderInputPath.get()
#     folderOutput = folderOutputPath.get()
#     print("Input folder", folderInput)
#     print("Output folder", folderOutput)