import re


def processar_data(texto):
    datas_validas = re.findall(r"\b\d{2}[-/:]\d{2}\b", texto)

    if not datas_validas:
        return "Nenhuma data válida encontrada"
    
    ultima_data = datas_validas[-1]

    parte_texto = texto.split(ultima_data, 1)
    texto_pos_ultima_data = parte_texto[1] if len(parte_texto) > 1 else ""

    return texto_pos_ultima_data

def remover_datas(texto):
    
    texto_sem_datas = re.sub(r"\b\d{2}[-/:]\d{2}[-/:](20|21|22|23|24|25)\b[^\w\s]*", "", texto)

    texto = texto_sem_datas.strip()

    return texto


