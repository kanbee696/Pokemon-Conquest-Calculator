import tkinter as tk
from math import *
from tkinter import ttk

"""--- POKEMON DATA PARSING ---"""

DataDict = {}
DataFile = open("PokemonData.xml","r")

for line in DataFile:
    line2 = str.split(line,("\n"))
    line3 = str.split(line2[0],(";"))
    DataDict[line3[0]] = line3[1:]
PokemonList = list(DataDict.keys())

"""--- CALCULATION FUNCTIONS ---"""

#Calculates one stat from base stats
def Calculate_One_Stat(Base_Stat,IV,Link,Energy):
    Stat = trunc(trunc((Base_Stat+IV)*trunc(Link)/100)*Energy/100)
    return(Stat)

#Calculates stat spread for all possible IVs and returns the min and max IVs corresponding to inputted values   
def Calculate_IVs(Pokemon_StatList,Base_StatList,Link,Energy):
    MinList=[-1,-1,-1,-1]
    MaxList=[-1,-1,-1,-1]
    
    for IV in range(32):
        for i in range(4):
            Stat = Calculate_One_Stat(int(Base_StatList[i]),IV,float(Link),Energy)
            if (IV==0 and Stat>int(Pokemon_StatList[i])) or (IV==31 and Stat<int(Pokemon_StatList[i])):
                MinList[i]=-1000
                MaxList[i]=1000
            if Stat==int(Pokemon_StatList[i]) and MinList[i]==-1:
                MinList[i]=IV
                MaxList[i]=IV
            if Stat==int(Pokemon_StatList[i]) and MaxList[i]<IV:
                MaxList[i]=IV
    return(MinList,MaxList)

#Calculates a stat spread for one possible set of IVs and returns the corresponding stat values
def Calculate_Stats(IV_List,Base_StatList,Link,Energy):
    Pokemon_StatList=[]
    for i in range(4):
        if int(IV_List[i])<0 or int(IV_List[i])>31:
            Stat="Err"
        else:
            Stat=Calculate_One_Stat(int(Base_StatList[i]),int(IV_List[i]),float(Link),Energy)
        Pokemon_StatList.append(Stat)
    return(Pokemon_StatList)
        

"""--- PROGRAM EXECUTION FUNCTION ---"""

def Execute_IV_Calc():
    Cur_BaseStatList = DataDict[IVCalc_PokemonCurName.get()]
    Cur_StatList = [IVCalc_PokemonHP.get(),IVCalc_PokemonAtk.get(),IVCalc_PokemonDef.get(),IVCalc_PokemonSpe.get()]
    [CurLink,CurEnergy] = [IVCalc_PokemonLink.get(),IVCalc_Energy.get()]
    CurMinList,CurMaxList = Calculate_IVs(Cur_StatList,Cur_BaseStatList,CurLink,CurEnergy)
    StatText=["HP:       ","Atk:       ","Def:       ","Spe:       "]
    selection = ""
    for i in range(4):
        if CurMinList[i] == -1000 or CurMaxList[i] == 1000:
            selection += StatText[i]+"Err\n"
        elif CurMinList[i] == CurMaxList[i]:
            selection += StatText[i]+str(CurMinList[i])+"\n"
        else:
            selection += StatText[i]+str(CurMinList[i])+"-"+str(CurMaxList[i])+"\n"
    IVLabel.config(text=selection[0:len(selection)-1])
    
def Execute_Stat_Calc():
    Cur_BaseStatList = DataDict[StatsCalc_PokemonCurName.get()]
    Cur_IVList = [StatsCalc_PokemonHP.get(),StatsCalc_PokemonAtk.get(),StatsCalc_PokemonDef.get(),StatsCalc_PokemonSpe.get()]
    [CurLink,CurEnergy] = [StatsCalc_PokemonLink.get(),StatsCalc_Energy.get()]
    Cur_StatList = Calculate_Stats(Cur_IVList,Cur_BaseStatList,CurLink,CurEnergy)
    StatText=["HP:       ","Atk:       ","Def:       ","Spe:       "]
    selection = ""
    for i in range(4):
        selection +=StatText[i]+str(Cur_StatList[i])+"\n"
    StatsLabel.config(text=selection[0:len(selection)-1])
    
