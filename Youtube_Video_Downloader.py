from tkinter import *
from tkinter import ttk
from tkinter import  filedialog
from pytube import  YouTube
root = Tk()
root.title("YVD")
root.geometry("350x400")
# root['bg']='black'
root.columnconfigure(0,weight=1)#set all content in center

def openlocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>0):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(tetx=Folder_Name,fg="red")

def DowloadVideo():
    choice = yvdchoices.get()
    url=yvdEntry.get()
    if (len(url)>1):
        yvdError.config(text="")
        yt=YouTube(url)
        if(choice==choices[0]):
            select= yt.streams.filter(progressive=True).first()
        elif(choice==choices[1]):
            select= yt.streams.filter(progressive=True,file_extension='mp3').last()
        elif(choice==choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            yvdError.config(text="Paste link again!!!!",fg="red")
    #download Function
    select.download(Folder_Name)
    yvdError.config(text="Download complete!!")

#Y_V_d link label
yvdLabel = Label(root,text="Enter the url of the video",fg="green",font=("jost",15))
yvdLabel.grid()

#Entery Box
yvdEntryvar = StringVar()
yvdEntry = Entry(root,width=50,textvariable=yvdEntryvar)
yvdEntry.grid()

#Error box
yvdError = Label(root,text="Error msg",fg="red",font=("jost",15))
yvdError.grid()

#Asking to save file Label
SaveLabel=Label(root,text="Save the Video File\n",font=("jost",15))
SaveLabel.grid()

#booton of save file location
SaveEntry=Button(root,width=20,bg="blue",fg="White",text="Choose path",command=openlocation)
SaveEntry.grid()

#Error message location
locationError = Label(root,text="*  Error  * Please Enter right path \n",fg="red",font=("jost",15))
locationError.grid()

#Download Quality
yvdQuality=Label(root,text="Select Quality\n",font=("jost",15))
yvdQuality.grid()

#Combo box
choices=["720p","144p","only Audio"]
yvdchoices=ttk.Combobox(root,value=choices)
yvdchoices.grid()

#Download button
downloadbtn=Button(root,text="Download  video",width=10,fg ='white',bg="blue",command=DowloadVideo)
downloadbtn.grid()

#develop label
developerLabel=Label(root,text="\n\n***Developer Its_Soni_Aman1710  ***\n",pady=20,fg="blue",font=("italic",16))
developerLabel.grid()

root.mainloop()
