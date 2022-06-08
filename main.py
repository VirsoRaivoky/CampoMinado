from tkinter import *
import settings
import utils

root = Tk()
# Configurações da janela (BG, Resolução, Nome etc..

root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Campo Minado")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',
    width=1440,
    height=utils.height_prct(25)
    )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=360,
    height=720
)
left_frame.place(x=0, y=180)

# executa a janela

root.mainloop()

