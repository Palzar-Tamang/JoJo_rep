

from tkinter import *
import json

# main root object

#eqp={"EDFA":[],"Fiber":[],"Roadms":[],"Span":[],"Transceiver":[],"SI":[]}
root = Tk()

# Title of GUI rootdow
root.title('Json creator')

# Size of rootdow
root.geometry('950x800')
#logo=PhotoImage(file="gnpy.png")
#root.iconphoto(True,logo)
labelframe= LabelFrame(root, text= "Equipment Manager",fg="deep sky blue",font= ('Century 20 bold'),labelanchor= "n",bd=5,width= 600, height= 450)
labelframe.pack(expand= True, fill= BOTH)



l1= Label(labelframe, text="OLS Name",fg="deep sky blue",font= ('Helvetica 15'),)
l1.place(relx= .03, rely=0.1)

e = Entry(root, font="Helvetica 15", width=30)
e.place(relx=0.25,rely=0.135)

# def writeToJSONFile(path, filename, data):
#         json.dump(data, path,indent=4)
 
# path = './'
X=IntVar()
Y=IntVar()
    
EDFA=[]
def createamp():
    crteamp=Toplevel(root)
    crteamp.title("Create amplifiers")
    crteamp.geometry("950x680")
    #crteamp.config(background="black")

    ampname=Label(crteamp, text="type_variety",fg="SteelBlue2",font= ('Helvetica 15'))
    ampname.place(relx= .03, rely=0.1)
    ampn = Entry(crteamp, font="Helvetica 15", width=30)
    ampn.place(relx=0.3,rely=0.1)

    amptyp=Label(crteamp, text="type_def",fg="SteelBlue2",font= ('Helvetica 15'),)
    amptyp.place(relx= .03, rely=0.15)
    amptype = Entry(crteamp, font="Helvetica 15", width=30)
    amptype.place(relx=0.3,rely=0.15)
   
    ampgainmax=Label(crteamp, text="gain_flatmax",fg="SteelBlue2",font= ('Helvetica 15'))
    ampgainmax.place(relx= .03, rely=0.2)
    ampGainmax = Entry(crteamp, font="Helvetica 15", width=30)
    ampGainmax.place(relx=0.3,rely=0.2)

    ampgainmin=Label(crteamp, text="gain_min",fg="SteelBlue2",font= ('Helvetica 15'))
    ampgainmin.place(relx= .03, rely=0.25)
    ampGainmin = Entry(crteamp, font="Helvetica 15", width=30)
    ampGainmin.place(relx=0.3,rely=0.25)
    
    Maxpow=Label(crteamp, text="p_max",fg="SteelBlue2",font= ('Helvetica 15'))
    Maxpow.place(relx= .03, rely=0.3)
    maxpow = Entry(crteamp, font="Helvetica 15", width=30)
    maxpow.place(relx=0.3,rely=0.3)

    adconfig=Label(crteamp,text="advanced_config_from_json",fg="SteelBlue2",font= ('Helvetica 15'))
    adconfig.place(relx= .03, rely=0.35)
    Adconfig = Entry(crteamp, font="Helvetica 15", width=30)
    Adconfig.place(relx=0.3,rely=0.35)

    voa=Label(crteamp,text="out_voa_auto",fg="SteelBlue2",font= ('Helvetica 15'))
    voa.place(relx= .03, rely=0.4)
    Voa = Checkbutton(crteamp,text="TRUE or FALSE",font= ('Helvetica 15'),variable=X,onvalue=1,offvalue=0)
    Voa.place(relx=0.3,rely=0.4)
    VOATF=""
    if X.get()==1:
        VOATF="true"
    else:
        VOATF="false"   


    nfmin=Label(crteamp,text="nf_min",fg="SteelBlue2",font= ('Helvetica 15'))
    nfmin.place(relx= .03, rely=0.45)
    Nfmin = Entry(crteamp, font="Helvetica 15", width=30)
    Nfmin.place(relx=0.3,rely=0.45)

    nfmax=Label(crteamp,text="nf_max",fg="SteelBlue2",font= ('Helvetica 15'))
    nfmax.place(relx= .03, rely=0.50)
    Nfmax = Entry(crteamp, font="Helvetica 15", width=30)
    Nfmax.place(relx=0.3,rely=0.5)

    nf=Label(crteamp,text="nf_coef",fg="SteelBlue2",font= ('Helvetica 15'))
    nf.place(relx= .03, rely=0.55)
    Nf = Entry(crteamp, font="Helvetica 15", width=30)
    Nf.place(relx=0.3,rely=0.55)

    Afd=Label(crteamp,text="allowed_for_design",fg="SteelBlue2",font= ('Helvetica 15'))
    Afd.place(relx= .03, rely=0.65)
    afd = Checkbutton(crteamp,text="TRUE or FALSE",font= ('Helvetica 15'),variable=Y,onvalue=True,offvalue=False)
    afd.place(relx=0.3,rely=0.65)
    AFDTF=""
    if Y.get()==1:
        AFDTF="true"
    else:
        AFDTF="false"    
    
   
    def ampdict():   #Function under the createamp that stores the given parameters in a list called EDFA
        a = ampn.get()
        c = amptype.get()
        b = int(ampGainmax.get())
        d = int(ampGainmin.get())
        f = float(maxpow.get())
        g = Adconfig.get()
        #h = Voa.get()
        #i = afd.get()
        #print(a)
        #print(b) 
        #print(c)
        global data
        data = {
        "type_variety":a,
        "type_def": c , 
        "gain_flatmax":b,
        "gain_min": d,
        "p_max": f,             # e has been used for filename 
        "advanced_config_from_json":g,
        "out_voa_auto":VOATF,
        "allowed_for_design":AFDTF

         }
        EDFA.append(data)
        crteamp.destroy()
        

    ampbutton=Button(crteamp, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=ampdict)
    ampbutton.place(relx=0.62,rely=0.75)

