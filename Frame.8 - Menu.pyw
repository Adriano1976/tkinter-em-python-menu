from tkinter import *

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.geometry('400x300')
root.title('Exemplo de Menu e Submenu')

# ==============================================================
# Método Donothing
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Validado")   
    button.pack()

# ==============================================================
# Menu Arquivo
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=filemenu)

# Submenu de Arquivo
filemenu.add_command(label="Novo", command=donothing)
filemenu.add_command(label="Abrir", command=donothing)
filemenu.add_command(label="Salvar", command=donothing)
filemenu.add_command(label="Salvar como...", command=donothing)
filemenu.add_command(label="Fechar", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.quit)

# ==============================================================
# Menu Editar
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editmenu)

# Submenu de Editar
editmenu.add_command(label="Pasta", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Recortar", command=donothing)
editmenu.add_command(label="Copiar", command=donothing)
editmenu.add_command(label="Colar", command=donothing)
editmenu.add_command(label="Excluir", command=donothing)
editmenu.add_command(label="Selecionar Tudo", command=donothing)

# ==============================================================
# Menu Ajuda
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ajuda", menu=helpmenu)

# Submenu de Ajuda
helpmenu.add_command(label="Ajuda Inicial", command=donothing)
helpmenu.add_command(label="Sobre...", command=donothing)

root.mainloop()



