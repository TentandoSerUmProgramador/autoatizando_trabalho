# Bibliotecas 
import pyautogui
from time import sleep
import keyboard
import funcoes_de_acoes
from salvar_enderecamento_sintetico import LISTA_CMC_UTILIZADA, NOME_CAMARAS

# Constantes com nome do relátorio
CAMARA_RELATORIO_ANALITICO = "Endereçamento e registo pH "

# Função para salvar relatório e endereçamente de carcaças modo analítico
def salvar_analitico(data_abate):
    try:

        # Selecionar analitico
        pyautogui.click(193, 207, duration=2)
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        pyautogui.write('1')
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
        keyboard.press_and_release('enter')
        sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)

        funcoes_de_acoes.inserir_abate(data_abate)
        funcoes_de_acoes.executar()
        funcoes_de_acoes.restaurar_layout()
        
        # Ordena sequencial
        pyautogui.click(120, 270, duration=1)
        
        funcoes_de_acoes.gravar_layout()
        funcoes_de_acoes.fechar_guia()
    
        # Percore a lista para salvar relatório analitico de cada câmara utilizado no dia
        for cod_camara, nome_camara in NOME_CAMARAS.items():

            if nome_camara in LISTA_CMC_UTILIZADA:        
                # Inserir código camara
                pyautogui.doubleClick(70, 352, duration=2)
                keyboard.press_and_release('ctrl+a')
                sleep(funcoes_de_acoes.TEMPO_ESPERA_CURTO)
                pyautogui.write(cod_camara)
                
                funcoes_de_acoes.executar()

                # Condição para remover grid de pH/pHmetro/Desvio caso seja câmara sequestro
                if(cod_camara == '10'):
                    for _ in range(3):

                        pyautogui.click(440, 270, duration=1, button='right')
                        pyautogui.click(480, 410, duration=1)
        
                funcoes_de_acoes.pre_visualizar()
                funcoes_de_acoes.page_setup_retrato()
                funcoes_de_acoes.imprimir()
                funcoes_de_acoes.salvar_relatorio(nome_arquivo = CAMARA_RELATORIO_ANALITICO + NOME_CAMARAS[cod_camara] + " Abate -" + data_abate.replace('/', '-'))
                funcoes_de_acoes.fechar_pre_visualizar()
                funcoes_de_acoes.fechar_guia()
                
                # Deletar dados das câmaras usadas para ser amarzenado novo valores
                del(LISTA_CMC_UTILIZADA, NOME_CAMARAS)

            else:
                pass
            
    except Exception as e:
        funcoes_de_acoes.registrar_log(e,'função salvar_endereçamento_analitico')