FIBER=[{
            "type_variety": "SSMF",
            "dispersion": 1.67e-05,
            "effective_area": 83e-12,
            "pmd_coef": 1.265e-15
            },
            {
            "type_variety": "NZDF",
            "dispersion": 0.5e-05,
            "effective_area": 72e-12,
            "pmd_coef": 1.265e-15
            },
            {
            "type_variety": "LOF",
            "dispersion": 2.2e-05,
            "effective_area": 125e-12,
            "pmd_coef": 1.265e-15
            }]
#This function generates a page for the fiber parameter entry's
def createfiber():
    crtefiber=Toplevel(root)
    crtefiber.title("Create fiber")
    crtefiber.geometry("800x680")

    fibnam=Label(crtefiber, text="type_variety",fg="SteelBlue2",font= ('Helvetica 15'))
    fibnam.place(relx= .03, rely=0.1)
    fibern = Entry(crtefiber, font="Helvetica 15", width=30)
    fibern.place(relx=0.3,rely=0.1)

    dspersn=Label(crtefiber, text="dispersion",fg="SteelBlue2",font= ('Helvetica 15'),)
    dspersn.place(relx= .03, rely=0.15)
    disp = Entry(crtefiber, font="Helvetica 15", width=30)
    disp.place(relx=0.3,rely=0.15)
   
    area=Label(crtefiber, text="effective_area",fg="SteelBlue2",font= ('Helvetica 15'))
    area.place(relx= .03, rely=0.2)
    Area = Entry(crtefiber, font="Helvetica 15", width=30)
    Area.place(relx=0.3,rely=0.2)

    Pmdco=Label(crtefiber, text="pmd_coef",fg="SteelBlue2",font= ('Helvetica 15'))
    Pmdco.place(relx= .03, rely=0.25)
    PmdCo = Entry(crtefiber, font="Helvetica 15", width=30)
    PmdCo.place(relx=0.3,rely=0.25)
   
    def fiberdict(): #this function stores the fiber parameters in list called FIBER
        a = fibern.get()
        b = float(disp.get())
        c = float(Area.get())
        d = float(PmdCo.get())
        
        global dataf
        dataf = {
        "type_variety":a,
        "dispersion": b , 
        "effective_area":c,
        "pmd_coef":d    
         }
        FIBER.append(dataf)
        crtefiber.destroy()
        

    fiberbutton=Button(crtefiber, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=fiberdict)
    fiberbutton.place(relx=0.6,rely=0.7)
