
import sys
import easygui
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)

    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):

    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    First_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Simplified Arabic Fixed} -size 18 -weight "  \
            "bold -slant roman -underline 0 -overstrike 0"
        font12 = "-family {Baskerville Old Face} -size 14 -weight bold"  \
            " -slant roman -underline 0 -overstrike 0"
        font15 = "-family {Viner Hand ITC} -size 17 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("1288x598")
        top.minsize(116, 1)
        top.maxsize(1370, 750)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.039, rely=0.067, relheight=0.962
                , relwidth=0.974)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.327, rely=0.035, height=34, width=531)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Facial expression recognition System''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.016, rely=0.104, height=474, width=719)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        photo_location = os.path.join(prog_location+"/hdd.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)
        self.Label2.configure(text='''Label''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.653, rely=0.296, height=28, width=30)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''ID''')

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.653, rely=0.383, relheight=0.059, relwidth=0.234)

        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Segoe UI} -size 9")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Text2 = tk.Text(self.Frame1)
        self.Text2.place(relx=0.653, rely=0.574, relheight=0.059, relwidth=0.234)

        self.Text2.configure(background="white")
        self.Text2.configure(font="-family {Segoe UI} -size 9")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")


        self.Text2.configure(wrap="word")
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.653, rely=0.661, height=34, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.Login)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font15)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Label3_1 = tk.Label(self.Frame1)
        self.Label3_1.place(relx=0.645, rely=0.487, height=28, width=96)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#d9d9d9")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Baskerville Old Face} -size 14 -weight bold")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Password''')


    def Login(self):
        a = self.Text1.get("1.0",'end-1c')
        b = self.Text2.get("1.0", 'end-1c')
        if(a=='Admin' and b=='Admin'):

            root.destroy()
            import emodec
            #FirstPage.start_up()
        else:
            easygui.msgbox("Worng ID or Password ")

if __name__ == '__main__':
    vp_start_gui()





