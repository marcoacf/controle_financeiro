import pandas as pd

def validar_lancamento(dado):
    """
    Valida os dados de um lançamento financeiro.
    Retorna (True, "") se válido, ou (False, "mensagem de erro") se inválido.
    """
    if dado.get("Valor", 0) < 0:
        return False, "O valor não pode ser negativo."
    if not dado.get("Mes_Ref"):
        return False, "O campo 'Mes_Ref' é obrigatório."
    if not isinstance(dado.get("Parcela", 1), int) or dado["Parcela"] < 1:
        return False, "O número da parcela deve ser um inteiro positivo."
    return True, ""

def formatar_mes_ref(data):
    """
    Recebe uma data e retorna o mês de referência no formato AAAA-MM.
    """
    if isinstance(data, pd.Timestamp):
        return data.strftime("%Y-%m")
    elif isinstance(data, str):
        try:
            return pd.to_datetime(data).strftime("%Y-%m")
        except:
            return ""
    return ""