RamanFIBER=[{
            "type_variety": "SSMF",
            "dispersion": 1.67e-05,
            "effective_area": 83e-12,
            "pmd_coef": 1.265e-15
            }]
def createRamanfib():
    crteRamanfiber=Toplevel(root)
    crteRamanfiber.title("Create fiber")
    crteRamanfiber.geometry("800x680")

    fibnam=Label(crteRamanfiber, text="type_variety",fg="SteelBlue2",font= ('Helvetica 15'))
    fibnam.place(relx= .03, rely=0.1)
    fibern = Entry(crteRamanfiber, font="Helvetica 15", width=30)
    fibern.place(relx=0.3,rely=0.1)

    dspersn=Label(crteRamanfiber, text="dispersion",fg="SteelBlue2",font= ('Helvetica 15'),)
    dspersn.place(relx= .03, rely=0.15)
    disp = Entry(crteRamanfiber, font="Helvetica 15", width=30)
    disp.place(relx=0.3,rely=0.15)
   
    area=Label(crteRamanfiber, text="effective_area",fg="SteelBlue2",font= ('Helvetica 15'))
    area.place(relx= .03, rely=0.20)
    Area = Entry(crteRamanfiber, font="Helvetica 15", width=30)
    Area.place(relx=0.3,rely=0.2)

    Pmdco=Label(crteRamanfiber, text="pmd_coef",fg="SteelBlue2",font= ('Helvetica 15'))
    Pmdco.place(relx= .03, rely=0.25)
    PmdCo = Entry(crteRamanfiber, font="Helvetica 15", width=30)
    PmdCo.place(relx=0.3,rely=0.25)
   
    def Ramanfiberdict(): #this function stores the fiber parameters in list called FIBER
        a = fibern.get()
        b = float(disp.get())
        c = float(Area.get())
        d = float(PmdCo.get())
        #print(a)
        #print(b)
        #print(c)
        global dataRf
        dataRf = {
        "type_variety":a,
        "dispersion": b , 
        "effective_area":c,
        "pmd_coef":d    
         }
        RamanFIBER.append(dataRf)
        crteRamanfiber.destroy()
        

    Rfiberbutton=Button(crteRamanfiber, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=Ramanfiberdict)
    Rfiberbutton.place(relx=0.6,rely=0.7)

