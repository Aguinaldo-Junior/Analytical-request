# Função para tipagem de dados 
def tipagem_dados(df, schema):
    import pandas as pd
    
    for col, tipo in schema.items():
        if col not in df.columns:
            continue

        if tipo == "str":
            df[col] = df[col].astype("string")

        elif tipo == "bool":
            df[col] = df[col].astype("bool")

        elif tipo == "int":
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

        elif tipo == "float":
            df[col] = pd.to_numeric(df[col], errors="coerce")

        elif tipo == "datetime":
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df
        