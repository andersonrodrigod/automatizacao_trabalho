import re

texto_original = "13/12 ANEXAR ACUIDADE VISUAL E OCT COM IMAGENS. APOS, SOLICITAR PARECER PARA OFTALMO. ITM"

def last_data():
    datas = re.findall(r'\b\d{1,2}/\d{1,2}\b', texto_original)

    valores = []
    for data in datas:
        dia, mes = map(int, data.split('/'))
        valores.append((mes, dia))

    maior_data = max(valores)

    maior_data_formatada = f"{maior_data[1]:02}/{maior_data[0]:02}"

    indice_inicio = texto_original.index(maior_data_formatada)
    resultado = texto_original[indice_inicio + len(maior_data_formatada):].strip()

    return resultado


texto_original = last_data()

substituicoes = {
    "TC": "TOMOGRAFIA DE",
    "RM": "RESSONÂNCIA DE",
    "RMN": "RESSONÂNCIA DE",
    "RX": "RAIO-X DE",
    "USG": "ULTRASSOM DE",
    "US": "ULTRASSOM DE",
    "ANEXAR": "",
    "ITM": "",
    "+": ",",
    "OCT": "TOMOGRAFICA DE OCOERENCIA OPTICA" 
}

texto_posterior = ["APOS", "VERIFICAR", "CHECAR"]

def processar_texto():
    texto_solicito = ""
    texto_questiona = ""
    texto_intermediario = None
    for item in texto_posterior:
        if item in texto_original:
            partes = texto_original.split(item)
            if len(partes) == 2:
                antes = partes[0].strip()
                depois = partes[1].strip()
                intermediarias = []
                texto_solicito = antes
                texto_questiona = depois
            elif len(partes) > 2:
                antes = partes[0].strip()
                intermediarias = [parte.strip() for parte in partes[1: -1]]
                depois = partes[-1].strip()
                texto_solicito = antes
                texto_intermediario = intermediarias if intermediarias else None
                texto_questiona = depois

        result = (texto_solicito, texto_intermediario, texto_questiona)
        if texto_intermediario is None:
            result = (texto_solicito, texto_questiona)
    return result
executar_func = False  
    
for palavra in texto_posterior:
    if palavra in texto_original:
        executar_func =  True

if executar_func == True:
    final = processar_texto()


print(final)
          


texto_questiona_incial = "auditoria questiona"

texto_cobra_exame = "exames de"
texto = texto_cobra_exame + texto_original

for chave, substituicao in substituicoes.items():
    if chave in texto_original:
        texto_original = texto_original.replace(chave, substituicao)
        texto = texto_cobra_exame + texto_original
    
texto_inicial = "auditoria está solicitando"
texto_final = "para dar continuidade a análise do procedimento"

print(f"{texto_inicial} {texto} {texto_final}")

