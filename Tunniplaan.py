from tkinter import*

def kirjeldus():
	pass

aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x500")
Ep=Label(aken,text="Esmaspäev",relief="solid",font="Calibri 30").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
Ep=Label(aken,text="Teisipäev",relief="solid",font="Calibri 30").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Ep=Label(aken,text="Kolmapäev",relief="solid",font="Calibri 30").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Ep=Label(aken,text="Neljapäev",relief="solid",font="Calibri 30").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Ep=Label(aken,text="Reede",relief="solid",font="Calibri 30").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)


t0=Label(aken,text="0",relief="solid",font="Calibri 26").grid(row=0,column=1,sticky=N+S+W+E)
t0=Label(aken,text="1",relief="solid",font="Calibri 26").grid(row=0,column=2,sticky=N+S+W+E)
t0=Label(aken,text="2",relief="solid",font="Calibri 26").grid(row=0,column=3,sticky=N+S+W+E)
t0=Label(aken,text="3",relief="solid",font="Calibri 26").grid(row=0,column=4,sticky=N+S+W+E)
t0=Label(aken,text="4",relief="solid",font="Calibri 26").grid(row=0,column=5,sticky=N+S+W+E)
t0=Label(aken,text="5",relief="solid",font="Calibri 26").grid(row=0,column=6,sticky=N+S+W+E)
t0=Label(aken,text="6",relief="solid",font="Calibri 26").grid(row=0,column=7,sticky=N+S+W+E)
t0=Label(aken,text="7",relief="solid",font="Calibri 26").grid(row=0,column=8,sticky=N+S+W+E)
t0=Label(aken,text="8",relief="solid",font="Calibri 26").grid(row=0,column=9,sticky=N+S+W+E)
t0=Label(aken,text="9",relief="solid",font="Calibri 26").grid(row=0,column=10,sticky=N+S+W+E)
t0=Label(aken,text="10",relief="solid",font="Calibri 26").grid(row=0,column=11,sticky=N+S+W+E)

#Esmaspäev
p1=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
p3=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
p4=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
p5=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
p27=Button(text="Rühma juhatuja tund", font="Calibri 26",bg="skyblue").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

#Teisipäev
p6=Button(text="Inglise keel", font="Calibri 26",bg="floralwhite").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
p7=Button(text="Inglise keel", font="Calibri 26",bg="mediumorchid").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
p8=Button(text="Operatsioonisüsteemide alused", font="Calibri 26",bg="darkorchid").grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p10=Button(text="Kehaline kasvatus", font="Calibri 26",bg="palevioletred").grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
p11=Button(text="Eesti keel", font="Calibri 26",bg="mediumpurple").grid(row=3,column=9,sticky=N+S+W+E)
p12=Button(text="Eesti keel", font="Calibri 26",bg="darkgrey").grid(row=4,column=9,sticky=N+S+W+E)
p13=Button(text="Ajalugu", font="Calibri 26",bg="khaki").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

#Kolmapäev
p14=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
p15=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
p16=Button(text="Multimeedia", font="Calibri 26",bg="cornflowerblue").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
p17=Button(text="Programmeerimise alused", font="Calibri 26",bg="skyblue").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
p18=Button(text="Kunstiained", font="Calibri 26",bg="orchid").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Neljapäev
p19=Button(text="Andmebaasisüsteemide alused", font="Calibri 26",bg="salmon").grid(row=7,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
p20=Button(text="Ajalugu", font="Calibri 26",bg="khaki").grid(row=7,column=6,rowspan=2,sticky=N+S+W+E)
p21=Button(text="Eesti keel", font="Calibri 26",bg="mediumpurple").grid(row=7,column=7,sticky=N+S+W+E)
p22=Button(text="Eesti keel", font="Calibri 26",bg="darkgrey").grid(row=8,column=7,sticky=N+S+W+E)

#Reede
p23=Button(text="Vene keel", font="Calibri 26",bg="greenyellow").grid(row=9,column=3,columnspan=2,rowspan=2,sticky=N+S+W+E)
p24=Button(text="Matemaatika", font="Calibri 26",bg="lightpink").grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
p25=Button(text="Suhtlemine ja kliienditeenindus", font="Calibri 26",bg="mediumslateblue").grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
p26=Button(text="Ajalugu", font="Calibri 26",bg="khaki").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)

aken.mainloop()

#Iljaloh)
