import requests
import json

# Códigos das cidades (completados com 5 dígitos)
cidades_ma = {
    'São Luís': '09210',
    'Imperatriz': '08036',
}

cidades_outros = {
    'Manaus': ('am', '02550'),
    'Salvador': ('ba', '38490'),
    'Fortaleza': ('ce', '13897'),
    'Belo Horizonte': ('mg', '41238'),
    'Belém': ('pa', '04278'),
    'Curitiba': ('pr', '75353'),
    'Rio de Janeiro': ('rj', '60011'),
    'Porto Alegre': ('rs', '88013'),
    'São Paulo': ('sp', '71072'),
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

# Dicionários para armazenar os dados de todas as cidades
dados_formatados_ma = []
dados_completos_ma = {}  # Dicionário para armazenar os dados completos

# Iterando sobre as cidades do Maranhão para obter e formatar os dados
uf_ma = 'ma'  # Unidade Federativa do Maranhão
for cidade, codigo in cidades_ma.items():
    urnas_apuradas = get_urnas_apuradas(uf_ma, codigo)
    if urnas_apuradas:
        dados_completos_ma[cidade] = urnas_apuradas  # Salvando os dados completos
        try:
            dados_formatados_ma.append(formatar_dados(cidade, urnas_apuradas))
            print(f"Dados processados para {cidade}.")
        except KeyError as e:
            print(f"Erro ao processar dados da cidade {cidade}: {e}")

# Criando o JSON com uma única linha para as cidades do Maranhão
resultado_ma = " | ".join(dados_formatados_ma)

# Salvando o resultado formatado no arquivo SLZ_ITZ_resultado_urnas.json
resultado_json_ma = {"resultado": resultado_ma}
with open('SLZ_ITZ_resultado_urnas.json', 'w', encoding='utf-8') as json_file:
    json.dump(resultado_json_ma, json_file, ensure_ascii=False)

# Salvando os dados completos da API no arquivo apiTse.json
with open('SLZ_ITZ_apiTse.json', 'w', encoding='utf-8') as api_file:
    json.dump(dados_completos_ma, api_file, ensure_ascii=False)

print("Dados formatados e salvos no arquivo SLZ_ITZ_resultado_urnas.json")
print("Dados completos salvos no arquivo SLZ_ITZ_apiTse.json")

# Parte para outras capitais
dados_formatados_outros = []
dados_completos_outros = {}  # Dicionário para armazenar os dados completos

# Iterando sobre as cidades para obter e formatar os dados
for cidade, (uf, codigo) in cidades_outros.items():
    urnas_apuradas = get_urnas_apuradas(uf, codigo)
    if urnas_apuradas:
        dados_completos_outros[cidade] = urnas_apuradas  # Salvando os dados completos
        try:
            dados_formatados_outros.append(formatar_dados(cidade, urnas_apuradas))
            print(f"Dados processados para {cidade}.")
        except KeyError as e:
            print(f"Erro ao processar dados da cidade {cidade}: {e}")

# Criando o JSON com uma única linha para as outras capitais
resultado_outros = " | ".join(dados_formatados_outros)

# Salvando o resultado formatado no arquivo outras_capitais.json
resultado_json_outros = {"resultado": resultado_outros}
with open('outras_capitais.json', 'w', encoding='utf-8') as json_file:
    json.dump(resultado_json_outros, json_file, ensure_ascii=False)

# Salvando os dados completos da API no arquivo apiTse_outras.json
with open('outras_capitais_apiTse.json', 'w', encoding='utf-8') as api_file:
    json.dump(dados_completos_outros, api_file, ensure_ascii=False)

print("Dados formatados e salvos no arquivo outras_capitais.json")
print("Dados completos salvos no arquivo outras_capitais_apiTse.json")
