from run import start_simulation
from tkinter import *
from settings import X_Size, Y_Size, screen_pos_x, screen_pos_y, BigB_X, BigB_Y
from tkinter_custom_button import TkinterCustomButton
from tkinter import filedialog
from PIL import ImageTk, Image
import CreateToolTip
from report import PDF
from tkinter import messagebox
import os
import time

#TODO
# dorms buttons with hints - done
# is_ready button with 3 colors - not done
# status of simulation showed on screen - not done
# Generate Dataset window - half done -> Dorms
# Generate Report after simulation - half done -> People setted
# Add hints to Selections
"""Global Variables to simulation"""
csv_path = None
n_of_people = 200
number_of_individuals: int = 0
number_of_students: int = 0
dorm_flag = 1
number_of_iterations: int = 20
mutation_non_included_probability: float=0.1
mutation_swap_probability: float=0.1
mutation_swap_flag: bool=True
mutation_non_included_flag:bool=True
rullet_selection_flag: bool=True
tournament_selection_flag=False
rank_selection_flag = False
best_solution = None


def SaveEverything(root, MutSwapFlag: int, MutAddNonFlag: int, MutSwapProb: float, MutAddNonProb: float,
                   Selection: str, N_iterations: int, N_individuals: int, dorm_type: int, Simtext):
    print(MutSwapFlag, MutAddNonFlag, MutAddNonProb, MutSwapProb, Selection, N_iterations, N_individuals)
    global number_of_individuals, dorm_flag, number_of_iterations, mutation_non_included_probability #TODO Dorm options
    global mutation_swap_probability, mutation_swap_flag, mutation_non_included_flag, rullet_selection_flag
    global tournament_selection_flag, csv_path, rank_selection_flag
    number_of_individuals = N_individuals
    number_of_iterations = N_iterations
    mutation_non_included_flag = bool(MutAddNonFlag)
    mutation_swap_flag = bool(MutSwapFlag)
    mutation_swap_probability = 0.01 * MutSwapProb
    mutation_non_included_probability = 0.01 * MutAddNonProb
    dorm_flag = dorm_type
    Simtext.config(text="Data ready", fg="#ffffff", bg='#19a56f')
    Simtext.place_configure(x=X_Size//2.54, y=Y_Size//1.25)
    root.update()
    if Selection == "Rullet":
        rullet_selection_flag = True
        tournament_selection_flag = False
        rank_selection_flag = False
    elif Selection == "Tournament":
        rullet_selection_flag = False
        tournament_selection_flag = True
        rank_selection_flag = False
    elif Selection == "Rank":
        rullet_selection_flag = False
        tournament_selection_flag = False
        rank_selection_flag = True


def start_working(Root, SimText):
    global best_solution
    SimText.config(text="Algorithm is working", font=('Helvetica', 30), bg='#ff9f3f', fg="#fffaef")
    SimText.place_configure(x=X_Size//2.86)
    Root.update()

    if csv_path:
        best_sol = start_simulation(csv_path, None, number_of_iterations, number_of_individuals,
                         mutation_non_included_probability, mutation_swap_probability, mutation_swap_flag,
                         mutation_non_included_flag, rullet_selection_flag, tournament_selection_flag, rank_selection_flag,
                         dorm_flag, True)
    else:
        best_sol = start_simulation(None, n_of_people, number_of_iterations, number_of_individuals,
                         mutation_non_included_probability, mutation_swap_probability, mutation_swap_flag,
                         mutation_non_included_flag, rullet_selection_flag, tournament_selection_flag, rank_selection_flag,
                         dorm_flag, True)
    SimText.config(text="Solution is ready", font=('Helvetica', 30), bg='#13f500', fg="#f6fffb")
    SimText.place_configure(x=X_Size//2.78)
    Root.update()
    best_solution = best_sol


def Generate_Report(root, Simtext):
    global best_solution

    if best_solution:
        doc = PDF(best_solution)
        doc.generate()
        time.sleep(1)
        Simtext.config(text="Report generated successfully", fg="#ffffff", bg='#19a56f')
        Simtext.place_configure(x=X_Size // 3.25, y=Y_Size // 1.25)
        root.update()
        os.system("start " + doc.file_path)
    else:
        messagebox.showerror(title="Error", message="There's no valid solution yet. Start simulation first.")


def Help_User():
    HelpRoot = Toplevel()
    HelpRoot.title("Help for new users")
    #TODO HELP
    HelpRoot.mainloop()


def Exit_app(root):
    root.destroy()


def Generate_DataSet():
    GenRoot = Toplevel()
    GenRoot.title("Generate DataSet for simulation")
    GenRoot.geometry(f"{X_Size//4}x{Y_Size//2}")

    NpeopleLabel = Label(GenRoot, text="Number of Students:")
    NpeopleLabel.place(x=X_Size//70, y=Y_Size//20)
    NpeopleEntry = Entry(GenRoot)
    NpeopleEntry.insert(0, '200')
    NpeopleEntry.place(x=X_Size//9, y=Y_Size//20)

    NplaceLabel = Label(GenRoot, text="Number of free place:")
    NplaceLabel.place(x=X_Size//70, y=Y_Size//11)
    NplaceEntry = Entry(GenRoot)
    NplaceEntry.insert(0, '100')
    NplaceEntry.place(x=X_Size // 9, y=Y_Size // 11)

    """DORM settings"""

    GenRoot.mainloop()


def Openfile():
    global csv_path
    csv_path = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", title="Select a file",
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

    """Shows the name: Genetic Algorithm"""
    main_Canv.create_text(X_Size//2.05, Y_Size//10, text="Genetic Algorithm", font=('Helvetica', 30), fill='#FFFFFF') #TODO Set good color

    """ Shows the name: Simulation Parameters"""
    main_Canv.create_text(X_Size//1.2, Y_Size//4, text="Simulation Parameters", font=('Times-Roman', 22), fill='#FDFFD9') #TODO Set good color
    """ Shows the flag which light green when ready, red when not ready"""

    SimText = Label(Root, text="Data not ready", font=('Helvetica', 30), fg='#ffdddc', bg='#FF2231')
    SimText.place(x=X_Size//2.63, y=Y_Size//1.25)
    """START Button -> When clicked, it run simulation"""
    StartButton = TkinterCustomButton(text="START", corner_radius=10,
                command=lambda: start_working(Root, SimText),
                bg_color="#142434", width=BigB_X, height=BigB_Y)
    StartButton.place(x=X_Size//2.43, y=Y_Size//5)
    CreateToolTip.CreateToolTip(StartButton, text="Click this button to start simulation.\nRemember to ensure that all parameters were inserted correctly and you clicked Save button")
    """REPORT Button -> When Simulation is done, it generate and shows report about simulation and dorm"""
    GenerateReportButton = TkinterCustomButton(text="Generate Report", corner_radius=10, width=BigB_X, height=BigB_Y,
                                               command=lambda: Generate_Report(Root, SimText), bg_color="#425b9a")
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
    MutationSwapButton = Checkbutton(Root, text="Swap Mutation", font=("Calibri", 12), variable=Mutation_Swap_Flag, bg="#425b9a", width=int(X_Size/70))
    MutationSwapButton.place(x=X_Size//1.2, y=Y_Size//2)
    CreateToolTip.CreateToolTip(MutationSwapButton, text="MutationSwap takes the begging and end of binary solution and swap them.")

    SwapMutationScale = Scale(Root, from_=0, to=10, state=ACTIVE, orient=HORIZONTAL, label=19*' '+ 'SWAP (%)', resolution=0.25,
                              troughcolor="#6580c3", bg="#425b9a", length=X_Size//7.5)
    SwapMutationScale.place(x=X_Size // 1.2, y=Y_Size // 1.8)

    MutationAddNonButton = Checkbutton(Root, text="AddNon Mutation",font=("Calibri", 12), variable=Mutation_AddNon_Flag, bg="#425b9a", width=int(X_Size/70))
    MutationAddNonButton.place(x=X_Size // 1.2, y=Y_Size // 1.49)
    CreateToolTip.CreateToolTip(MutationAddNonButton, text="MutationAddNon takes students that were not included in solution yet \nand swap them with students with the smallest achievments in the binary solution")

    AddNonMutationScale = Scale(Root, from_=0, to=10, state=ACTIVE, orient=HORIZONTAL, label=18*' '+'Add Non (%)',
                              resolution=0.25,
                              troughcolor="#6580c3", bg="#425b9a", length=X_Size // 7.5)
    AddNonMutationScale.place(x=X_Size // 1.2, y=Y_Size // 1.37)

    main_Canv.create_text(X_Size//1.11, Y_Size//2.39, text="Number of iterations", font=('Helvetica', 14), fill='#FFBBDD')
    IterationsEntry = Entry(Root, fg='#081117', width=int(X_Size / 60), font=("Calibri", 12))
    IterationsEntry.insert(0, '100')
    IterationsEntry.place(x=X_Size//1.2, y=Y_Size//2.3)
    CreateToolTip.CreateToolTip(IterationsEntry, "Insert number of iterations. Sometimes big number of iterations doesn't change anything.")

    main_Canv.create_text(X_Size // 1.11, Y_Size // 2.9, text="Number of Individuals", font=('Helvetica', 14),
                          fill='#FFBBDD')
    IndividualsEntry = Entry(Root, fg='#081117', width=int(X_Size / 60), font=("Calibri", 12))
    IndividualsEntry.insert(0, '50')
    IndividualsEntry.place(x=X_Size // 1.2, y=Y_Size // 2.7)
    CreateToolTip.CreateToolTip(IndividualsEntry, text="Insert number of Individuals there.\nToo small number of Individuals may cause in small score")

    """Selection radiobuttons"""
    MODES = [
        ("Tournament Selection", "Tournament"),
        ("Rullet Selection", "Rullet"),
        ("Rank Selection", "Rank")
    ]
    Selection = StringVar()
    Selection.set("Rullet")
    for i, (text, mode) in enumerate(MODES):
        Radiobutton(Root, text=text, variable=Selection, value=mode, width=int(X_Size//60),
                    font=("Calibri", 12), bg="#425b9a").place(x=X_Size//1.55, y=Y_Size//2.9 +i*(Y_Size//20))

    """Dorm radiobuttons"""
    MODES_Dorm = [
        ("Dorm 1", 1),
        ("Dorm 2", 2),
        ("Dorm 3", 3),
        ("Other", 4)
    ]
    DormType = IntVar()
    DormType.set(1)
    Dorm_description = ["Olimp - 120 free places, 8 floors, 6 rooms on floor",
                        "Filutek - 100 free places, 5 floors, 8 rooms on floor",
                        "Babilon - 350 free places, 14 floors, 10 rooms on floor",
                        "Dorm created in 'Generate Dataset' option "]
    for i, (text, mode) in enumerate(MODES_Dorm):
        x = Radiobutton(Root, text=text, variable=DormType, value=mode, width=int(X_Size // 60),
                    font=("Calibri", 12), bg="#756cab")
        x.place(x=X_Size // 1.55, y=Y_Size // 2 + i * (Y_Size // 20))
        CreateToolTip.CreateToolTip(x, text=Dorm_description[i])

    """ EXIT Button -> When clicked, it closes application"""
    ExitButton = TkinterCustomButton(text="EXIT", corner_radius=3, fg_color="#FF0000", bg_color="#295528", command=lambda: Exit_app(Root))
    ExitButton.place(x=X_Size//1.11, y=Y_Size//1.08)
    CreateToolTip.CreateToolTip(ExitButton, text="Click this button to quit")

    """ SAVE button"""
    SaveButton = TkinterCustomButton(text="Save", corner_radius=5,
                                     command=lambda: SaveEverything(Root, Mutation_Swap_Flag.get(), Mutation_AddNon_Flag.get(), SwapMutationScale.get(), AddNonMutationScale.get(), Selection.get(), int(IterationsEntry.get()), int(IndividualsEntry.get()), int(DormType.get()), SimText),
                                     bg_color="#aaaaFF")
    SaveButton.place(x=X_Size//1.2, y=Y_Size//10)
    CreateToolTip.CreateToolTip(SaveButton, text="Click this button to actualize parameters of simulation")
    """Simulation label"""

    Root.mainloop()


def main():
    main_screen()


if __name__ == "__main__":
    main()