"""--- SEARCHES AND FILTERS POKEMON BY NAME ---"""

def IVCalc_NameFilter(event):
    value = event.widget.get()
    if value == "":
        IVCalc_PokemonNameMenu['values'] = PokemonList
    else:
        MatchingNames = []
        for Name in PokemonList:
            if value.lower() == Name.lower()[0:len(value.lower())]:
                MatchingNames.append(Name)
        IVCalc_PokemonNameMenu['values'] = MatchingNames

def StatsCalc_NameFilter(event):
    value = event.widget.get()
    if value == "":
        StatsCalc_PokemonNameMenu['values'] = PokemonList
    else:
        MatchingNames = []
        for Name in PokemonList:
            if value.lower() == Name.lower()[0:len(value.lower())]:
                MatchingNames.append(Name)
        StatsCalc_PokemonNameMenu['values'] = MatchingNames
        
"""--- MAIN WINDOW AND GLOBAL FRAMES ---"""

Calculator=tk.Tk()
Calculator.title("Pokémon Conquest Calculators")
Calculator.geometry("510x650")

IVCalc_GlobalFrame=tk.LabelFrame(Calculator,text="IV Calculator",width=490,height=280)
IVCalc_GlobalFrame.place(x=10,y=10)
StatsCalc_GlobalFrame=tk.LabelFrame(Calculator,text="Stat Calculator",width=490,height=280)
StatsCalc_GlobalFrame.place(x=10,y=330)

"""--- IV CALCULATOR POKEMON NAME DROPDOWN MENU ---"""

IVCalc_LabelPoke = tk.Label(IVCalc_GlobalFrame,text="Pokémon")
IVCalc_LabelPoke.place(x=300,y=70)
IVCalc_PokemonCurName = tk.StringVar(IVCalc_GlobalFrame)
IVCalc_PokemonNameMenu = ttk.Combobox(IVCalc_GlobalFrame,textvariable=IVCalc_PokemonCurName,values=PokemonList,width=12)
IVCalc_PokemonNameMenu.set("(Type Name)")
IVCalc_PokemonNameMenu.place(x=370,y=70)
IVCalc_PokemonNameMenu.bind("<KeyRelease>",IVCalc_NameFilter)

"""--- IV CALCULATOR FRAMES ---"""

IVCalc_StatFrame=tk.LabelFrame(IVCalc_GlobalFrame,text="Stats",width=125,height=225)
IVCalc_StatFrame.place(x=10,y=25)
IVCalc_EnergyFrame=tk.LabelFrame(IVCalc_GlobalFrame,text="Energy",width=125,height=225)
IVCalc_EnergyFrame.place(x=150,y=25)
IVCalc_IVFrame=tk.LabelFrame(IVCalc_GlobalFrame,text="Pokémon IVs",width=170,height=100)
IVCalc_IVFrame.place(x=300,y=110)

"""--- IV CALCULATOR POKEMON STATS ENTRIES --"""

