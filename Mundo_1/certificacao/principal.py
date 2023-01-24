from tkinter import *
from tkinter import ttk

root = Tk()

def cadastrar_ferramentas():
    top_ferramenta = Toplevel()
    top_ferramenta.title("Cadastrar Ferramentas")
    top_ferramenta.configure(background='#1e3743')
    top_ferramenta.state('zoomed')
    titulo_ferramentas = Label(top_ferramenta, text="Cadastrar ferramentas").place(relx=0.4, rely=0.03)
    class button():
        def exit1():
            top_ferramenta.destroy()
            top_ferramenta.update()
        btn_salvar = Button(top_ferramenta, text="salvar").place(relx=0.87, rely=0.88, relwidth=0.12,relheight=0.1)
        btn_sair = Button(top_ferramenta, text="Voltar", command=exit1).place(relx=0.87, rely=0.03, relwidth=0.12,relheight=0.1)

    class entradas():
        # DESCRIÇÃO
        label_descricao_ferrament = Label(top_ferramenta, text="Descrição da ferramenta: ").place(relx=0.23, rely=0.1, relwidth=0.2, relheight=0.085)
        entry_descricao_ferramenta = Entry(top_ferramenta).place(relx=0.48, rely=0.1, relwidth=0.2, relheight=0.085)

        # FABRICANTE
        label_fabricante = Label(top_ferramenta,text="Fabricante: ").place(relx=0.23, rely=0.2, relwidth=0.2, relheight=0.085)
        entry_fabricante = Entry(top_ferramenta).place(relx=0.48, rely=0.2, relwidth=0.2, relheight=0.085)

        # VOLTAGEM
        label_voltagem = Label(top_ferramenta, text="Voltagem: ").place(relx=0.23, rely=0.3, relwidth=0.2, relheight=0.085)
        volts = ["110v", "220v", "360v", "110v~220v"]
        voltagem = ttk.Combobox(top_ferramenta, values=volts).place(relx=0.48, rely=0.3, relwidth=0.2, relheight=0.085)

        # PART_NUMBER
        label_part_number = Label(top_ferramenta,text="Part Number: ").place(relx=0.23, rely=0.4, relwidth=0.2, relheight=0.085)
        entry_part_number = Entry(top_ferramenta).place(relx=0.48, rely=0.4, relwidth=0.2, relheight=0.085)

        # UNIDADE DE MEDIDA && TAMANHO
        # label
        label_tamanho = Label(top_ferramenta, text="Tamanho").place(relx=0.23, rely=0.5, relwidth=0.2, relheight=0.085)
        # entry
        medida = ["Pol", "MM", "CM", "M", "Outro"]
        entry_tamanho = Entry(top_ferramenta).place(relx=0.48, rely=0.5, relwidth=0.15, relheight=0.085)
        unidade_medida = ttk.Combobox(top_ferramenta, values=medida).place(relx=0.63, rely=0.5, relwidth=0.05, relheight=0.085)
        
        # TIPO DA FERRAMENTA
        label_tipo_ferramenta = Label(top_ferramenta, text="Tipo da ferramenta: ").place(relx=0.23, rely=0.6, relwidth=0.2, relheight=0.085)
        entry_tipo_ferramenta = Entry(top_ferramenta).place(relx=0.48, rely=0.6, relwidth=0.2, relheight=0.085)

        # MATERIAL DA FERRAMENTA
        label_material_ferramenta = Label(top_ferramenta, text="Material da ferramenta: ").place(relx=0.23, rely=0.7, relwidth=0.2, relheight=0.085)
        entry_material_ferramenta = Entry(top_ferramenta).place(relx=0.48, rely=0.7, relwidth=0.2, relheight=0.085)

        # TEMPO MAXIMO DA RESERVA
        label_tempo_reserva = Label(top_ferramenta, text="Tempo maximo de reserva(em horas): ").place(relx=0.23, rely=0.8, relwidth=0.2, relheight=0.085)
        entry_tempo_reserva = Entry(top_ferramenta).place(relx=0.48, rely=0.8, relwidth=0.2, relheight=0.085)

    entradas()
    button()

