import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
import requests
from io import BytesIO

def descarga():
    try:
        botonDescargar.configure(app, text = "Cargando...")
        linkYT = link.get()
        yt = YouTube(linkYT, on_progress_callback= on_progress)      
        video = yt.streams.get_highest_resolution()

        titulo.configure(text = yt.title, text_color = "white")
        descargaFin.configure(text = "")

        # Sacar la miniatura
        try:
            thumbnail_url = yt.thumbnail_url
            response = requests.get(thumbnail_url)
            thumbnail_image = Image.open(BytesIO(response.content))
            thumbnail_photo = ImageTk.PhotoImage(thumbnail_image)

            label = customtkinter.CTkLabel(app, text="", image=thumbnail_photo)
            label.image = thumbnail_photo
            label.pack(padx=10, pady=10)

        except Exception as e:
            print(f"No se puede sacar la miniatura: {str(e)}")

        video.download()
        descargaFin.configure(text= "¡Descarga finalizada!")
        botonDescargar.configure(app, text = "Descargar")

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
titulo.pack(padx = 10, pady = 10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=35, textvariable= url)
link.pack()

botonDescargar = customtkinter.CTkButton(app, text="Descargar", command= descarga)
botonDescargar.pack(padx = 20, pady = 20)

porcentaje = customtkinter.CTkLabel(app, text= "0%")
porcentaje.pack()

barraProg = customtkinter.CTkProgressBar(app, width= 500)
barraProg.set(0)
barraProg.pack()

descargaFin = customtkinter.CTkLabel(app, text="")
descargaFin.pack()

# Ejecutar app
app.mainloop()