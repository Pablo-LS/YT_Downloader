import tkinter
import customtkinter
from pytube import YouTube

def descarga():
    try:
        linkYT = link.get()
        yt = YouTube(linkYT, on_progress_callback= on_progress)      
        video = yt.streams.get_highest_resolution()

        titulo.configure(text = yt.title, text_color = "white")
        descargaFin.configure(text = "")

        video.download()
        descargaFin.configure(text= "¡Descarga finalizada!")

    except:
        descargaFin.configure(text = "Link no válido", text_color = "red")

def on_progress(stream, chunk, bytes_remaining):
    tamaño_total = stream.filesize
    bytes_descargados = tamaño_total - bytes_remaining
    porcentajeProgreso = bytes_descargados / tamaño_total * 100
    porcentajeCompletado = str(int(porcentajeProgreso))
    
    porcentaje.configure(text = porcentajeCompletado + "%")
    porcentaje.update()

    barraProg.set(float(porcentajeProgreso) / 100)

# Configuración de sistema
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Ventana
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Elementos de la ventana
titulo = customtkinter.CTkLabel(app, text="Inserta el link de un video de Youtube")
titulo.place(relx=0.5, rely=0.2, anchor="center")

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=550, height=35, textvariable= url)
link.place(relx=0.5, rely=0.3, anchor="center")

botonDescargar = customtkinter.CTkButton(app, text="Descargar", command= descarga)
botonDescargar.place(relx=0.5, rely=0.45, anchor="center")

porcentaje = customtkinter.CTkLabel(app, text= "0%")
porcentaje.place(relx=0.5, rely=0.55, anchor="center")

barraProg = customtkinter.CTkProgressBar(app, width= 400)
barraProg.set(0)
barraProg.place(relx=0.5, rely=0.6, anchor="center")

descargaFin = customtkinter.CTkLabel(app, text="")
descargaFin.place(relx=0.5, rely=0.65, anchor="center")

# Ejecutar app
app.mainloop()