IVCalc_HPLabel= tk.Label(IVCalc_StatFrame,text="HP")
IVCalc_PokemonHP = tk.Entry(IVCalc_StatFrame,bd=1,width=5)
IVCalc_HPLabel.place(x=10,y=30)
IVCalc_PokemonHP.place(x=50,y=30)
IVCalc_AtkLabel= tk.Label(IVCalc_StatFrame,text="Atk")
IVCalc_PokemonAtk = tk.Entry(IVCalc_StatFrame,bd=1,width=5)
IVCalc_AtkLabel.place(x=10,y=70)
IVCalc_PokemonAtk.place(x=50,y=70)
IVCalc_DefLabel= tk.Label(IVCalc_StatFrame,text="Def")
IVCalc_PokemonDef = tk.Entry(IVCalc_StatFrame,bd=1,width=5)
IVCalc_DefLabel.place(x=10,y=110)
IVCalc_PokemonDef.place(x=50,y=110)
IVCalc_SpeLabel= tk.Label(IVCalc_StatFrame,text="Spe")
IVCalc_PokemonSpe = tk.Entry(IVCalc_StatFrame,bd=1,width=5)
IVCalc_SpeLabel.place(x=10,y=150)
IVCalc_PokemonSpe.place(x=50,y=150)

"""--- IV CALCULATOR POKEMON LINK ENTRY ---"""

IVCalc_LinkLabel= tk.Label(IVCalc_GlobalFrame,text="Link (%)")
IVCalc_PokemonLink = tk.Entry(IVCalc_GlobalFrame,bd=1,width=5)
IVCalc_LinkLabel.place(x=300,y=30)
IVCalc_PokemonLink.place(x=370,y=30)

"""--- IV CALCULATOR ENERGY SELECTION BUTTONS ---"""

IVCalc_Energy=tk.IntVar()
IVCalc_Energy_VeryHigh = tk.Radiobutton(IVCalc_EnergyFrame,text="Very High",variable=IVCalc_Energy,value=110)
IVCalc_Energy_High = tk.Radiobutton(IVCalc_EnergyFrame,text="High",variable=IVCalc_Energy,value=105)
IVCalc_Energy_Medium = tk.Radiobutton(IVCalc_EnergyFrame,text="Medium",variable=IVCalc_Energy,value=100)
IVCalc_Energy_Low = tk.Radiobutton(IVCalc_EnergyFrame,text="Low",variable=IVCalc_Energy,value=95)
IVCalc_Energy_VeryLow = tk.Radiobutton(IVCalc_EnergyFrame,text="Very Low",variable=IVCalc_Energy,value=90)

IVCalc_Energy_VeryLow.place(x=25,y=170)
IVCalc_Energy_Low.place(x=25,y=130)
IVCalc_Energy_Medium.place(x=25,y=90)
IVCalc_Energy_High.place(x=25,y=50)
IVCalc_Energy_VeryHigh.place(x=25,y=10)

"""--- IV CALCULATOR RESULT COMMANDS ---"""

IV_Calculate=tk.Button(IVCalc_GlobalFrame,text="Calculate IVs",command=Execute_IV_Calc)
IV_Calculate.place(x=300,y=225)

#Empty text label to display results
IVLabel = tk.Label(IVCalc_IVFrame,anchor="nw",justify="left") 
IVLabel.place(x=50,y=0)

"""--- STATS CALCULATOR POKEMON NAME DROPDOWN MENU ---"""

StatsCalc_LabelPoke = tk.Label(StatsCalc_GlobalFrame,text="Pokémon")
StatsCalc_LabelPoke.place(x=300,y=70)
StatsCalc_PokemonCurName = tk.StringVar(StatsCalc_GlobalFrame)
StatsCalc_PokemonNameMenu = ttk.Combobox(StatsCalc_GlobalFrame,textvariable=StatsCalc_PokemonCurName,values=PokemonList,width=12)
StatsCalc_PokemonNameMenu.set("(Type Name)")
StatsCalc_PokemonNameMenu.place(x=370,y=70)
StatsCalc_PokemonNameMenu.bind("<KeyRelease>",StatsCalc_NameFilter)

"""--- STATS CALCULATOR FRAMES ---"""

StatsCalc_IVFrame=tk.LabelFrame(StatsCalc_GlobalFrame,text="IVs",width=125,height=225)
StatsCalc_IVFrame.place(x=10,y=25)
StatsCalc_EnergyFrame=tk.LabelFrame(StatsCalc_GlobalFrame,text="Energy",width=125,height=225)
StatsCalc_EnergyFrame.place(x=150,y=25)
StatsCalc_StatsFrame=tk.LabelFrame(StatsCalc_GlobalFrame,text="Pokémon Stats",width=170,height=100)
StatsCalc_StatsFrame.place(x=300,y=110)