def cadastrar_tecnico():
    top_tecnico = Toplevel()
    top_tecnico.title("Cadastrar Ferramentas")
    top_tecnico.configure(background='#1e3743')
    top_tecnico.state('zoomed')
    titulo_tecnico = Label(top_tecnico, text="Cadastrar Técnico").place(relx=0.42, rely=0.03)

    class button():
        def exit2():
            top_tecnico.destroy()
            top_tecnico.update()
        btn_salvar = Button(top_tecnico, text="salvar").place(relx=0.87, rely=0.88, relwidth=0.12,relheight=0.1)
        btn_sair = Button(top_tecnico, text="voltar", command=exit2).place(relx=0.87, rely=0.03, relwidth=0.12,relheight=0.1)
    class entrys():

        #label_descricao_ferrament = Label(top_ferramenta, text="Descrição da ferramenta: ").place(relx=0.23, rely=0.1, relwidth=0.2, relheight=0.085)
        #entry_descricao_ferramenta = Entry(top_ferramenta).place(relx=0.48, rely=0.1, relwidth=0.2, relheight=0.085)
        label_cpf = Label(top_tecnico, text="CPF: ").place(relx=0.23, rely=0.15, relwidth=0.2, relheight=0.085)
        entry_cpf = Entry(top_tecnico).place(relx=0.48, rely=0.15, relwidth=0.2, relheight=0.085)

        label_Nome = Label(top_tecnico, text="Nome completo: ").place(relx=0.23, rely=0.30, relwidth=0.2, relheight=0.085)
        entry_Nome = Entry(top_tecnico).place(relx=0.48, rely=0.30, relwidth=0.2, relheight=0.085)

        label_telefone = Label(top_tecnico, text="Telefone: ").place(relx=0.23, rely=0.45, relwidth=0.2, relheight=0.085)
        entry_telefone = Entry(top_tecnico).place(relx=0.48, rely=0.45, relwidth=0.2, relheight=0.085)

        label_turno = Label(top_tecnico, text="Turno: ").place(relx=0.23, rely=0.6, relwidth=0.2, relheight=0.085)
        turno = ["manhã","tarde","noite"]
        voltagem = ttk.Combobox(top_tecnico, values=turno).place(relx=0.48, rely=0.6, relwidth=0.2, relheight=0.085)

        label_equipe = Label(top_tecnico, text="Equipe: ").place(relx=0.23, rely=0.75, relwidth=0.2, relheight=0.085)
        entry_equipe = Entry(top_tecnico).place(relx=0.48, rely=0.75, relwidth=0.2, relheight=0.085)

    entrys()
    button()



class main():
    class estilo():
        root.title("Reservar Ferramentas")
        root.configure(background='#1e3743')
        root.state('zoomed')
        root.geometry("750x600")

    class Frame():

        frame = Frame(bd=4, bg='#959595', highlightthickness=3, highlightbackground='#759fe6')
        frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
            
        # ///////////////////////            LINHA              ////////////////////
        linha = Label(frame, text='')
        linha.place(relx=-0.1, rely=0.13, relwidth=1.5, relheight=0.008)
            
        # ///////////////////////               TEXTO PRINCIPAL              ///////////////////////
        titulo = Label(frame, text="Reservas")
        titulo.place(relx=0.40, rely=0.15, relwidth=0.2, relheight=0.1)
            
        # ///////////////////////                   BOTÕES                   ///////////////////////
        # Cadastrar_tecnico
        btn_tecnico = Button(frame, text="Cadastrar técnico", command=cadastrar_tecnico)
        btn_tecnico.place(relx=0.01, rely=0.015, relwidth=0.1, relheight=0.1)

        # cadastrar_ferramenta
        btn_ferramenta = Button(frame, text="Cadastrar ferramentas", command=cadastrar_ferramentas)
        btn_ferramenta.place(relx=0.12, rely=0.015, relwidth=0.1, relheight=0.1)

        # reservar
        btn_reservar = Button(frame, text="Reservar")
        btn_reservar.place(relx=0.88, rely=0.015, relwidth=0.1, relheight=0.1)



        




main()
mainloop()