SPAN=[]
def createspan():
    crtespan=Toplevel(root)
    crtespan.title("Create Span")
    crtespan.geometry("800x680")
    
    powm=Label(crtespan, text="power_mode",fg="SteelBlue2",font= ('Helvetica 15'))
    powm.place(relx= .03, rely=0.1)
    powme = Entry(crtespan, font="Helvetica 15", width=30)
    powme.place(relx=0.3,rely=0.1)

    dpr=Label(crtespan, text="delta_power_range_db",fg="SteelBlue2",font= ('Helvetica 15'))
    dpr.place(relx= .03, rely=0.15)
    dpre = Entry(crtespan, font="Helvetica 15", width=30)
    dpre.place(relx=0.3,rely=0.15)

    mfl=Label(crtespan, text="max_fiber_lineic_loss_for_raman",fg="SteelBlue2",font= ('Helvetica 15'))
    mfl.place(relx= .03, rely=0.2)
    mfle = Entry(crtespan, font="Helvetica 15", width=30)
    mfle.place(relx=0.3,rely=0.2)

    teg=Label(crtespan, text="target_extended_gain",fg="SteelBlue2",font= ('Helvetica 15'))
    teg.place(relx= .03, rely=0.25)
    tege = Entry(crtespan, font="Helvetica 15", width=30)
    tege.place(relx=0.3,rely=0.25)

    ml=Label(crtespan, text="max_length",fg="SteelBlue2",font= ('Helvetica 15'))
    ml.place(relx= .03, rely=0.3)
    mle = Entry(crtespan, font="Helvetica 15", width=30)
    mle.place(relx=0.3,rely=0.3)

    mloss=Label(crtespan, text="max_loss",fg="SteelBlue2",font= ('Helvetica 15'))
    mloss.place(relx= .03, rely=0.35)
    mlosse = Entry(crtespan, font="Helvetica 15", width=30)
    mlosse.place(relx=0.3,rely=0.35)

    padd=Label(crtespan, text="padding",fg="SteelBlue2",font= ('Helvetica 15'))
    padd.place(relx= .03, rely=0.4)
    padde = Entry(crtespan, font="Helvetica 15", width=30)
    padde.place(relx=0.3,rely=0.4)

    eol=Label(crtespan, text="EOL",fg="SteelBlue2",font= ('Helvetica 15'))
    eol.place(relx= .03, rely=0.45)
    eole = Entry(crtespan, font="Helvetica 15", width=30)
    eole.place(relx=0.3,rely=0.45)

    conin=Label(crtespan, text="conn_in",fg="SteelBlue2",font= ('Helvetica 15'))
    conin.place(relx= .03, rely=0.5)
    conine = Entry(crtespan, font="Helvetica 15", width=30)
    conine.place(relx=0.3,rely=0.5)

    conout=Label(crtespan, text="conn_out",fg="SteelBlue2",font= ('Helvetica 15'))
    conout.place(relx= .03, rely=0.55)
    conoute = Entry(crtespan, font="Helvetica 15", width=30)
    conoute.place(relx=0.3,rely=0.55)

    def Spandict(): #this function stores the fiber parameters in list called FIBER
        a = powme.get()
        b = list(dpre.get())
        c = float(mfle.get())
        d = float(tege.get())
        f = float(mle.get())
        #length units=km
        g = float(mlosse.get())
        h = float(padde.get())
        i = float(eole.get())
        j = float(conine.get())
        k = float(conoute.get())

        global dataSpan
        dataSpan = {
        "power_mode":a,
        "delta_power_range_db": b,
        "max_fiber_lineic_loss_for_raman": c,
        "target_extended_gain": d,
        "max_length": f ,
        "length_units": "km",
        "max_loss": g,
        "padding": h,
        "EOL": i,
        "con_in": j,
        "con_out": k 
         }
        SPAN.append(dataSpan)
        crtespan.destroy()
        

    Spanbutton=Button(crtespan, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=Spandict)
    Spanbutton.place(relx=0.6,rely=0.7)