"""--- IV CALCULATOR POKEMON STATS ENTRIES --"""

StatsCalc_HPLabel= tk.Label(StatsCalc_IVFrame,text="HP")
StatsCalc_PokemonHP = tk.Entry(StatsCalc_IVFrame,bd=1,width=5)
StatsCalc_HPLabel.place(x=10,y=30)
StatsCalc_PokemonHP.place(x=50,y=30)
StatsCalc_AtkLabel= tk.Label(StatsCalc_IVFrame,text="Atk")
StatsCalc_PokemonAtk = tk.Entry(StatsCalc_IVFrame,bd=1,width=5)
StatsCalc_AtkLabel.place(x=10,y=70)
StatsCalc_PokemonAtk.place(x=50,y=70)
StatsCalc_DefLabel= tk.Label(StatsCalc_IVFrame,text="Def")
StatsCalc_PokemonDef = tk.Entry(StatsCalc_IVFrame,bd=1,width=5)
StatsCalc_DefLabel.place(x=10,y=110)
StatsCalc_PokemonDef.place(x=50,y=110)
StatsCalc_SpeLabel= tk.Label(StatsCalc_IVFrame,text="Spe")
StatsCalc_PokemonSpe = tk.Entry(StatsCalc_IVFrame,bd=1,width=5)
StatsCalc_SpeLabel.place(x=10,y=150)
StatsCalc_PokemonSpe.place(x=50,y=150)

"""--- IV CALCULATOR POKEMON LINK ENTRY ---"""

StatsCalc_LinkLabel= tk.Label(StatsCalc_GlobalFrame,text="Link (%)")
StatsCalc_PokemonLink = tk.Entry(StatsCalc_GlobalFrame,bd=1,width=5)
StatsCalc_LinkLabel.place(x=300,y=30)
StatsCalc_PokemonLink.place(x=370,y=30)

"""--- IV CALCULATOR ENERGY SELECTION BUTTONS ---"""

StatsCalc_Energy=tk.IntVar()
StatsCalc_Energy_VeryHigh = tk.Radiobutton(StatsCalc_EnergyFrame,text="Very High",variable=StatsCalc_Energy,value=110)
StatsCalc_Energy_High = tk.Radiobutton(StatsCalc_EnergyFrame,text="High",variable=StatsCalc_Energy,value=105)
StatsCalc_Energy_Medium = tk.Radiobutton(StatsCalc_EnergyFrame,text="Medium",variable=StatsCalc_Energy,value=100)
StatsCalc_Energy_Low = tk.Radiobutton(StatsCalc_EnergyFrame,text="Low",variable=StatsCalc_Energy,value=95)
StatsCalc_Energy_VeryLow = tk.Radiobutton(StatsCalc_EnergyFrame,text="Very Low",variable=StatsCalc_Energy,value=90)

StatsCalc_Energy_VeryLow.place(x=25,y=170)
StatsCalc_Energy_Low.place(x=25,y=130)
StatsCalc_Energy_Medium.place(x=25,y=90)
StatsCalc_Energy_High.place(x=25,y=50)
StatsCalc_Energy_VeryHigh.place(x=25,y=10)

"""--- IV CALCULATOR RESULT COMMANDS ---"""

Stats_Calculate=tk.Button(StatsCalc_GlobalFrame,text="Calculate Stats",command=Execute_Stat_Calc)
Stats_Calculate.place(x=300,y=225)

#Empty text label to display results
StatsLabel = tk.Label(StatsCalc_StatsFrame,anchor="nw",justify="left") 
StatsLabel.place(x=50,y=0)

Calculator.mainloop()