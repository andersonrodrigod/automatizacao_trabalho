import re

questiona_texto = ["POSSUI", "SE POSSUI", "CHECAR", "CHECAR SE", "VERIFICAR", "VERIFICAR SE", "REALIZOU", "SE REALIZOU"]

def separar_questionamento(texto, questiona_texto):
    # Cria um padrão regex com todas as palavras-chave unidas por "|"
    padrao = rf"([^.?]*\b(?:{'|'.join(map(re.escape, questiona_texto))})\b[^.?]*[.?])"
    
    # Busca o padrão no texto
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(0).strip()
    return None

# Exemplo de uso
texto = "POSSUI LISTA DE MATERIAL?? SOLICITAR CARTA DE HONORARIOS MEDICOS + ELETRONEUROMIOGRAFIA + APLICAR QUESTIONARIO DE COLUNA + APOS, SOLICITAR PARECER PARA ORTOPEDISTA DE COLUNA E NEUROCIRURGIA. ITM"

frase_encontrada = separar_questionamento(texto, questiona_texto)
if frase_encontrada:
    print("Frase encontrada:", frase_encontrada)
else:
    print("Nenhuma palavra-chave encontrada.")
