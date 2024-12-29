
def filtrar_nome(df, nome):
    return df[df["nome"] == nome].drop_duplicates(subset="nome", keep="first")
