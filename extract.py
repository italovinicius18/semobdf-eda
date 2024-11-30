import requests
from geopandas import GeoDataFrame
import os
import warnings
warnings.filterwarnings('ignore')

# URL da API
url = "https://geoserver.semob.df.gov.br/geoserver/semob/ows"


datasets = {
    "frota_por_operadora": "semob:Frota por Operadora",
    "horarios_linhas": "semob:Horários das Linhas",
    "linhas_onibus": "semob:Linhas de onibus",
    "paradas_onibus": "semob:Paradas de onibus",
    "ultima_posicao": "semob:Ultima Posicao Transmitida",
}

def request_data(dataset: str) -> GeoDataFrame:
    # Parâmetros da requisição
    params = {
        "service": "WFS",
        "version": "1.0.0",
        "request": "GetFeature",
        "typeName": datasets[dataset],
        "outputFormat": "application/json",
    }

    response = requests.get(url, params=params, verify=False)

    os.makedirs("data", exist_ok=True)

    # Save to file as GeoJSON
    with open(f"data/{dataset}.geojson", "w") as f:
        f.write(response.text)

    # return GeoDataFrame.from_features(response.json())

for k in datasets.keys():
    print(f"Requesting data for dataset: {k}")
    request_data(k)

    # print(gdf.shape)

    # print(gdf.head())

    # print(gdf.info())

    # print(gdf.columns)

    # # Save to file as GeoJSON
    # gdf.to_file(f"{k}.geojson", driver="GeoJSON")