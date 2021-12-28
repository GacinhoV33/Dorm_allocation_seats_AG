from run import start_simulation
from tkinter import *
from settings import X_Size, Y_Size, screen_pos_x, screen_pos_y, BigB_X, BigB_Y
from tkinter_custom_button import TkinterCustomButton
from tkinter import filedialog
from PIL import ImageTk, Image
csv_path = str()

"""Variables used in GUI"""


def Generate_Report(Root):
    Root.update()


def Help_User():
    HelpRoot = Toplevel()
    HelpRoot.title("Help for new users")
    #TODO
    HelpRoot.mainloop()


def Exit_app(root):
    root.destroy()


def Generate_DataSet():
    GenRoot = Toplevel()
    GenRoot.title("Generate DataSet for simulation")
    #TODO

    GenRoot.mainloop()


def Openfile():
    #TODO get root and put in initialdir
    global csv_path
    csv_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                                   filetypes=(("xls files", "*.xls"), ("all files", "*.*")))


def main_screen():
    Root = Tk()
    Root.title("Genetic Algorithm - Dorm Allocation")
    Root.geometry(f'{X_Size}x{Y_Size}+{screen_pos_x}+{screen_pos_y}')
    Mutation_Swap_Flag = IntVar()
    Mutation_AddNon_Flag = IntVar()

    """ Code responsible for logo"""
    Root.wm_attributes('-transparentcolor', '#ab23ff')
    logo_img = PhotoImage(file='images/agh.png')
    Root.tk.call('wm', 'iconphoto', Root._w, logo_img)

    """ Code responsible for background"""
    background_img = ImageTk.PhotoImage((Image.open("images/genetic.jpeg")).resize((X_Size, Y_Size), Image.ANTIALIAS))
    main_Canv = Canvas(Root, width=X_Size, height=Y_Size)
    main_Canv.create_image(0, 0, image=background_img, anchor='nw')
    main_Canv.pack(fill='both', expand=True)
    """ Logo of AGH"""


    """Shows the name: Genetic Algorithm"""
    main_Canv.create_text(X_Size//2.05, Y_Size//10, text="Genetic Algorithm", font=('Helvetica', 30), fill='#FFFFFF') #TODO Set good color

    """ Shows the name: Simulation Parameters"""
    main_Canv.create_text(X_Size//1.2, Y_Size//4, text="Simulation Parameters", font=('Helvetica', 22), fill='#12FF11') #TODO Set good color
    """ Shows the flag which light green when ready, red when not ready"""

    """START Button -> When clicked, it run simulation"""
    StartButton = TkinterCustomButton(text="START", corner_radius=10,
                command=lambda: start_simulation("Data/Test_december19.xls", None, 100, 50),
                bg_color="#142434", width=BigB_X, height=BigB_Y)
    StartButton.place(x=X_Size//2.43, y=Y_Size//5)
    """REPORT Button -> When Simulation is done, it generate and shows report about simulation and dorm"""
    GenerateReportButton = TkinterCustomButton(text="Generate Report", corner_radius=10, width=BigB_X, height=BigB_Y,
                                               command=lambda: Generate_Report(Root), bg_color="#425b9a")
    GenerateReportButton.place(x=X_Size//10, y=Y_Size//2)

    """Help Button -> When clicked it opens new window with description how to use program"""
    HelpButton = TkinterCustomButton(text="Help", corner_radius=10, width=BigB_X, height=BigB_Y, command=Help_User, bg_color="#4f6aaf")
    HelpButton.place(x=X_Size//10, y=Y_Size//2.39)
    """Choose file with data -> When clicked the browsers opens and user can choose file with data"""
    ChoseButton = TkinterCustomButton(text="Open File", corner_radius=8, command=Openfile, width=BigB_X, height=BigB_Y, bg_color="#6580c3")
    ChoseButton.place(x=X_Size//10, y=Y_Size//4)
    """ Generate dataset Button -> When clicked it opens new window with parameters of new dataset """
    GenerateButton = TkinterCustomButton(text="Generate Dataset", corner_radius=8, command=Generate_DataSet,
                                         height=BigB_Y, width=BigB_X,bg_color="#6580c3")
    GenerateButton.place(x=X_Size//10, y=Y_Size//3)

    """Parameters of Simulation"""
    MutationSwapButton = Checkbutton(Root, text="Swap Mutation", variable=Mutation_Swap_Flag)
    MutationSwapButton.place(x=X_Size//1.2, y=Y_Size//2)

    MutationAddNonButton = Checkbutton(Root, text="AddNon Mutation", variable=Mutation_AddNon_Flag)
    MutationAddNonButton.place(x=X_Size // 1.2, y=Y_Size // 1.8)

    """ EXIT Button -> When clicked, it closes application"""
    ExitButton = TkinterCustomButton(text="EXIT", corner_radius=3, fg_color="#FF0000", bg_color="#081117", command=lambda: Exit_app(Root))
    ExitButton.place(x=X_Size//1.11, y=Y_Size//1.08)

    Root.after(1000, Root.update())
    Root.mainloop()


def main():
    main_screen()


if __name__ == "__main__":
    main()