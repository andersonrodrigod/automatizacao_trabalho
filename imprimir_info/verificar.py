def criar_arquivo(self):

        caminho_do_arquivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", ".json"), ("All files", ".")],
            title="Salvar arquivo"
        )

        if caminho_do_arquivo:
            # Abrir nova janela para preencher coordenadas
            self.nova_janela_pos = ctk.CTkToplevel(self.parent)
            self.nova_janela_pos.title("Preencher Coordenadas")
            self.nova_janela_pos.geometry("400x200")
            self.nova_janela_pos.grab_set()

            label = ctk.CTkLabel(self.nova_janela_pos, text="Preencha as coordenadas:", font=("Arial", 16))
            label.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

            # Entradas para coordenadas
            self.coord_x = ctk.CTkEntry(self.nova_janela_pos, placeholder_text="Coordenada X")
            self.coord_x.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")

            self.coord_y = ctk.CTkEntry(self.nova_janela_pos, placeholder_text="Coordenada Y")
            self.coord_y.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

            # Botão para salvar coordenadas e criar arquivo
            botao_salvar = ctk.CTkButton(self.nova_janela_pos, text="Salvar Coordenadas", command=lambda: self.salvar_coordenadas(caminho_do_arquivo))
            botao_salvar.grid(row=3, column=0, pady=20, padx=20, sticky="nsew")

    def salvar_coordenadas(self, caminho_do_arquivo):
        # Coletando dados da entrada de coordenadas
        try:
            x = int(self.coord_x.get())
            y = int(self.coord_y.get())
        except ValueError:
            print("Por favor, insira valores válidos para as coordenadas.")
            return

        posicao = {
            "codigo_carteira": [{"x": x, "y": y}],
            "info_meidico": [{"x": 0, "y": 0}],
            "info_assistente": [{"x": 0, "y": 0}]
        }

        with open(caminho_do_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(posicao, arquivo, indent=4)
            print(f"Arquivo {caminho_do_arquivo} criado com sucesso")

        # Fechar a janela após salvar
        self.nova_janela_pos.destroy()