ROADM=[]
def createroadm():
    crterdm=Toplevel(root)
    crterdm.title("Create Roadm")
    crterdm.geometry("800x680")

    tar=Label(crterdm, text="target_pch_out_db",fg="SteelBlue2",font= ('Helvetica 15'))
    tar.place(relx= .03, rely=0.1)
    tare = Entry(crterdm, font="Helvetica 15", width=30)
    tare.place(relx=0.3,rely=0.1)

    ado=Label(crterdm, text="add_drop_osnr",fg="SteelBlue2",font= ('Helvetica 15'))
    ado.place(relx= .03, rely=0.15)
    adoe = Entry(crterdm, font="Helvetica 15", width=30)
    adoe.place(relx=0.3,rely=0.15)

    pmd=Label(crterdm, text="pmd",fg="SteelBlue2",font= ('Helvetica 15'))
    pmd.place(relx= .03, rely=0.2)
    pmde = Entry(crterdm, font="Helvetica 15", width=30)
    pmde.place(relx=0.3,rely=0.2)

    pdl=Label(crterdm, text="pml",fg="SteelBlue2",font= ('Helvetica 15'))
    pdl.place(relx= .03, rely=0.25)
    pde = Entry(crterdm, font="Helvetica 15", width=30)
    pde.place(relx=0.3,rely=0.25)

    def Roadmdict(): #this function stores the fiber parameters in list called FIBER
        a = float(tare.get())
        b = float(adoe.get())
        c = float(pmde.get())
        d = float(pde.get())
        
        global datarRoadm
        dataRoadm = {
        "target_pch_out_db":a,
        "add_drop_osnr": b , 
        "pmd":c,
        "pdl":d    
         }
        ROADM.append(dataRoadm)
        crterdm.destroy()
        

    Roadmbutton=Button(crterdm, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=Roadmdict)
    Roadmbutton.place(relx=0.6,rely=0.5)

    #def rdmdict():
SI=[]
def sysinput():
    SIp=Toplevel(root)
    SIp.title("SI ")
    SIp.geometry("800x680")

    fmin=Label(SIp, text="f_min",fg="SteelBlue2",font= ('Helvetica 15'))
    fmin.place(relx= .03, rely=0.1)
    Fmin = Entry(SIp, font="Helvetica 15", width=30)
    Fmin.place(relx=0.3,rely=0.1)

    baudr=Label(SIp, text="baud_rate",fg="SteelBlue2",font= ('Helvetica 15'))
    baudr.place(relx=0.03,rely=0.15)
    Baudr=Entry(SIp, font="Helvetica 15", width=30)
    Baudr.place(relx=0.3,rely=0.15)

    fmax=Label(SIp, text="f_max",fg="SteelBlue2",font= ('Helvetica 15'))
    fmax.place(relx= .03, rely=0.2)
    Fmax = Entry(SIp, font="Helvetica 15", width=30)
    Fmax.place(relx=0.3,rely=0.2)

    spacing=Label(SIp, text="spacing",fg="SteelBlue2",font= ('Helvetica 15'))
    spacing.place(relx= .03, rely=0.25)
    space = Entry(SIp, font="Helvetica 15", width=30)
    space.place(relx=0.3,rely=0.25)

    power=Label(SIp, text="power(dBm)",fg="SteelBlue2",font= ('Helvetica 15'))
    power.place(relx= .03, rely=0.3)
    powr = Entry(SIp, font="Helvetica 15", width=30)
    powr.place(relx=0.3,rely=0.3)

    powerst=Label(SIp, text="start power",fg="SteelBlue2",font= ('Helvetica 15'))
    powerst.place(relx= .03, rely=0.35)
    pose = Entry(SIp, font="Helvetica 15", width=30)
    pose.place(relx=0.3,rely=0.35)

    powered=Label(SIp, text="end_power",fg="SteelBlue2",font= ('Helvetica 15'))
    powered.place(relx= .03, rely=0.4)
    poee = Entry(SIp, font="Helvetica 15", width=30)
    poee.place(relx=0.3,rely=0.4)

    powstep=Label(SIp, text="power step size",fg="SteelBlue2",font= ('Helvetica 15'))
    powstep.place(relx= .03, rely=0.45)
    poste = Entry(SIp, font="Helvetica 15", width=30)
    poste.place(relx=0.3,rely=0.45)

    roll=Label(SIp, text="roll_off",fg="SteelBlue2",font= ('Helvetica 15'))
    roll.place(relx= .03, rely=0.5)
    rolle = Entry(SIp, font="Helvetica 15", width=30)
    rolle.place(relx=0.3,rely=0.5)

    tosnr=Label(SIp, text="tx_osnr",fg="SteelBlue2",font= ('Helvetica 15'))
    tosnr.place(relx= .03, rely=0.55)
    tosnre = Entry(SIp, font="Helvetica 15", width=30)
    tosnre.place(relx=0.3,rely=0.55)

    sysm=Label(SIp, text="sys_margins",fg="SteelBlue2",font= ('Helvetica 15'))
    sysm.place(relx= .03, rely=0.6)
    sysme = Entry(SIp, font="Helvetica 15", width=30)
    sysme.place(relx=0.3,rely=0.6)

    def SIdict(): #this function stores the fiber parameters in list called FIBER
        a = float(Fmin.get())
        b = float(Baudr.get())
        c = float(Fmax.get())
        d = float(space.get())
        f = float(powr.get())
        p = [float(pose.get()),float(poee.get()),float(poste.get())]
        g = float(rolle.get())
        h = float(tosnre.get())
        i = int(sysme.get())
        global dataSI
        dataSI = {
        "f_min": a,
        "baud_rate": b,
        "f_max": c,
        "spacing": d,
        "power_dbm": f,
        "power_range_db": p,
        "roll_off": g,
        "tx_osnr": h,
        "sys_margins": i  
         }
        SI.append(dataSI)
        SIp.destroy()
    SIbutton=Button(SIp, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=SIdict)
    SIbutton.place(relx=0.6,rely=0.75)    

