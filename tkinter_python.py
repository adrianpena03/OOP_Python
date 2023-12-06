from tkinter import *

root = Tk()
root.title('Tip Calulator')

frame = Frame(root, height = 400, width = 300)
frame.pack()

root.mainloop() # executes the code above

class MyFrame(Frame):
    def __init__(self, root, ht = 400, wd = 300):
        Frame.__init__(self, root, height = ht, width = wd)
        
        label_bill = Label(self, text = 'Enter bill amount.')
        self.bill = Entry(self, width = 20)
        label_tip = Label(self, text = 'Enter desired tip (%). ')
        self.tip = Entry(self, width = 20)
        button = Button(self, text = "CALCULATE", command = self.click)
        label_result = Label(self, self, text = "Your tip is: ")
        self.result = StringVar()
        final_result = Label(self, textvariable = self.result)

    def click(self):
        pass