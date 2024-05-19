import funcoes_de_acoes

# Função para salvar embarque de quartos rastreados por pedido
def salvar_embarque():
    try: 
        
        caminho_arquivo = r'C:\Users\Floreste\Desktop\Projetos Python\automoção_trabalho'
        nome_arquivo = 'pediodo.txt'
        
        # Abre pedidos.txt para ler dados
        #with open(r"C:\Users\Floreste\Desktop\Projetos Python\automoção_trabalho\data_abate.txt", 'r') as arquivo:
        with open(f"{caminho_arquivo}\\{nome_arquivo}", 'r') as arquivo:

            for linha in arquivo:
                pedido = linha.split()[0]
                ordem  = linha.split()[1]
                data   = linha.split()[3]

                if pedido != "":
                    funcoes_de_acoes.inserir_pedido(pedido)
                    funcoes_de_acoes.executar()
                    funcoes_de_acoes.pre_visualizar()
                    funcoes_de_acoes.page_setup_retrato()
                    funcoes_de_acoes.imprimir()
                    funcoes_de_acoes.salvar_relatorio(nome_arquivo = "12 - Embarque de quartos rastreados - Op. " + ordem + " " + data)
                    funcoes_de_acoes.fechar_pre_visualizar()
                    funcoes_de_acoes.fechar_guia()  
                else:
                    break

    except Exception as e:
        funcoes_de_acoes.registrar_log(e,'função salvar_embarque')