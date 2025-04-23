# Import

import tkinter as tk
from tkinter import messagebox

# Lista para armazenar matérias e dificuldades
materias = []

# Função para adicionar uma matéria à lista
def adicionar_materia():
    nome = entrada_materia.get()
    dificuldade = entrada_dificuldade.get()
    
    if nome and dificuldade.isdigit():
        dificuldade_int = int(dificuldade)
        if 1 <= dificuldade_int <= 5:
            materias.append({
                "nome": nome,
                "dificuldade": dificuldade_int
            })
            lista_materias.insert(tk.END, f"{nome} - Dificuldade: {dificuldade}")
            entrada_materia.delete(0, tk.END)
            entrada_dificuldade.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "A dificuldade deve ser um número entre 1 e 5.")
    else:
        messagebox.showwarning("Atenção", "Preencha o nome e uma dificuldade válida (número)")
        
# Função para calcular o tempo de estudo
def calcular_tempo():
    tempo_total = entrada_tempo.get()
    
    try:
        
        if ':' in tempo_total:
            horas, minutos = map(int, tempo_total.split(':'))
            tempo_total = horas * 60 + minutos
        else:
            tempo_total = int(tempo_total)
    except:
        messagebox.showwarning("Erro", "Digite o tempo com minutos (ex: 90) ou horas:minutos(ex: 1:30)")
        return
    
    tempo_total = int(tempo_total)
    total_dificuldade = sum(m['dificuldade'] for m in materias)
    
    if total_dificuldade == 0:
        messagebox.showwarning("Erro", "Adicione pelo menos uma matéria com dificuldade maior que 0.")
        return
    
    resultado_texto.delete("1.0", tk.END)
    
    for m in materias:
        
        tempo_materia = round((m['dificuldade']/ total_dificuldade) * tempo_total)
        resultado_texto.insert(tk.END, f"{m['nome']}: {tempo_materia} minutos\n")

# Interface principal

janela = tk.Tk()
janela.title("Calculadora de Rotina de Estudos")

# Campo para tempo total

tk.Label(janela, text="Tempo total disponível (min ou horas:min):").pack()
tk.Label(janela, text="Ex: 90 ou 1:30", fg="gray").pack()
entrada_tempo = tk.Entry(janela)
entrada_tempo.pack()

# Nome da matéria

tk.Label(janela, text="Nome da matéria:").pack()
entrada_materia = tk.Entry(janela)
entrada_materia.pack()

# Nível de dificuldade

tk.Label(janela, text="Nível de dificuldade (1-5):").pack()
entrada_dificuldade = tk.Entry(janela)
entrada_dificuldade.pack()

# Botões e Lista
tk.Button(janela, text="Adicionar Matéria", command=adicionar_materia).pack(pady=5)
lista_materias = tk.Listbox(janela, width=50)
lista_materias.pack(pady=10)

# Botão para calcular tempo
tk.Button(janela, text="Calcular Rotina", command=calcular_tempo).pack(pady=5)

# Resultado
tk.Label(janela, text="Distribuição do Tempo:").pack()
resultado_texto = tk.Text(janela, height=10, width=40)
resultado_texto.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()
