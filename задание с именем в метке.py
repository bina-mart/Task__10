from tkinter import *
def click():
    res = 'Здравствуйте, {}'.format(ent.get())
    lab.configure(text=res)
window = Tk()
window.title("Здравствуйте!")
window.geometry('1500x600')
lab = Label(window, text="Введите ваше имя: ")
lab.grid(column=0, row=0)
ent=Entry(window,width=70)
ent.grid(column=1, row=0)
but= Button(window, text="Отправить" ,command=click)
but.grid(column=2,row=0)
window.mainloop()