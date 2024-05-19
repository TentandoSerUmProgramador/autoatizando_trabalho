import keyboard
import pyautogui
from time import sleep
import datetime 

# Constantes tempo em segundos para sleep()
TEMPO_ESPERA_PEQUENO = 1
TEMPO_ESPERA_CURTO   = 3
TEMPO_ESPERA_MEDIO   = 5
TEMPO_ESPERA_LONGO   = 8
TEMPO_ESPERA_ALTO    = 15

# Constsntes código das telas
EMBARQUE_DE_QUARTOS        = 'cFBED307'
ENDERECAMENTO_E_RGISTRO_PH = 'cFBED348'

# Função para salvar log de erros
def registrar_log(erro, acao):
    try:

        data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        caminho_arquivo = r'C:\Users\Floreste\Desktop\Projetos Python\automoção_trabalho\LOG'
        nome_arquivo = f"log_{acao} as {data_hora_atual}.txt"

        with open(f"{caminho_arquivo}\\{nome_arquivo}", 'w') as arquivo_log:
            log_erro = f"ERRO: [{erro}] HORA: {data_hora_atual}"
            arquivo_log.write(log_erro)
        
        print("VERIFICAR LOG")        
        return "VERIFICAR LOG"
        
    except Exception as e:
        print(f"erro ao registrar LOG {e}")

# Função para fechar todas telas
def fechar_telas():
    try:

        pyautogui.click(579, 36)
        sleep(TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('alt+f10')
        sleep(TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('left')
        sleep(TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('enter')
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função fechar_telas')

# Função para pesquisar telas
def pesquisar_telas(tela):
    try:

        pyautogui.doubleClick(579, 36)
        sleep(TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('ctrl+a')
        sleep(TEMPO_ESPERA_CURTO)

        nome_tela = tela

        if nome_tela == "endereçamento":
    
            pyautogui.write(ENDERECAMENTO_E_RGISTRO_PH)
            sleep(TEMPO_ESPERA_CURTO)
            keyboard.press_and_release('enter')
            sleep(TEMPO_ESPERA_CURTO)
            keyboard.press_and_release('enter')
            sleep(TEMPO_ESPERA_CURTO)

        elif nome_tela == "embarque":

            pyautogui.write(EMBARQUE_DE_QUARTOS)
            keyboard.press_and_release('enter')
            sleep(TEMPO_ESPERA_CURTO)
            keyboard.press_and_release('enter')
            sleep(TEMPO_ESPERA_CURTO)

        else:        
            raise ValueError("NOME DA TELA NÃO INFORMADO/INVALIDO")
        
    except ValueError as e:
        registrar_log(e, 'função pesquisar_telas')   

    except Exception as e:
        registrar_log(e, 'função pesquisar_telas')

# Função para inserir a Pedido
def inserir_pedido(pedido):
    try:

        pyautogui.doubleClick(121, 228, duration=2)
        sleep(TEMPO_ESPERA_PEQUENO)
        pyautogui.write(pedido)
        sleep(TEMPO_ESPERA_PEQUENO)

    except Exception as e:
        registrar_log(e, 'função inserir_pedido')

# Função para inserir a data de abate
def inserir_abate(data_abate):
    try:

        pyautogui.doubleClick(177, 184, duration=2)
        sleep(TEMPO_ESPERA_PEQUENO)
        pyautogui.write(data_abate)
        sleep(TEMPO_ESPERA_PEQUENO)

    except Exception as e:
        registrar_log(e, 'função inserir_abate')

# Função para executar
def executar():
    try:

        keyboard.press_and_release('f3')
        sleep(TEMPO_ESPERA_ALTO)

    except Exception as e:
        registrar_log(e, 'função executar')
        
# Função para restaurar o layout
def restaurar_layout():
    try:

        pyautogui.click(422, 156, duration=2)
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função restaurar_layout')
        
# Função para gravar o layout
def gravar_layout():
    try:

        pyautogui.click(395, 151, duration=2)
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função gravar_layout')
        
# Função para atualizar o layout
def atualizar_layout():
    try:

        pyautogui.click(48, 151, duration=2)
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função atualizar_layout')
        
# Função para abrir a pré-visualização
def pre_visualizar():
    try:

        pyautogui.click(103, 152, duration=2)
        sleep(TEMPO_ESPERA_LONGO)

    except Exception as e:
        registrar_log(e, 'função pre_visualizar')
        
# Função para abrir page setup e configurar no modo retrato
def page_setup_retrato():
    try:

        pyautogui.click(219, 57, duration=2)
        sleep(TEMPO_ESPERA_LONGO)
        pyautogui.click(886, 288, duration=2)
        sleep(TEMPO_ESPERA_MEDIO)
        pyautogui.click(901, 527, duration=2)
        sleep(TEMPO_ESPERA_LONGO)

    except Exception as e:
        registrar_log(e, 'função page_setup_retrato')
        
# Função para imprimir 
def imprimir():
    try:

        pyautogui.click(167, 55, duration=2)
        sleep(TEMPO_ESPERA_MEDIO)
        pyautogui.click(795, 595, duration=2)
        sleep(TEMPO_ESPERA_MEDIO)

    except Exception as e:
        registrar_log(e, 'função imprimir')
        

# Função para salvar o relatório
def salvar_relatorio(nome_arquivo):
    try:

        pyautogui.write(nome_arquivo)
        sleep(TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('enter')
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função salvar_relatorio')
        

# Função para fechar a pré-visualização
def fechar_pre_visualizar():
    try:

        pyautogui.click(756, 55, duration=2)
        sleep(TEMPO_ESPERA_CURTO)
        
    except Exception as e:
        registrar_log(e, 'função fechar_pre_visualiza')
        

# Função para fechar a guia
def fechar_guia():
    try:

        pyautogui.click(148, 126, duration=2)
        pyautogui.click(160, 126, duration=2)
        sleep(TEMPO_ESPERA_CURTO)

    except Exception as e:
        registrar_log(e, 'função fechar_guia')