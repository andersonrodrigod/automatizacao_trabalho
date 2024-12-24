import pandas as pd
import re



def processar_data(texto):
    datas_validas = re.findall(r"\b\d{2}[-/:]\d{2}\b", texto)

    if not datas_validas:
        return "Nenhuma data válida encontrada"
    
    ultima_data = datas_validas[-1]

    parte_texto = texto.split(ultima_data, 1)
    texto_pos_ultima_data = parte_texto[1] if len(parte_texto) > 1 else ""

    return texto_pos_ultima_data

def substituir_texto(texto, substituicoes):
    for chave, valor in substituicoes.items():
        if chave in texto:
            texto = texto.replace(chave, valor) 
    return texto

def deletar_texto(texto, delete_texto):
    for item in delete_texto:
        if item in texto:  
            texto = texto.split(item, 1)[0]
    texto = retirar_palavras_extras(texto)  
    return texto

def retirar_palavras_extras(texto):
    return texto.rstrip(" +")

def separar_questionamento(texto, questiona_texto):
    padrao = rf"([^.?]*\b(?:{'|'.join(map(re.escape, questiona_texto))})\b[^.?]*[.?]+)"   
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(0).strip()
    return None

def remover_duplicatas_texto_editado(texto, retirar_texto):
    if retirar_texto in texto:
        texto = texto.replace(retirar_texto, "").strip()
    return texto

def filtrar_nome(df, nome):
    return df[df["nome"] == nome].drop_duplicates(subset="nome", keep="first")
  
def processar_texto(info_medico, substituicoes, delete_texto):
    texto_editado = processar_data(info_medico)
    texto_editado = deletar_texto(texto_editado, delete_texto)
    texto_editado = substituir_texto(texto_editado, substituicoes)
    frase_encontrada = separar_questionamento(texto_editado, questiona_texto)
    
    if frase_encontrada:
        texto_editado = remover_duplicatas_texto_editado(texto_editado, frase_encontrada)
        return [frase_encontrada, texto_editado]
    else:
        return texto_editado
    
        

nome = "CLAUDIO SERGIO QUINTEIRO"

df = pd.read_json("./dados/dados_coletados.json", encoding="utf-8")

filtrar_bf = df[df["nome"] == nome]

bf = filtrar_nome(df, nome)

substituicoes = {
    "TC": "TOMOGRAFIA DE",
    "RM": "RESSONÂNCIA DE",
    "RMN": "RESSONÂNCIA DE",
    "RX": "RAIO-X DE",
    "USG": "ULTRASSOM DE",
    "US": "ULTRASSOM DE",
    "ANEXAR": "",
    "ITM": "",
    "OCT": "TOMOGRAFICA DE OCOERENCIA OPTICA",
    "LESALES": "",
    "SOLICITAR": "",
    "APLICAR": "PREENCHER",
    " ,": "",
    ",": "",
    ", ": "",
    ". ": "",
    " .": "",
    ": ": "",
    " :": "",
    "+": ",",
    " - ": "",   
}

delete_texto = [
    "APOS SOLICITAR", "APOSSOLICITAR", "APOS, SOLICITAR PARECER", "APOS,SOLICITAR", 
    "APOS. SOLICITAR", "APOS.SOLICITAR", "E APOS SOLICITAR", "E APOS, SOLICITAR", 
    "CASO NAO POSSUA, SOLICITAR", "CASO POSSUA, SOLICITAR", 
    "+ APOS SOLICITAR", "+ APOS, SOLICITAR", "+APOS SOLICITAR", "+APOS, SOLICITAR"
]

questiona_texto = ["POSSUI", "SE POSSUI", "CHECAR", "CHECAR SE", "VERIFICAR", "VERIFICAR SE", "REALIZOU", "SE REALIZOU"]

if not bf.empty:
    info_medico = bf["info_medico"].iloc[0]
    texto_editado = processar_texto(info_medico, substituicoes, delete_texto)

print(texto_editado)

def resultado():
    return texto_editado

