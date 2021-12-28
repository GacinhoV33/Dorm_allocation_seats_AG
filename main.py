import run
from tkinter import *
from settings import X_Size, Y_Size, screen_pos_x, screen_pos_y
from tkinter_custom_button import TkinterCustomButton
from tkinter import filedialog
from PIL import ImageTk, Image
csv_path = str()


def Openfile():
    #TODO get root and put in initialdir
    global csv_path
    csv_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                                   filetypes=(("xls files", "*.xls"), ("all files", "*.*")))


def main_screen():
    Root = Tk()
    Root.title("Genetic Algorithm - Dorm Allocation")
    Root.geometry(f'{X_Size}x{Y_Size}+{screen_pos_x}+{screen_pos_y}')

    """ Code responsible for logo"""
    Root.wm_attributes('-transparentcolor', '#ab23ff')
    logo_img = PhotoImage(file='images/books.png')
    Root.tk.call('wm', 'iconphoto', Root._w, logo_img)

    """ Code responsible for background"""
    background_img = ImageTk.PhotoImage(
        (Image.open("images/background.jpg")).resize((X_Size, Y_Size), Image.ANTIALIAS)
    )
    bg_label = Label(Root, image=background_img)
    bg_label.place(x=0, y=0)
    """Shows the name: Genetic Algorithm"""

    """ Shows the flag which light green when ready, red when not ready"""

    """START Button -> When clicked, it run simulation"""

    """REPORT Button -> When Simulation is done, it generate and shows report about simulation and dorm"""

    """Help Button -> When clicked it opens new window with description how to use program"""

    """Choose file with data -> When clicked the browsers opens and user can choose file with data"""
    ChoseButton = TkinterCustomButton(text="Open File", corner_radius=50, command=Openfile)
    ChoseButton.place(x=X_Size//8, y=Y_Size//2)
    """ Generate dataset Button -> When clicked it opens new window with parameters of new dataset """

    """ EXIT Button -> When clicked, it closes application"""

    # test_button = TkinterCustomButton(text="Only for test", )
    # test_button.place(x=50, y=50)

    Root.mainloop()


def main():
    main_screen()


if __name__ == "__main__":
    main()