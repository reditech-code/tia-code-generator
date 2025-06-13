
################################################################################################################################################
# FERRAMENTA PARA RENOMEAR TODOS OS BLOCOS NO TIA PORTAL
# DATA DE INICIO: 27/01/2025
# AUTOR: WNC
# Versão 0 - 27/01/2025 - Versão Inicial

################################################################################################################################################
# INSTRUÇÕES DE USO
#
# TENHA CERTEZA QUE A LISTA DE ELEMENTOS.XLSX ESTÁ NA PASTA "C:\Users\Reditech\Desktop\Gerador de códigos " E COM O NOME EXATEMENTE COMO "LISTA DE ELEMENTOS.XLSX"
# ABRIR O TIA PORTAL E GERAR OS BLOCOS
# COM OS BLOCOS GERADOS, CLICAR EM QUALQUER BLOCO GERADO E RODAR O PROGRAMA (DE PREFERÊNCIA, ESCOLHER O PRIMEIRO BLOCO A SER RENOMEADO DE CIMA PARA BAIXO)
# NÃO MEXER NO TECLADO E NEM NO MOUSE ATÉ O FIM DA EXECUÇÃO DO PROGRAMA

################################################################################################################################################

import keyboard     # Biblioteca para simular um teclado
import time         # Biblioteca praa gerar delay
import openpyxl     # Biblioteca para abrir/ler/editar arquivos excel
import os           # Biiblioteca para conseguir usar endereçamento de diretórios relativamente a pasta aonde o programa esta salvo 
import pyperclip    # Biblioteca para conseguir o valor selecionado

# Atribuindo o valor do diretório atual na variavel current_directory
current_directory = os.getcwd()
print("Diretório relativo: ", current_directory)

# Diretório dos arquivos de programa montados com relativismo ao diretório dos arquivos de referência
file_path_mapa_de_memoria = os.path.join(current_directory, "LISTA DE ELEMENTOS.xlsx")
print("Diretório lista: ", file_path_mapa_de_memoria)
#file_path_mapa_de_memoria = os.path.join("C:\\Users\\Reditech\\Desktop\\LISTA_DE_ELEMENTOS.xlsx")
#current_directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_column(file_path, column_name, columm_name_check):
    wb = openpyxl.load_workbook(file_path)
    
    sheet = wb[columm_name_check]
    column_index = {}

    for cell in sheet[1]:
        column_index[cell.value] = cell.column

    if column_name not in column_index:
        print(f"Column '{column_name}' not found.")
        return []
    
    column_values = []
    column_letter = openpyxl.utils.get_column_letter(column_index[column_name])
    for cell in sheet[column_letter]:
            if (cell.value) != column_name:
                column_values.append(cell.value)
    return column_values

def find_value(array, value):
    for i in range(len(array)):
        arrayFC = ("FC"+str(array[i]))
        arrayDB = ("DB"+str(array[i]))
        if arrayFC == value:
            return i, "FC"
        elif arrayDB == value:
            return i, "DB"
    return -1, -1

# Definição de strings de controle das colunas dentro do arquivo excel
tag_name = "CODIGO KKS (TAG)"
tipo_controle = "BLOCO DE CONTROLE"
fc_db_number = "DB"

# Chamada da função de leitura de do arquivo de excel
tag_data = read_column(file_path_mapa_de_memoria, tag_name, 'LISTA DE MEMORIA')
tipo_controle_data = read_column(file_path_mapa_de_memoria, tipo_controle, 'LISTA DE MEMORIA')
fc_db_number_data = read_column(file_path_mapa_de_memoria, fc_db_number, 'LISTA DE MEMORIA')

# inicializando variavel selectedText e selectedText_prev
selectedText = ""
selectedText_prev = ""
end_bit = 0

# Trocando de janela
keyboard.press('alt')
keyboard.press_and_release('tab')
time.sleep(0.1)
keyboard.release('alt')
time.sleep(0.3)

while True:   

    if keyboard.is_pressed('shift'):
        print("Shift pressed. Exiting program.")
        break
   
    if end_bit == 1:
        print("Exiting program.")
        break

    end_bit = 1

    while selectedText == selectedText_prev:
        time.sleep(0.2)
        keyboard.press_and_release("F2")
        time.sleep(0.2)
        keyboard.press('ctrl')
        keyboard.press_and_release('c')
        keyboard.release('ctrl')
        time.sleep(0.1)
        selectedText = pyperclip.paste()
        time.sleep(0.1)

        if selectedText != selectedText_prev:
            selectedText_prev = selectedText
        else:
            print("Exiting program")
            break

        j, TIPO = find_value(fc_db_number_data, selectedText)
        if j != -1:
            end_bit = 0
            if TIPO == "FC":
                print("FC_"+tag_data[j])
                keyboard.write("FC_"+tag_data[j])
                keyboard.press_and_release('enter')
        
            if TIPO == "DB":
                print("DB_"+tag_data[j])
                keyboard.write("DB_"+tag_data[j])
                keyboard.press_and_release('enter')

        if keyboard.is_pressed('shift'):
            print("Shift pressed. Exiting program.")
            break
        keyboard.press_and_release('esc')
        time.sleep(0.2)
        keyboard.press_and_release('down')

    if end_bit == 1:
        print("Exiting program.")
        break
    else:
        end_bit = 1

    while selectedText != "Main":
        time.sleep(0.2)
        keyboard.press_and_release('up')
        time.sleep(0.2)       
        keyboard.press_and_release("F2")
        time.sleep(0.2)
        keyboard.press('ctrl')
        keyboard.press_and_release('c')
        keyboard.release('ctrl')
        time.sleep(0.1)
        selectedText = pyperclip.paste()
        time.sleep(0.1)
        
        j, TIPO = find_value(fc_db_number_data, selectedText)
        if j != -1:
            end_bit = 0
            if TIPO == "FC":
                print("FC_"+tag_data[j])
                keyboard.write("FC_"+tag_data[j])
                keyboard.press_and_release('enter')
        
            if TIPO == "DB":
                print("DB_"+tag_data[j])
                keyboard.write("DB_"+tag_data[j])
                keyboard.press_and_release('enter')

        keyboard.press_and_release('esc')
    

        if keyboard.is_pressed('shift'):
            print("Shift pressed. Exiting program.")
            break

    if end_bit == 1:
        print("Exiting program.")
        break