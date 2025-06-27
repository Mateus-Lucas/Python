import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
from fpdf import FPDF

# Configurações iniciais (serão substituídas pelas metas do usuário)
METAS = {"calorias": 0, "proteina": 0, "carboidrato": 0, "gordura": 0}
REFEICOES = ["Café da Manhã", "Almoço", "Lanche", "Jantar"]
CORES = {"positivo": "#4CAF50", "negativo": "#F44336", "neutro": "#2196F3"}


class DietaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Primeiro configurar a janela principal
        self.title("Gerenciador de Dieta Avançado")
        self.geometry("1000x700")
        self.configure(bg="#f5f5f5")

        # Esconder a janela principal até definir as metas
        self.withdraw()

        # Inicializar estruturas de dados
        self.frames = {}
        self.itens = {ref: [] for ref in REFEICOES}
        self.diff_labels = {}

        # Pedir metas ao usuário
        self.definir_metas()

        # Se o usuário não definiu metas, fechar o app
        if not all(METAS.values()):
            self.destroy()
            return

        # Carregar alimentos
        self.alimentos_dict = self.carregar_alimentos()
        if not self.alimentos_dict:
            self.destroy()
            return

        self.nomes_alimentos = list(self.alimentos_dict.keys())

        # Mostrar a interface principal
        self._criar_interface()
        self._criar_menu()
        self.deiconify()

    def definir_metas(self):
        """Janela para o usuário definir suas metas nutricionais"""
        meta_window = tk.Toplevel(self)
        meta_window.title("Definir Metas Nutricionais")
        meta_window.geometry("400x300")
        meta_window.grab_set()  # Torna modal
        meta_window.protocol("WM_DELETE_WINDOW", lambda: None)  # Impede fechar sem definir metas

        tk.Label(meta_window, text="Digite suas metas diárias:", font=('Arial', 12)).pack(pady=10)

        campos = [
            ("Calorias (kcal):", "calorias"),
            ("Proteína (g):", "proteina"),
            ("Carboidratos (g):", "carboidrato"),
            ("Gorduras (g):", "gordura")
        ]

        entries = {}
        for texto, key in campos:
            frame = tk.Frame(meta_window)
            frame.pack(pady=5, fill='x', padx=20)

            tk.Label(frame, text=texto, width=15).pack(side='left')
            entry = tk.Entry(frame)
            entry.pack(side='left', expand=True, fill='x')
            entries[key] = entry

        def salvar_metas():
            try:
                for key, entry in entries.items():
                    METAS[key] = float(entry.get())
                meta_window.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Digite valores numéricos válidos!", parent=meta_window)

        btn_salvar = tk.Button(meta_window, text="Salvar Metas", command=salvar_metas)
        btn_salvar.pack(pady=20)

        self.wait_window(meta_window)  # Espera fechar a janela de metas

    def carregar_alimentos(self):
        try:
            with open("base_alimentos.json", "r", encoding="utf-8") as f:
                alimentos = json.load(f)
            return {a["nome"]: a for a in alimentos}
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo base_alimentos.json não encontrado!", parent=self)
            self.destroy()
            return None
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao ler o arquivo de alimentos!", parent=self)
            self.destroy()
            return None

    def _criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Notebook para as refeições
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill="both", expand=True)

        for refeicao in REFEICOES:
            frame = ttk.Frame(notebook, padding=10)
            notebook.add(frame, text=refeicao)
            self._criar_refeicao_frame(frame, refeicao)

        # Frame de resumo
        resumo_frame = ttk.LabelFrame(main_frame, text="Resumo do Dia", padding=10)
        resumo_frame.pack(fill="x", pady=10)

        self.resumo_text = tk.Text(resumo_frame, height=8, wrap=tk.WORD, font=("Segoe UI", 10))
        self.resumo_text.pack(fill="both", expand=True)

        # Frame de diferenças
        diff_frame = ttk.LabelFrame(main_frame, text="Diferença em Relação às Metas", padding=10)
        diff_frame.pack(fill="x", pady=5)

        self.diff_labels = {}
        for i, nutriente in enumerate(["calorias", "proteina", "carboidrato", "gordura"]):
            lbl = ttk.Label(diff_frame, text=f"{nutriente.capitalize()}: ", font=("Segoe UI", 9))
            lbl.grid(row=0, column=i * 2, padx=5, sticky="e")

            diff_lbl = ttk.Label(diff_frame, text="0", font=("Segoe UI", 9, "bold"))
            diff_lbl.grid(row=0, column=i * 2 + 1, padx=5, sticky="w")
            self.diff_labels[nutriente] = diff_lbl

        # Botão de cálculo
        ttk.Button(main_frame, text="Calcular Totais", command=self.calcular_totais,
                   style="Accent.TButton").pack(pady=10)

        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("Accent.TButton", foreground="white", background=CORES["neutro"])

    def _criar_menu(self):
        menubar = tk.Menu(self)

        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Salvar Dieta", command=self.salvar_dieta)
        file_menu.add_command(label="Carregar Dieta", command=self.carregar_dieta)
        file_menu.add_separator()
        file_menu.add_command(label="Exportar PDF", command=self.exportar_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Resetar Tudo", command=self.resetar_tudo)
        file_menu.add_command(label="Sair", command=self.destroy)
        menubar.add_cascade(label="Arquivo", menu=file_menu)

        self.config(menu=menubar)

    def _criar_refeicao_frame(self, frame, refeicao):
        # Frame de adição
        add_frame = ttk.Frame(frame)
        add_frame.pack(fill="x", pady=5)

        ttk.Label(add_frame, text="Alimento:").pack(side="left", padx=5)

        alimento_var = tk.StringVar()
        alimento_cb = ttk.Combobox(add_frame, textvariable=alimento_var,
                                   values=self.nomes_alimentos, state="readonly", width=25)
        alimento_cb.pack(side="left", padx=5)

        ttk.Label(add_frame, text="Quantidade:").pack(side="left", padx=5)

        qtd_var = tk.StringVar(value="100")
        qtd_entry = ttk.Entry(add_frame, textvariable=qtd_var, width=8)
        qtd_entry.pack(side="left", padx=5)

        tipo_var = tk.StringVar()
        tipo_label = ttk.Label(add_frame, textvariable=tipo_var, width=5)
        tipo_label.pack(side="left", padx=5)

        def atualizar_tipo(*args):
            nome = alimento_var.get()
            if nome in self.alimentos_dict:
                tipo_var.set(f"({self.alimentos_dict[nome]['tipo']})")
            else:
                tipo_var.set("")

        alimento_var.trace_add("write", atualizar_tipo)

        def adicionar():
            nome = alimento_var.get()
            try:
                qtd = float(qtd_var.get())
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida.")
                return

            if not nome or nome not in self.alimentos_dict:
                messagebox.showerror("Erro", "Selecione um alimento válido.")
                return

            self.itens[refeicao].append({
                "nome": nome,
                "quantidade": qtd,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            self._atualizar_lista(refeicao)
            alimento_var.set("")
            qtd_var.set("100")

        add_btn = ttk.Button(add_frame, text="Adicionar", command=adicionar)
        add_btn.pack(side="left", padx=5)

        # Lista de alimentos
        lista_frame = ttk.Frame(frame)
        lista_frame.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")

        lista = tk.Listbox(lista_frame, height=10, yscrollcommand=scrollbar.set,
                           selectbackground=CORES["neutro"], font=("Segoe UI", 9))
        lista.pack(fill="both", expand=True)
        scrollbar.config(command=lista.yview)

        # Context menu para remover itens
        context_menu = tk.Menu(lista, tearoff=0)
        context_menu.add_command(label="Remover Selecionado",
                                 command=lambda: self.remover_item(refeicao, lista))

        def show_context_menu(event):
            try:
                context_menu.tk_popup(event.x_root, event.y_root)
            finally:
                context_menu.grab_release()

        lista.bind("<Button-3>", show_context_menu)

        self.frames[refeicao + "_lista"] = lista

    def remover_item(self, refeicao, lista):
        selection = lista.curselection()
        if selection:
            index = selection[0]
            del self.itens[refeicao][index]
            self._atualizar_lista(refeicao)

    def _atualizar_lista(self, refeicao):
        lista = self.frames[refeicao + "_lista"]
        lista.delete(0, tk.END)

        for item in self.itens[refeicao]:
            alimento = self.alimentos_dict[item["nome"]]
            texto = (f"{item['timestamp']} - {item['nome']} ({item['quantidade']}{alimento['tipo']}) | "
                     f"P: {alimento['proteina'] * (item['quantidade'] if alimento['tipo'] == 'un' else item['quantidade'] / alimento['porcao']):.1f}g | "
                     f"C: {alimento['carboidrato'] * (item['quantidade'] if alimento['tipo'] == 'un' else item['quantidade'] / alimento['porcao']):.1f}g | "
                     f"G: {alimento['gordura'] * (item['quantidade'] if alimento['tipo'] == 'un' else item['quantidade'] / alimento['porcao']):.1f}g")
            lista.insert(tk.END, texto)

    def calcular_totais(self):
        totais = {
            "proteina": 0,
            "carboidrato": 0,
            "gordura": 0,
            "calorias": 0
        }

        detalhes = []

        for refeicao in REFEICOES:
            refeicao_total = {"proteina": 0, "carboidrato": 0, "gordura": 0, "calorias": 0}

            for item in self.itens[refeicao]:
                alimento = self.alimentos_dict[item["nome"]]
                qtd = item["quantidade"]

                if alimento["tipo"] == "un":
                    fator = qtd
                else:
                    fator = qtd / alimento["porcao"]

                p = alimento["proteina"] * fator
                c = alimento["carboidrato"] * fator
                g = alimento["gordura"] * fator
                kcal = 4 * p + 4 * c + 9 * g

                refeicao_total["proteina"] += p
                refeicao_total["carboidrato"] += c
                refeicao_total["gordura"] += g
                refeicao_total["calorias"] += kcal

            for k in refeicao_total:
                totais[k] += refeicao_total[k]

            detalhes.append(f"\n{refeicao}:\n"
                            f"  Proteína: {refeicao_total['proteina']:.1f}g\n"
                            f"  Carboidrato: {refeicao_total['carboidrato']:.1f}g\n"
                            f"  Gordura: {refeicao_total['gordura']:.1f}g\n"
                            f"  Calorias: {refeicao_total['calorias']:.0f}kcal")

        # Atualiza resumo
        self.resumo_text.config(state=tk.NORMAL)
        self.resumo_text.delete(1.0, tk.END)

        resumo = (f"TOTAIS DO DIA:\n"
                  f"Calorias: {totais['calorias']:.0f}kcal ({'✅' if totais['calorias'] >= METAS['calorias'] else '❌'} meta: {METAS['calorias']}kcal)\n"
                  f"Proteína: {totais['proteina']:.1f}g ({'✅' if totais['proteina'] >= METAS['proteina'] else '❌'} meta: {METAS['proteina']}g)\n"
                  f"Carboidrato: {totais['carboidrato']:.1f}g ({'✅' if totais['carboidrato'] >= METAS['carboidrato'] else '❌'} meta: {METAS['carboidrato']}g)\n"
                  f"Gordura: {totais['gordura']:.1f}g ({'✅' if totais['gordura'] >= METAS['gordura'] else '❌'} meta: {METAS['gordura']}g)\n"
                  f"\nDETALHES POR REFEIÇÃO:" + "".join(detalhes))

        self.resumo_text.insert(tk.END, resumo)
        self.resumo_text.config(state=tk.DISABLED)

        # Atualiza diferenças
        for nutriente in METAS:
            diferenca = totais[nutriente] - METAS[nutriente]
            self.diff_labels[nutriente].config(
                text=f"{diferenca:+.1f}",
                foreground=CORES["positivo"] if diferenca >= 0 else CORES["negativo"]
            )

    def resetar_tudo(self):
        if messagebox.askyesno("Confirmar", "Deseja realmente resetar todos os dados?"):
            for refeicao in REFEICOES:
                self.itens[refeicao] = []
                self._atualizar_lista(refeicao)

            self.resumo_text.config(state=tk.NORMAL)
            self.resumo_text.delete(1.0, tk.END)
            self.resumo_text.config(state=tk.DISABLED)

            for lbl in self.diff_labels.values():
                lbl.config(text="0", foreground="black")

    def salvar_dieta(self):
        try:
            with open("dieta_salva.json", "w", encoding="utf-8") as f:
                json.dump({
                    "itens": self.itens,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }, f, indent=2)
            messagebox.showinfo("Sucesso", "Dieta salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar dieta:\n{str(e)}")

    def carregar_dieta(self):
        try:
            with open("dieta_salva.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.itens = data["itens"]

                for refeicao in REFEICOES:
                    self._atualizar_lista(refeicao)

            messagebox.showinfo("Sucesso", "Dieta carregada com sucesso!")
            self.calcular_totais()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de dieta não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar dieta:\n{str(e)}")

    def exportar_pdf(self):
        """Exporta a dieta atual para PDF"""
        if not any(len(ref) > 0 for ref in self.itens.values()):
            messagebox.showwarning("Aviso", "Adicione alimentos antes de exportar para PDF!")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Cabeçalho
        pdf.cell(200, 10, txt="Plano Alimentar Personalizado", ln=True, align='C')
        pdf.ln(10)

        # Metas
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Metas Nutricionais:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10,
                 txt=f"Calorias: {METAS['calorias']}kcal | Proteína: {METAS['proteina']}g | Carboidratos: {METAS['carboidrato']}g | Gorduras: {METAS['gordura']}g",
                 ln=True)
        pdf.ln(10)

        # Refeições e totais
        totais = {"proteina": 0, "carboidrato": 0, "gordura": 0, "calorias": 0}

        for refeicao in REFEICOES:
            if not self.itens[refeicao]:  # Pula refeições vazias
                continue

            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt=refeicao, ln=True)
            pdf.set_font("Arial", size=11)

            for item in self.itens[refeicao]:
                alimento = self.alimentos_dict[item["nome"]]
                qtd = item["quantidade"]

                if alimento["tipo"] == "un":
                    fator = qtd
                else:
                    fator = qtd / alimento["porcao"]

                p = alimento["proteina"] * fator
                c = alimento["carboidrato"] * fator
                g = alimento["gordura"] * fator
                kcal = 4 * p + 4 * c + 9 * g

                pdf.cell(0, 10,
                         txt=f"- {item['nome']} ({qtd}{alimento['tipo']}): P:{p:.1f}g C:{c:.1f}g G:{g:.1f}g Kcal:{kcal:.1f}",
                         ln=True)

                # Acumula totais
                totais["proteina"] += p
                totais["carboidrato"] += c
                totais["gordura"] += g
                totais["calorias"] += kcal

            pdf.ln(5)

        # Totais e diferenças
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Totais Diários:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10,
                 txt=f"Calorias: {totais['calorias']:.1f}kcal | Proteína: {totais['proteina']:.1f}g | Carboidratos: {totais['carboidrato']:.1f}g | Gorduras: {totais['gordura']:.1f}g",
                 ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Diferença em Relação às Metas:", ln=True)
        pdf.set_font("Arial", size=11)
        for nutriente in METAS:
            diferenca = totais[nutriente] - METAS[nutriente]
            status = "✅ Atingida" if diferenca >= 0 else "❌ Não atingida"
            pdf.cell(200, 10, txt=f"{nutriente.capitalize()}: {diferenca:+.1f} ({status})", ln=True)

        # Salvar arquivo
        nome_arquivo = f"dieta_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        pdf.output(nome_arquivo)
        messagebox.showinfo("Sucesso", f"PDF gerado com sucesso!\nArquivo: {nome_arquivo}")


if __name__ == "__main__":
    app = DietaApp()
    app.mainloop()
