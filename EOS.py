from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import Button
import pandas as pd
from tkinter import Canvas
    
class EOS:

    def __init__(self, root):
        self.wind = root
        self.wind.title("EOS - Magnetics Reconnection")
        self.wind.geometry ("600x600")

        imagen_original = Image.open("C:\EOS PROYECT\mr.jpg")
        imagen_convertida = ImageTk.PhotoImage(imagen_original)

        imagen_original2 = Image.open("C:\EOS PROYECT\solsolecito.jpg")
        imagen_convertida2 = ImageTk.PhotoImage(imagen_original2)

        self.image = PhotoImage(file="C:\EOS PROYECT\image0.png")
        self.image_label = tk.Label(self.wind, image=self.image)
        self.image_label.place(x=0, y=0)

        # Crear un frame superior para otros elementos (por ejemplo, encabezado)
        self.top_frame = tk.Frame(self.wind)
        self.top_frame.pack(fill='x')  # Ajustar a lo ancho de la ventana

        # Colocar el Notebook debajo del frame superior
        self.notebook = ttk.Notebook(self.wind)
        self.notebook.pack(fill='both', expand='yes', pady=100)  # Añadir espacio en la parte superior
        
        # Crear pestañas
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)
        self.tab3 = tk.Frame(self.notebook)
        self.tab4 = tk.Frame(self.notebook)
        self.tab5 = tk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Introduction')
        self.notebook.add(self.tab2, text='Satellites')
        self.notebook.add(self.tab3, text= "Information")
        self.notebook.add(self.tab4, text ="Calculation")
        self.notebook.add(self.tab5, text ="Recommendations")

        
        # Crear el LabelFrame dentro de la pestaña "Introduction"
        frame1 = LabelFrame(self.tab1, text="What is this program about?", font=('Impact', 14), fg='midnight blue')
        frame1.pack(fill="both", expand="yes", padx=20, pady=20)
        label = Label(frame1, text="We created this program in order to raise awareness to the general public abot the magnetic")  # Crea el widget Label en el frame1
        label.place(x=20, y=12)  # Posiciona el widget Label en el frame1
        label1 = Label(frame1, text="reconnection, its causes and effects, what to do in case it happens, and analyze how often they")  # Crea el widget Label en el frame1
        label1.place(x=20, y=31) 
        label2 = Label(frame1, text="occur, with specific guidance for any kind of people, even those which deal with technical affairs.")  # Crea el widget Label en el frame1
        label2.place(x=20, y=51) 
        label3 = Label(frame1, text="What is a magnetic reconnection?", font=("Impact",12), fg='midnight blue')  # Crea el widget Label en el frame1
        label3.place(x=2, y=77) 
        label = Label(frame1, image=imagen_convertida)
        label.image = imagen_convertida  # Mantén una referencia a la imagen para evitar la recolección de basura
        label.place(x=2, y=110)
        label4 = Label(frame1, text="Is a fundamental plasma process converting magnetic energy")  # Crea el widget Label en el frame1
        label4.place(x=200, y=111) 
        label5 = Label(frame1, text="into particles' kinetic and thermal energy and is known to")  # Crea el widget Label en el frame1
        label5.place(x=200, y=130) 
        label6 = Label(frame1, text="occur in the sun's atmosphere, the earth magnetosphere and")  # Crea el widget Label en el frame1
        label6.place(x=200, y=149) 
        label7 = Label(frame1, text="and the laboratory plasmas.")  # Crea el widget Label en el frame1
        label7.place(x=200, y=167) 
        label8 = Label(frame1, text="Magnetic Reconnection can abruptly convert energy stored in")  # Crea el widget Label en el frame1
        label8.place(x=200, y=195)
        label9 = Label(frame1, text="magnetic fields to energy in charged particles, and power such")  # Crea el widget Label en el frame1
        label9.place(x=200, y=214)
        label10 = Label(frame1, text="diverse phenomena as solar and stellar flares, magnetic storms")  # Crea el widget Label en el frame1
        label10.place(x=200, y=232)
        label11 = Label(frame1, text=" and aurorae in near-Earth space, and major disruptions in magnetically confined fusion devices.")
        label11.place(x=2, y=252)

        # Botones en la pestaña "Satellites"
        frame2= LabelFrame(self.tab2, text = "Satellites that keep track of magnetic fields", font = ("Impact",14), fg= 'midnight blue')
        frame2.pack(fill="both", expand="yes", padx=20, pady=20)
        label12 = Label(frame2, text="DSCOVR", font=("Impact",12), fg = "midnight blue")  # Crea el widget Label en el frame1
        label12.place(x=15, y=12)
        label13 = Label(frame2, text="(Deep Space Climate Observatory), pronounced disco-ver, is a NASA space satellite that was")
        label13.place(x=15, y=35) 
        label14 = Label(frame2, text="launched in 2015. DSCOVR's primary mission is to monitor and provide data on space weather,")
        label14.place(x=15, y=53)
        label15 = Label(frame2, text="specifically on the solar wind and its impact on Earth.")
        label15.place(x=15, y=71)  
        label17 = Label(frame2, text="Cluster", font=("Impact",12), fg = "midnight blue")  # Crea el widget Label en el frame1
        label17.place(x=15, y=98)
        label18 = Label(frame2, text="The European Space Agency (ESA) operates the Cluster mission, which consists of four identical")
        label18.place(x=15, y=121)
        label19 = Label(frame2, text="satellites launched in 2000. These satellites have made detailed measurements of the Earth's")
        label19.place(x=15, y=138)
        label20 = Label(frame2, text="magnetosphere, including the study of magnetic reconnections.")
        label20.place(x=15, y=155)
        label17 = Label(frame2, text="THEMIS", font=("Impact",12), fg = "midnight blue")  # Crea el widget Label en el frame1
        label17.place(x=15, y=180)
        label20 = Label(frame2, text="(Time History of Events and Macroscale Interactions during Substorms) mission launched five")
        label20.place(x=15, y=200)
        label20 = Label(frame2, text="satellites in 2007 to study auroras and magnetic reconnections in Earth's magnetosphere.")
        label20.place(x=15, y=215)
        
        self.button1 = tk.Button(self.tab2, text="Back", command=self.open_tab1)
        self.button1.pack(pady=10)
        self.button1.place(x=500, y=300)
        
        #Crear label dentro de la pestaña information
        frame3 = LabelFrame(self.tab3, text="Recent Event about Magnetic Reconnections", font=('Impact', 14), fg='midnight blue')
        frame3.pack(fill="both", expand="yes", padx=20, pady=20)
        label17 = Label(frame3, text="", font=("Impact",12), fg = "midnight blue")  # Crea el widget Label en el frame1
        label17.place(x=15, y=180)
        label18 = Label(frame3, image=imagen_convertida2)
        label18.image = imagen_convertida2  # Mantén una referencia a la imagen para evitar la recolección de basura
        label18.place(x=15, y=20)
        label19 = Label(frame3, text="International experts confirmed that last Tuesday, July 18,")
        label19.place(x=240, y=20) 
        label19 = Label(frame3, text="2023, a cannibalistic solar storm, occurred with a weak")
        label19.place(x=240, y=37)
        label20 = Label(frame3, text="magnitude on the G scale, which did not even cause")
        label20.place(x=240, y=53)
        label21 = Label(frame3, text="problems in the satellites. Likewise, scientits predict")
        label21.place(x=240, y=70)
        label22 = Label(frame3, text="that the greatest impact may reach the year 2025, and to")
        label22.place(x=240, y=87)
        label23 = Label(frame3, text="this end, it is expected that solar storms will be detected")
        label23.place(x=240, y=105)
        label24 = Label(frame3, text="in the next few months.")
        label24.place(x=240, y=120)
        label_ = Label(frame3, text="Days before, on July 14, a CME - cannibalistic solar storm was also recorded, which apparently")
        label_.place(x=15, y=150)
        label_1 = Label(frame3, text="originated with a sunspot AR3370, the second ejecta was detected a day later with a high speed")
        label_1.place(x=15, y=168)
        label_2 = Label(frame3, text="and originating from the sunspot AR3363, reported experts from the Space Weather Prediction")
        label_2.place(x=15, y=185)
        label_3 = Label(frame3, text="Center of the National Oceanic and Atmospheric Administration (NOAA).")
        label_3.place(x=15, y=205)
        self.button1 = tk.Button(self.tab3, text="Back", command=self.open_tab2)
        self.button1.pack(pady=10)
        self.button1.place(x=500, y=300)

        # Crear el LabelFrame dentro de la pestaña "Calculation"
        frame4 = LabelFrame(self.tab4, text="Table of Magnitude Values ​​of the chosen day", font=('Impact', 14), fg='midnight blue')
        frame4.pack(fill="both", expand="yes", padx=20, pady=20)
    
    # Crear un botón para generar y mostrar la tabla

        self.button2 = tk.Button(frame4, text="Generar", command=self.generar_tabla)
        self.button2.pack(pady=10)
        self.button2.place(x=100, y=400)
        self.button2.pack()

        # Crear un lienzo (Canvas) en el frame4 para mostrar la tabla
        self.canvas = Canvas(frame4)
        self.canvas.pack(fill="both", expand=True)
        self.treeview = None

        

    def generar_tabla(self):
        # Carga los datos del archivo Excel correspondientes a "23 de Julio del 2023"
        try:
            df = pd.read_excel("C:/EOS PROYECT/23 de Julio del 2023.xlsx", sheet_name='23 de Julio del 2023')
            # Muestra los datos en el Canvas en lugar de una nueva ventana
            self.mostrar_tabla_en_canvas(df)
        except Exception as e:
            print("Error al cargar el archivo Excel:", str(e))


    def mostrar_tabla_en_canvas(self, df):
        if self.treeview:
            self.treeview.destroy()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.treeview = ttk.Treeview(self.canvas, columns=list(df.columns))

        for col in df.columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=50)
    
    # Calcula las dimensiones del Canvas y la tabla
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        table_width = sum(self.treeview.column(col, option="width") for col in df.columns)
        table_height = len(df) * self.treeview.winfo_reqheight()

    # Calcula la posición para centrar la tabla
        x = (canvas_width - table_width) / 45
        y = (canvas_height - table_height) / 45

        for i, row in df.iterrows():
            self.treeview.insert('', "end", values=[i] + row.tolist())
    
        self.treeview.pack()
        self.canvas.create_window(x, y, window=self.treeview, anchor="nw")
    
    #Frame 5
        
        frame5 = LabelFrame(self.tab5, text="General precautions you can take to protect yourself", font=('Impact', 14), fg='midnight blue')
        frame5.pack(fill="both", expand="yes", padx=20, pady=20)
        label_1 = Label(frame5, text="Stay informed", font= ("Impact", 12), fg= "midnight blue")
        label_1.place(x=10, y=15)
        label13 = Label(frame5, text="Keep an eye on space weather forecasts. Sign up for space weather alerts and notifications on our")
        label13.place(x=10, y=40)
        label13 = Label(frame5, text="program for events like solar flares and geomagnetic storms that can result from magnetic")
        label13.place(x=10, y=58)
        label13 = Label(frame5, text="reconnection in the Sun's atmosphere")
        label13.place(x=10, y=75)
        label_10 = Label(frame5, text="Mitigating communication disruptions", font= ("Impact", 12), fg= "midnight blue")
        label_10.place(x=10, y=94)
        label13 = Label(frame5, text="Be aware that geomagnetic storms can disrupt radio communications and GPS signals. Consider")
        label13.place(x=10, y=115)
        label13 = Label(frame5, text="rescheduling them during preducted geomagnetic storm activity periods.")
        label13.place(x=10, y=134)
        label_10 = Label(frame5, text="Power grid Protection", font= ("Impact", 12), fg= "midnight blue")
        label_10.place(x=10, y=155)
        label13 = Label(frame5, text=" Severe geomagnetic storms can induce electric currents in power lines and transformers,")
        label13.place(x=10, y=175)
        label13 = Label(frame5, text="potentially causing electrical grid disturbances or even blackouts. There isn't much an")
        label13.place(x=10, y=195)
        label13 = Label(frame5, text="individual can do to proyect the power grid")
        label13.place(x=10, y=215)
    def open_tab1(self):
        self.notebook.select(self.tab1)

    def open_tab2(self):
        self.notebook.select(self.tab2)
    
    def open_tab3(self):
        self.notebook.select(self.tab3)

    def open_tab4(self):
        self.notebook.select(self.tab4)

    def open_tab5(self):
        self.notebook.select(self.tab5)
    

if __name__ == '__main__':
    root = Tk()
    eos = EOS(root)
    
    root.iconbitmap("C:\EOS PROYECT\icono.ico")
    
    root.mainloop()
