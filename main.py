import re
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('800x600+0+0')
root.title('corretor de palavras')

textoe = Text(root,font=('Arial',18))
textoe.place(x=20,y=10,width=760,height=350)

Label(root,text='palavra antiga:',font=('Arial',15)).place(x=10,y=397)
antigae = Entry(root,font=('Arial',15))
antigae.place(x=150,y=400,width=130)

Label(root,text='palavra nova:',font=('Arial',15)).place(x=10,y=457)
novoe = Entry(root,font=('Arial',15))
novoe.place(x=150,y=460,width=130)

btn = Button(root,text='substituir',font=('Arial',30),bg='snow',fg='steelblue',bd=5,command=lambda:mudar(antigae.get(),novoe.get(),textoe.get('1.0',END)))
btn.place(x=15,y=510)

def mudar(antiga,novo,texto):
    if antiga == '' or novo == '' or texto == '':
        messagebox.showerror('mensagem de erro','porfavor preencha tudo !!!')
        return
    res = re.sub("{}".format(antiga),"{}".format(novo),texto)
    antigae.delete(0,END)
    novoe.delete(0,END)
    textoe.delete(1.0,END)
    textoe.insert(1.0,str(res))
    
    
    
root.mainloop()