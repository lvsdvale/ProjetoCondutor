import googlemaps as gmaps
from googlemaps import directions
import pandas as pd


API_KEY = 'AIzaSyChQK0qiIuwHzFZ1VEioEmxraqNugGUvk0'


class Estado:
    def __init__(self, nome, adress, tempo):
        self.nome = nome
        self.endereco = adress
        self.tempo = tempo

    def __str__(self):
        return self.nome


def df_inicial(path):
    return pd.read_csv(path)


def retorna_tempo(from_adress, to_adress):
    client = gmaps.client.Client(key=API_KEY)
    direction = directions.directions(
        client=client,
        origin=from_adress,
        destination=to_adress,
        mode="driving",
        optimize_waypoints=True,
        language="Portuguese",
    )
    return direction[0]["legs"][0]["duration"]['value']


def cria_grafo(estado_atual, df):
    grafo = {}
    for i in range(len(df)):
        tempo = retorna_tempo(estado_atual.endereco, df["Endereço"][i])
        estado = Estado(nome=df["Unidade"][i], adress=df["Endereço"][i], tempo=tempo)
        grafo[estado.nome] = estado
    return grafo


def busca(estado_atual, df):
    df_auxiliar = df.loc[lambda x:x["Endereço"] != estado_atual.endereco]
    df = df_auxiliar
    df.reset_index(inplace=True, drop=True)
    if df.empty:
        proximo = Estado(nome="Rodoviaria",
                         adress="Av. Presidente Affonso Camargo, 330",
                         tempo=retorna_tempo(
                             from_adress=estado_atual.endereco,
                             to_adress="Av. Presidente Affonso Camargo, 330")
                         )
    else:
        proximo = None
        grafo = cria_grafo(estado_atual=estado_atual, df=df)
        for chave in grafo.keys():
            if proximo is None:
                proximo = grafo[chave]
            else:
                if proximo.tempo > grafo[chave].tempo:
                    proximo = grafo[chave]

    return proximo, df


estado_atual = Estado(
    nome="Rodoviaria",
    adress="Av. Presidente Affonso Camargo, 330",
    tempo=0
    )
df = df_inicial("Tabela_Unidades.csv")
print(f"Endereço Inicial:{estado_atual.nome}\nEndereço:{estado_atual.endereco}\n")
sum_tempo = 0
while not df.empty:
    estado_atual, df = busca(estado_atual=estado_atual, df=df)
    tmp = int(estado_atual.tempo / 60)
    resto = estado_atual.tempo % 60
    estimado = f"{tmp} minutos e {resto} segundos"
    sum_tempo += estado_atual.tempo
    print(f"Próxima parada:{estado_atual.nome}\nEndereço:{estado_atual.endereco}\nTempo Estimado:{estimado}\n")

tmp = int(sum_tempo / 60)
resto = sum_tempo % 60
print(f"O tempo estimado das entregas foram de {tmp} minutos e {resto} segundos")