MODE=[]
def Mode():
    mode=Toplevel(root)
    mode.title("MODE")
    mode.geometry("800x680")

    format=Label(mode,text="format",fg="SteelBlue2",font= ('Helvetica 15'))
    format.place(relx= .03, rely=0.1)
    formate= Entry(mode, font="Helvetica 15", width=30)
    formate.place(relx=0.3,rely=0.1)

    baudr=Label(mode,text="baud_rate",fg="SteelBlue2",font= ('Helvetica 15'))
    baudr.place(relx= .03, rely=0.15)
    baude= Entry(mode, font="Helvetica 15", width=30)
    baude.place(relx=0.3,rely=0.15)

    osnr=Label(mode,text="OSNR",fg="SteelBlue2",font= ('Helvetica 15'))
    osnr.place(relx= .03, rely=0.2)
    osnre= Entry(mode, font="Helvetica 15", width=30)
    osnre.place(relx=0.3,rely=0.2)

    bitr=Label(mode,text="bit_rate",fg="SteelBlue2",font= ('Helvetica 15'))
    bitr.place(relx= .03, rely=0.25)
    bitre= Entry(mode, font="Helvetica 15", width=30)
    bitre.place(relx=0.3,rely=0.25)

    rollof=Label(mode,text="roll_off",fg="SteelBlue2",font= ('Helvetica 15'))
    rollof.place(relx= .03, rely=0.3)
    rolle= Entry(mode, font="Helvetica 15", width=30)
    rolle.place(relx=0.3,rely=0.3)

    txosnr=Label(mode,text="tx_osnr",fg="SteelBlue2",font= ('Helvetica 15'))
    txosnr.place(relx= .03, rely=0.35)
    txosnre= Entry(mode, font="Helvetica 15", width=30)
    txosnre.place(relx=0.3,rely=0.35)

    mins=Label(mode,text="min_Spacing",fg="SteelBlue2",font= ('Helvetica 15'))
    mins.place(relx= .03, rely=0.4)
    minse= Entry(mode, font="Helvetica 15", width=30)
    minse.place(relx=0.3,rely=0.4)

    cost=Label(mode,text="cost",fg="SteelBlue2",font= ('Helvetica 15'))
    cost.place(relx= .03, rely=0.45)
    coste= Entry(mode, font="Helvetica 15", width=30)
    coste.place(relx=0.3,rely=0.45)

    def modedict():
        a = formate.get()
        b = float(baude.get())
        c = float(osnre.get())
        d= float(bitre.get())
        f = float(rolle.get())
        g = float(txosnre.get())
        h = float(minse.get())
        i = int(coste.get())
        global datamode
        datamode = {
        "format": a,
        "baud_rate": b,
        "OSNR": c,
        "bit_rate": d,
        "roll_off": f,
        "tx_osnr": g,
        "min_spacing": h,
        "cost":i
    }
        MODE.append(datamode)
        mode.destroy()
    modebutton=Button(mode, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=modedict)
    modebutton.place(relx=0.6,rely=0.6)  

    
