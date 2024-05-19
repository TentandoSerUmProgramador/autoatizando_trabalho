import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from salvar_embarque_de_quartos import salvar_embarque
from salvar_enderecamento_sintetico import salvar_sintetico
from salvar_enderecamento_analitico import salvar_analitico
from funcoes_de_acoes import registrar_log, fechar_telas, pesquisar_telas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("automatização salvar relatórios")
        self.setGeometry(450, 230, 400, 200)
        
        self.botao_start_embarque = QPushButton("Salvar Embarque de\n Quartos Rastredos", self)
        self.botao_start_embarque.setGeometry(50, 70, 150, 50)
        self.botao_start_embarque.clicked.connect(self.start_embarque)

        self.botao_start_enderecamento = QPushButton("Salvar Endereçamento \ne Registro de pH", self)
        self.botao_start_enderecamento.setGeometry(200, 70, 150, 50)
        self.botao_start_enderecamento.clicked.connect(self.start_enderecamento)

    def start_embarque(self):
        try:

            fechar_telas()
            pesquisar_telas("embarque")
            salvar_embarque()  
        
        except Exception as e:
            registrar_log(e,'função start_embarque')
                
    def start_enderecamento(self):
        try:

            fechar_telas()
            pesquisar_telas("endereçamento")

            caminho_arquivo = r'C:\Users\Floreste\Desktop\Projetos Python\automoção_trabalho'
            nome_arquivo = 'data_abate.txt'

            # Abre data_abate.txt para ler dados
            #with open(r"C:\Users\Floreste\Desktop\Projetos Python\automoção_trabalho\data_abate.txt", 'r') as arquivo:
            with open(f"{caminho_arquivo}\\{nome_arquivo}", 'r') as arquivo:

                for linha in arquivo:
                    data_abate = linha.split()[0]
                    print(data_abate)
                    if data_abate != "":
                        salvar_sintetico(data_abate)
                        salvar_analitico(data_abate)
                    else:
                        break

        except Exception as e:
            registrar_log(e, 'função start_enderecamento')







if __name__ == "__main__":
    # Inicia aplicação PyQt5
    app = QApplication(sys.argv)

    # Cria e exibe a janela principal
    window = MainWindow()
    window.show()

    # Executa o loop de eventos da aplicação
    sys.exit(app.exec_())