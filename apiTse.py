import requests
import json

# Códigos das cidades (completados com 5 dígitos)
cidades = {
    'Imperatriz': '08036',
    'Balsas': '07277',
    'Timon': '09377',
    'Caxias': '07579',
    'São Luís': '09210',
}

# Função para construir a URL e buscar os dados
def get_urnas_apuradas(uf, codigo_cidade):
    url = f'https://resultados-sim.tse.jus.br/simulado/ele2024/10143/dados/{uf}/{uf}{codigo_cidade}-c0011-e010143-u.json'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # Dados retornados em JSON
            return data
        else:
            print(f"Erro {response.status_code} ao obter dados da cidade {codigo_cidade}")
    except Exception as e:
        print(f"Erro ao conectar à API: {e}")

# Dicionário para armazenar os dados de todas as cidades
dados_urnas = {}

# Iterando sobre as cidades para obter dados de cada uma
uf = 'ma'  # Unidade Federativa do Maranhão
for cidade, codigo in cidades.items():
    urnas_apuradas = get_urnas_apuradas(uf, codigo)
    if urnas_apuradas:
        dados_urnas[cidade] = urnas_apuradas  # Armazenando os dados da cidade no dicionário
        print(f"Conexão para obter dados de urnas apuradas para {cidade} concluída.")

# Salvando os dados no arquivo JSON
with open('apiTse.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados_urnas, json_file, ensure_ascii=False, indent=4)

print("Dados salvos no arquivo apiTse.json")
