import customtkinter as ctk # type: ignore
from tkinter import messagebox

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

class AppEscala(ctk.CTk):
    def __init__(self):
        super().__init__()

## INTERFACE
        self.title("Calculadora de Escalas")
        self.geometry("450x580")
        self.grid_columnconfigure(0, weight=1)


        self.logo_label = ctk.CTkLabel(self, text="Calculadora de Desenho Técnico", 
                                      font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=(30, 20))

        self.container = ctk.CTkFrame(self)
        self.container.pack(pady=10, padx=30, fill="both", expand=True)

        self.label_d = ctk.CTkLabel(self.container, text="Dimensão do Desenho (d)")
        self.label_d.pack(pady=(15, 0))
        self.entry_desenho = ctk.CTkEntry(self.container, placeholder_text="Ex: 18", width=250)
        self.entry_desenho.pack(pady=5)

        self.label_e = ctk.CTkLabel(self.container, text="Escala (X:Y)")
        self.label_e.pack(pady=(10, 0))
        self.entry_escala = ctk.CTkEntry(self.container, placeholder_text="Ex: 1:2 ou 5:1", width=250)
        self.entry_escala.pack(pady=5)

        self.label_r = ctk.CTkLabel(self.container, text="Dimensão Real da Peça (R)")
        self.label_r.pack(pady=(10, 0))
        self.entry_real = ctk.CTkEntry(self.container, placeholder_text="Ex: 36", width=250)
        self.entry_real.pack(pady=5)

        self.btn_calc = ctk.CTkButton(self, text="RESOLVER CAMPO VAZIO", command=self.calcular, 
                                      fg_color="#2ecc71", hover_color="#27ae60", font=ctk.CTkFont(weight="bold"))
        self.btn_calc.pack(pady=(20, 10), padx=50, fill="x")

        self.btn_clear = ctk.CTkButton(self, text="Limpar Tudo", command=self.limpar, 
                                       fg_color="#cc382e", hover_color="#a82d25")
        self.btn_clear.pack(pady=10)

        self.res_frame = ctk.CTkFrame(self, height=60, fg_color="transparent")
        self.res_frame.pack(pady=10, fill="x")
        self.label_resultado = ctk.CTkLabel(self.res_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_resultado.pack()

# LÓGICA E FORMULAS 
    def calcular(self):
        try:
            d_str = self.entry_desenho.get().replace(',', '.').strip()
            r_str = self.entry_real.get().replace(',', '.').strip()
            e_str = self.entry_escala.get().strip()

            d = float(d_str) if d_str else None
            r = float(r_str) if r_str else None
            
            # Escala E = d / R. Se for 1:2, o fator é 0.5. Se 5:1, o fator é 5.0.
            fator = None
            if e_str:
                if ":" in e_str:
                    p1, p2 = map(float, e_str.split(":"))
                    fator = p1 / p2
                else:
                    fator = 1 / float(e_str)

 #  APLICAÇÃO DAS FÓRMULAS MATEMÁTICAS 

            # FÓRMULA ESCALA: Fator = d / R
            if d is not None and r is not None and fator is None:
                fator_calc = d / r
                # Formata o texto para exibir 1:X (Redução) ou X:1 (Ampliação)
                if fator_calc < 1:
                    texto_escala = f"1:{int(1/fator_calc) if (1/fator_calc).is_integer() else round(1/fator_calc, 2)}"
                else:
                    texto_escala = f"{int(fator_calc) if fator_calc.is_integer() else round(fator_calc, 2)}:1"
                
                self.entry_escala.delete(0, 'end')
                self.entry_escala.insert(0, texto_escala)
                self.exibir_resultado(f"Escala Calculada: {texto_escala}")


            # FÓRMULA DIMENSÃO REAL (R): R = d / Fator
            elif d is not None and fator is not None and r is None:
                res_r = d / fator
                self.entry_real.delete(0, 'end')
                self.entry_real.insert(0, f"{res_r:g}")
                self.exibir_resultado(f"Dimensão Real: {res_r:g}")

            
            # FÓRMULA DIMENSÃO NO DESENHO (d): d = R * Fator
            elif r is not None and fator is not None and d is None:
                res_d = r * fator
                self.entry_desenho.delete(0, 'end')
                self.entry_desenho.insert(0, f"{res_d:g}")
                self.exibir_resultado(f"Medida no Desenho: {res_d:g}")
            
            else:
                messagebox.showwarning("Aviso", "Por favor, deixe apenas UM campo vazio para calcular.")

        except Exception as e:
            messagebox.showerror("Erro", "Entrada inválida! Verifique os números e o formato da escala (ex: 1:2).")

    def exibir_resultado(self, texto):
        self.label_resultado.configure(text=texto, text_color="#3498db")

    def limpar(self):
        self.entry_desenho.delete(0, 'end')
        self.entry_real.delete(0, 'end')
        self.entry_escala.delete(0, 'end')
        self.label_resultado.configure(text="")

#  EXECUÇÃO DO PROGRAMA 
if __name__ == "__main__":
    app = AppEscala()
    app.mainloop()