# Bibliotecas 
import pyautogui
from time import sleep
import pyperclip
import keyboard
import funcoes_de_acoes


# Constantes com nome do relátorio e lista para amarzana dados das camaras utilizadas no dia
NOME_CAMARAS = {'4': 'CMC-01', '5': 'CMC-02', '6': 'CMC-03',
                '7': 'CMC-04','8': 'CMC-05','21': 'CMC-06', 
                '22': 'CMC-07', '10': 'CÂMARA SEQUESTRO'}

LISTA_CMC_UTILIZADA = []
CAMARA_RELATORIO_SINTETICO = "Endereçamento e registo pH(Sintetico) Abate - "


# Função para salvar relatório de endereçamente de carcaças modo sintético
def salvar_sintetico(data_abate):
    try:

        # Deleta Codigo câmara usado anteriormente
        pyautogui.click(x=17, y=358, duration=1)
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        pyautogui.click(x=17, y=358)
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('ctrl+delete')
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('enter')

        # Selecionar sintético
        pyautogui.click(193, 207, duration=2)
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        pyautogui.write('2')
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('enter')
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)

        funcoes_de_acoes.inserir_abate(data_abate)
        funcoes_de_acoes.executar()
        funcoes_de_acoes.restaurar_layout()

        # Ordena câmara
        pyautogui.click(250,260, duration=1)

        funcoes_de_acoes.gravar_layout()
        funcoes_de_acoes.atualizar_layout()

        # Habilita copiar
        pyautogui.click(111,284, duration=1, button='right')
        pyautogui.click(130,315, duration=1)

        # Posição inicial para açoes do mauser
        linha_x  = 111
        linha_y  = 286
        linha_x2 = 130
        linha_y2 = 292

        global LISTA_CMC_UTILIZADA
        
        # Copia as camaras pra adicionar em uma lista e depois formatar string para saber quais das 7 câmaras devem ser salvo no analitico
        for _ in range(8):

                pyautogui.click(linha_x, linha_y, duration=1, button='right')
                pyautogui.click(linha_x2, linha_y2, duration=1)
                
                # Adicionando valores nas vaiaveis para mudar posição aonde terá ação do mauser
                linha_y  += 20
                linha_y2 += 22

                valor_copiado = pyperclip.paste().split('/')
                LISTA_CMC_UTILIZADA.append(valor_copiado[0])

        # Organizando informações coletadas para serem utilizadas na fução salva_enderecamento_analitico
        LISTA_CMC_UTILIZADA = set(LISTA_CMC_UTILIZADA)
        LISTA_CMC_UTILIZADA = list(LISTA_CMC_UTILIZADA)
        LISTA_CMC_UTILIZADA = [item.rstrip() for item in LISTA_CMC_UTILIZADA]
        
        # Termina de salvar endereçamento sintético
        funcoes_de_acoes.pre_visualizar()
        funcoes_de_acoes.imprimir()
        funcoes_de_acoes.salvar_relatorio(nome_arquivo = CAMARA_RELATORIO_SINTETICO + data_abate.replace('/', '-'))
        funcoes_de_acoes.fechar_pre_visualizar()
        funcoes_de_acoes.fechar_guia()

    except Exception as e:
        funcoes_de_acoes.registrar_log(e,'função salvar_endereçamento_sintético')