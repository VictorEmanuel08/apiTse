import requests
import json

# Códigos das cidades
cidades = {
    'São Luís': '09210',
    'Imperatriz': '08036',
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

# Função para extrair os dados necessários e formatar em uma linha única
def formatar_dados(cidade, dados):
    # Acessando o percentual de urnas apuradas
    try:
        urnas_apuradas = dados['s']['pst']  # o valor que representa o percentual de urnas apuradas
    except KeyError:
        urnas_apuradas = "N/A"
    
    candidatos_info = []
    
    # Navegando nos dados para pegar informações dos candidatos
    for grupo in dados['carg'][0]['agr']:
        for partido in grupo['par']:
            for candidato in partido['cand']:
                nome_candidato = candidato['nm']
                percentual_votos = candidato['pvap']
                candidatos_info.append(f"{nome_candidato} ({percentual_votos}%)")
    
    # Formatando a string final para a cidade
    candidatos_formatado = " - ".join(candidatos_info)
    return f"{cidade} ({urnas_apuradas}% das urnas apuradas): {candidatos_formatado}"

# Dicionário para armazenar os dados de todas as cidades
dados_formatados = []
dados_completos = {}  # Dicionário para armazenar os dados completos

# Iterando sobre as cidades para obter e formatar os dados
uf = 'ma'  # Unidade Federativa do Maranhão
for cidade, codigo in cidades.items():
    urnas_apuradas = get_urnas_apuradas(uf, codigo)
    if urnas_apuradas:
        dados_completos[cidade] = urnas_apuradas  # Salvando os dados completos
        try:
            dados_formatados.append(formatar_dados(cidade, urnas_apuradas))
            print(f"Dados processados para {cidade}.")
        except KeyError as e:
            print(f"Erro ao processar dados da cidade {cidade}: {e}")

# Criando o JSON com uma única linha
resultado = " | ".join(dados_formatados)

# Salvando o resultado formatado no arquivo resultado_urnas.json
resultado_json = {"resultado": resultado}
with open('SLZ_ITZ_resultado_urnas.json', 'w', encoding='utf-8') as json_file:
    json.dump(resultado_json, json_file, ensure_ascii=False)

# Salvando os dados completos da API no arquivo apiTse.json
with open('apiTse.json', 'w', encoding='utf-8') as api_file:
    json.dump(dados_completos, api_file, ensure_ascii=False)

print("Dados formatados e salvos no arquivo resultado_urnas.json")
print("Dados completos salvos no arquivo apiTse.json")
