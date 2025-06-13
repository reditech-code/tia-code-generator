

import keyboard     # Biblioteca para simular um teclado
import time         # Biblioteca praa gerar delay
import openpyxl     # Biblioteca para abrir/ler/editar arquivos excel
import os           # Biiblioteca para conseguir usar endereçamento de diretórios relativamente a pasta aonde o programa esta salvo 
import pyperclip    # Biblioteca para conseguir o valor selecionado


# Atribuindo o valor do diretório atual na variavel current_directory
current_directory = os.getcwd()

# Diretório dos arquivos de programa montados com relativismo ao diretório dos arquivos de referência
file_path_mapa_de_memoria = os.path.join("C:\\Users\\Reditech\Desktop\\LISTA DE ELEMENTOS.xlsx")

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

# Definição de strings de controle das colunas dentro do arquivo excel
tag_name = "CODIGO KKS (TAG)"
tipo_controle = "BLOCO DE CONTROLE"
fc_db_number = "DB"

# Chamada da função de leitura de do arquivo de excel
tag_data = read_column(file_path_mapa_de_memoria, tag_name, 'LISTA DE MEMORIA')
tipo_controle_data = read_column(file_path_mapa_de_memoria, tipo_controle, 'LISTA DE MEMORIA')
fc_db_number_data = read_column(file_path_mapa_de_memoria, fc_db_number, 'LISTA DE MEMORIA')

# Trocando de janela
keyboard.press('alt')
keyboard.press_and_release('tab')
time.sleep(0.1)
keyboard.release('alt')
time.sleep(0.3)

# Iniciando a alteração de nome de arquivo
keyboard.press_and_release("F2")
time.sleep(0.5)

def find_value(array, value):
    for i in range(len(array)):
        arrayFC = ("FC"+str(array[i]))
        arrayDB = ("DB"+str(array[i]))
        if arrayFC == value:
            return i, "FC"
        elif arrayDB == value:
            return i, "DB"
    return -1, -1


time.sleep(0.2)

keyboard.press('ctrl')
keyboard.press_and_release('c')
keyboard.release('ctrl')
time.sleep(0.1)
selectedText = pyperclip.paste()

time.sleep(0.2)

j, TIPO = find_value(fc_db_number_data, selectedText)
if j != -1:
    if TIPO == "FC":
        print("FC_"+tag_data[j])
        keyboard.write("FC_"+tag_data[j])
        keyboard.press_and_release('enter')
    
    if TIPO == "DB":
        print("DB_"+tag_data[j])
        keyboard.write("DB_"+tag_data[j])
        keyboard.press_and_release('enter')