TRANSCEIVER=[]
def createtrx():
    trx=Toplevel(root)
    trx.title("SI ")
    trx.geometry("800x680")

    typvar=Label(trx, text="type_variety",fg="SteelBlue2",font= ('Helvetica 15'))
    typvar.place(relx= .03, rely=0.1)
    typv = Entry(trx, font="Helvetica 15", width=30)
    typv.place(relx=0.3,rely=0.1)

    fmin=Label(trx, text="f_min",fg="SteelBlue2",font= ('Helvetica 15'))
    fmin.place(relx= .03, rely=0.15)
    Fmin = Entry(trx, font="Helvetica 15", width=30)
    Fmin.place(relx=0.3,rely=0.15)

    fmax=Label(trx, text="f_max",fg="SteelBlue2",font= ('Helvetica 15'))
    fmax.place(relx= .03, rely=0.2)
    Fmax = Entry(trx, font="Helvetica 15", width=30)
    Fmax.place(relx=0.3,rely=0.2)
    
      
    modebut=Button(trx, text="mode",font= ('Helvetica 15'),command=Mode)
    modebut.place(relx=0.03,rely=0.3)
    def trxdict(): #this function stores the fiber parameters in list called TRANSCEIVER
        a=typv.get()
        b=float(Fmin.get())
        c=float(Fmax.get())
        
        global datatrx
        datatrx = {
            
            "type_variety": a,
            "frequency":{
                        "min": b,
                        "max": c
                        },
            "mode":MODE
        
         }
        TRANSCEIVER.append(datatrx)
        trx.destroy()
    
    trxbutton=Button(trx, text="OK",bg="green3",font= ('Helvetica 15'),height=1,width=8,command=trxdict)
    trxbutton.place(relx=0.6,rely=0.6) 






   




#transceiver
def crtjson():
     Eqp={"EDFA":EDFA,"Fiber":FIBER,"RamanFiber":RamanFIBER,"Span":SPAN,"Roadm":ROADM,"SI":SI,"Transceiver":TRANSCEIVER}
     filename=e.get()
     print(filename)
     json_object = json.dumps(Eqp, indent=4)
     # Writing to sample.json
     with open(f"{filename}.json", "w") as outfile:
        outfile.write(json_object)
     root.quit()    

        
        
amp=Button(root,text="Amplifiers",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createamp)
amp.place(relx=0.03,rely=0.22)

fiber=Button(root,text="Fiber",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createfiber)
fiber.place(relx=0.03,rely=0.28)

raman=Button(root,text="Raman_fiber",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createRamanfib)
raman.place(relx=0.03,rely=0.34)

span=Button(root,text="Span",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createspan)
span.place(relx=0.03,rely=0.40)

roadm=Button(root,text="Roadm",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createroadm)
roadm.place(relx=0.03,rely=0.46)

si=Button(root,text="SI",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=sysinput)
si.place(relx=0.03,rely=0.52)

transceiver=Button(root,text="Transceiver",fg="SteelBlue1",bg="blue4",font= ('Helvetica 15'),height=1,width=10,command=createtrx)
transceiver.place(relx=0.03,rely=0.58)



createjson=Button(root, text="Create json",font= ('Helvetica 15'),command=crtjson)
createjson.place(relx=0.75,rely=0.135)
root.mainloop()

