import requests
import json
import time
import os

# Definindo os caminhos de salvamento
save_path_remote = r"\\viena02\Public\Victor\apiTse"
save_path_local = os.path.join(os.getcwd(), 'json')  # Pasta local chamada 'json'

# Códigos das cidades (completados com 5 dígitos)
slz_itz = {
    'São Luís': '09210',
    'Imperatriz': '08036',
}

# Códigos das cidades (completados com 5 dígitos)
cidades_ma = {
    "AFONSO CUNHA": "07013",
    "AGUA DOCE DO MARANHÃO": "07005",
    "ALCÂNTARA": "07030",
    "ALDEIAS ALTAS": "07056",
    "ALTAMIRA DO MARANHÃO": "07072",
    "ALTO ALEGRE DO MARANHÃO": "07021",
    "ALTO ALEGRE DO PINDARÉ": "07048",
    "ALTO PARNAÍBA": "07099",
    "AMAPÁ DO MARANHÃO": "07080",
    "AMARANTE DO MARANHÃO": "07110",
    "ANAJATUBA": "07137",
    "ANAPURUS": "07153",
    "APICUM-AÇU": "07064",
    "ARAGUANÃ": "07102",
    "ARAIOSES": "07170",
    "ARAME": "09679",
    "ARARI": "07196",
    "AXIXÁ": "07218",
    "AÇAILÂNDIA": "09610",
    "BACABAL": "07234",
    "BACABEIRA": "07129",
    "BACURI": "07250",
    "BACURITUBA": "07145",
    "BALSAS": "07277",
    "BARRA DO CORDA": "07315",
    "BARREIRINHAS": "07331",
    "BARÃO DE GRAJAÚ": "07293",
    "BELA VISTA DO MARANHÃO": "07188",
    "BELÁGUA": "07161",
    "BENEDITO LEITE": "07358",
    "BEQUIMÃO": "07374",
    "BERNARDO DO MEARIM": "07200",
    "BOA VISTA DO GURUPI": "07323",
    "BOM JARDIM": "09555",
    "BOM JESUS DAS SELVAS": "07269",
    "BOM LUGAR": "07285",
    "BREJO": "07390",
    "BREJO DE AREIA": "07307",
    "BURITI": "07412",
    "BURITI BRAVO": "07439",
    "BURITICUPU": "07340",
    "BURITIRANA": "07366",
    "CACHOEIRA GRANDE": "07226",
    "CAJAPIÓ": "07455",
    "CAJARI": "07471",
    "CAMPESTRE DO MARANHÃO": "07382",
    "CANTANHEDE": "07510",
    "CAPINZAL DO NORTE": "07404",
    "CAROLINA": "07536",
    "CARUTAPERA": "07552",
    "CAXIAS": "07579",
    "CEDRAL": "07595",
    "CENTRAL DO MARANHÃO": "07420",
    "CENTRO DO GUILHERME": "07447",
    "CENTRO NOVO DO MARANHÃO": "07463",
    "CHAPADINHA": "07617",
    "CIDELÂNDIA": "07480",
    "CODÓ": "07633",
    "COELHO NETO": "07650",
    "COLINAS": "07676",
    "CONCEIÇÃO DO LAGO-AÇU": "07501",
    "COROATÁ": "07692",
    "CURURUPU": "07714",
    "CÂNDIDO MENDES": "07498",
    "DAVINÓPOLIS": "07242",
    "DOM PEDRO": "07730",
    "DUQUE BACELAR": "07757",
    "ESPERANTINÓPOLIS": "07773",
    "ESTREITO": "09636",
    "FEIRA NOVA DO MARANHÃO": "07528",
    "FERNANDO FALCÃO": "07544",
    "FORMOSA DA SERRA NEGRA": "07560",
    "FORTALEZA DOS NOGUEIRAS": "07790",
    "FORTUNA": "07811",
    "GODOFREDO VIANA": "07838",
    "GONÇALVES DIAS": "07854",
    "GOVERNADOR ARCHER": "07870",
    "GOVERNADOR EDISON LOBÃO": "07609",
    "GOVERNADOR EUGÊNIO BARROS": "07897",
    "GOVERNADOR LUIZ ROCHA": "07625",
    "GOVERNADOR NEWTON BELLO": "07641",
    "GOVERNADOR NUNES FREIRE": "07668",
    "GRAJAÚ": "07935",
    "GRAÇA ARANHA": "07919",
    "GUIMARÃES": "07951",
    "HUMBERTO DE CAMPOS": "07978",
    "ICATU": "07994",
    "IGARAPÉ DO MEIO": "07684",
    "IGARAPÉ GRANDE": "08010",
    "IMPERATRIZ": "08036",
    "ITAIPAVA DO GRAJAÚ": "07706",
    "ITAPECURU MIRIM": "08079",
    "ITINGA DO MARANHÃO": "07722",
    "JATOBÁ": "07749",
    "JENIPAPO DOS VIEIRAS": "07765",
    "JOSELÂNDIA": "08117",
    "JOÃO LISBOA": "08095",
    "JUNCO DO MARANHÃO": "07781",
    "LAGO DA PEDRA": "08133",
    "LAGO DO JUNCO": "08150",
    "LAGO DOS RODRIGUES": "07803",
    "LAGO VERDE": "08176",
    "LAGOA DO MATO": "07820",
    "LAGOA GRANDE DO MARANHÃO": "07846",
    "LAJEADO NOVO": "07862",
    "LIMA CAMPOS": "08192",
    "LORETO": "08214",
    "LUÍS DOMINGUES": "08230",
    "MAGALHÃES DE ALMEIDA": "08257",
    "MARACAÇUMÉ": "07889",
    "MARAJÁ DO SENA": "07900",
    "MARANHÃOZINHO": "07927",
    "MATA ROMA": "08273",
    "MATINHA": "08290",
    "MATÕES": "08311",
    "MATÕES DO NORTE": "07943",
    "MILAGRES DO MARANHÃO": "07960",
    "MIRADOR": "08338",
    "MIRANDA DO NORTE": "09695",
    "MIRINZAL": "08354",
    "MONTES ALTOS": "08397",
    "MONÇÃO": "08370",
    "MORROS": "08419",
    "NINA RODRIGUES": "08435",
    "NOVA COLINAS": "07986",
    "NOVA IORQUE": "08451",
    "NOVA OLINDA DO MARANHÃO": "08001",
    "OLHO D´ÁGUA DAS CUNHÃS": "08478",
    "OLINDA NOVA DO MARANHÃO": "08028",
    "PALMEIRÂNDIA": "08516",
    "PARAIBANO": "08532",
    "PARNARAMA": "08559",
    "PASSAGEM FRANCA": "08575",
    "PASTOS BONS": "08591",
    "PAULINO NEVES": "08044",
    "PAULO RAMOS": "09598",
    "PAÇO DO LUMIAR": "08494",
    "PEDREIRAS": "08613",
    "PEDRO DO ROSÁRIO": "08060",
    "PENALVA": "08630",
    "PERI MIRIM": "08656",
    "PERITORÓ": "08087",
    "PINDARÉ-MIRIM": "08672",
    "PINHEIRO": "08699",
    "PIO XII": "08710",
    "PIRAPEMAS": "08737",
    "PORTO FRANCO": "08770",
    "PORTO RICO DO MARANHÃO": "08109",
    "POÇÃO DE PEDRAS": "08753",
    "PRESIDENTE DUTRA": "08796",
    "PRESIDENTE JUSCELINO": "08818",
    "PRESIDENTE MÉDICI": "08125",
    "PRESIDENTE SARNEY": "08141",
    "PRESIDENTE VARGAS": "08834",
    "PRIMEIRA CRUZ": "08850",
    "RAPOSA": "08168",
    "RIACHÃO": "08877",
    "RIBAMAR FIQUENE": "08184",
    "ROSÁRIO": "08915",
    "SAMBAÍBA": "08931",
    "SANTA FILOMENA DO MARANHÃO": "08206",
    "SANTA HELENA": "08958",
    "SANTA INÊS": "09571",
    "SANTA LUZIA": "08974",
    "SANTA LUZIA DO PARUÁ": "09652",
    "SANTA QUITÉRIA DO MARANHÃO": "08990",
    "SANTA RITA": "09016",
    "SANTANA DO MARANHÃO": "08222",
    "SANTO AMARO DO MARANHÃO": "08249",
    "SANTO ANTÔNIO DOS LOPES": "09032",
    "SATUBINHA": "08460",
    "SENADOR ALEXANDRE COSTA": "08486",
    "SENADOR LA ROCQUE": "08508",
    "SERRANO DO MARANHÃO": "08524",
    "SUCUPIRA DO NORTE": "09318",
    "SUCUPIRA DO RIACHÃO": "08540",
    "SÃO ": "08303",
    "SÃO BENEDITO DO RIO PRETO": "09059",
    "SÃO BENTO": "09075",
    "SÃO BERNARDO": "09091",
    "SÃO DOMINGOS DO AZEITÃO": "08265",
    "SÃO DOMINGOS DO MARANHÃO": "09113",
    "SÃO FRANCISCO DO BREJÃO": "08281",
    "SÃO FRANCISCO DO MARANHÃO": "09156",
    "SÃO FÉLIX DE BALSAS": "09130",
    "SÃO JOSÉ DE RIBAMAR": "08893",
    "SÃO JOSÉ DOS BASÍLIOS": "08362",
    "SÃO JOÃO BATISTA": "09172",
    "SÃO JOÃO DO PARAÍSO": "08320",
    "SÃO JOÃO DO SOTER": "08346",
    "SÃO JOÃO DOS PATOS": "09199",
    "SÃO LUÍS": "09210",
    "SÃO LUÍS GONZAGA DO MARANHÃO": "08052",
    "SÃO MATEUS DO MARANHÃO": "09237",
    "SÃO PEDRO DA ÁGUA BRANCA": "08389",
    "SÃO PEDRO DOS CRENTES": "08400",
    "SÃO RAIMUNDO DAS MANGABEIRAS": "09253",
    "SÃO RAIMUNDO DO DOCA BEZERRA": "08427",
    "SÃO ROBERTO": "08443",
    "SÃO VICENTE FERRER": "09270",
    "SÍTIO NOVO": "09296",
    "TASSO FRAGOSO": "09334",
    "TIMBIRAS": "09350",
    "TIMON": "09377",
    "TRIZIDELA DO VALE": "08567",
    "TUFILÂNDIA": "08583",
    "TUNTUM": "09393",
    "TURIAÇU": "09415",
    "TURILÂNDIA": "08605",
    "TUTÓIA": "09431",
    "URBANO SANTOS": "09458",
    "VARGEM GRANDE": "09474",
    "VIANA": "09490",
    "VILA NOVA DOS MARTÍRIOS": "08621",
    "VITORINO FREIRE": "09539",
    "VITÓRIA DO MEARIM": "09512",
    "ZÉ DOCA": "09717"
}

cidades_outros = {
    'Belém': ('pa', '04278'),
    'Belo Horizonte': ('mg', '41238'),
    'Curitiba': ('pr', '75353'),
    'Manaus': ('am', '02550'),
    'Fortaleza': ('ce', '13897'),
    'Rio de Janeiro': ('rj', '60011'),
    'Salvador': ('ba', '38490'),
    'São Paulo': ('sp', '71072'),
    'Porto Alegre': ('rs', '88013'),
}

start_time = time.time()  # Inicia o temporizador

def get_urnas_apuradas(uf, codigo_cidade):
    """Busca dados das urnas apuradas de uma cidade específica na API do TSE."""
    time.sleep(0.75)
    url = f'https://resultados.tse.jus.br/oficial/ele2024/619/dados/{uf}/{uf}{codigo_cidade}-c0011-e000619-u.json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se o status não for 200
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao obter dados da cidade {codigo_cidade}: {e}")
        return None

def formatar_dados_percentuais(cidade, dados):
    """Formata os dados de percentual de votos de uma cidade."""
    try:
        urnas_apuradas = dados['s']['pst']  # Percentual de urnas apuradas
    except KeyError:
        urnas_apuradas = "N/A"

    candidatos_info = []
    for grupo in dados['carg'][0]['agr']:
        for partido in grupo['par']:
            for candidato in partido['cand']:
                nome_candidato = candidato['nm']
                percentual_votos = candidato['pvap']
                candidatos_info.append(f"{nome_candidato} ({percentual_votos}%)")

    candidatos_formatado = " - ".join(candidatos_info)
    return f"{cidade} ({urnas_apuradas}% das urnas apuradas): {candidatos_formatado}"

def formatar_dados_eleitos(cidade, dados):
    """Formata os dados dos candidatos eleitos de uma cidade."""
    try:
        urnas_apuradas = dados['s']['pst']  # Percentual de urnas apuradas
    except KeyError:
        urnas_apuradas = "N/A"

    candidatos_info = []
    for grupo in dados['carg'][0]['agr']:
        for partido in grupo['par']:
            for candidato in partido['cand']:
                if candidato['st'] == 'E':  # Verifica se o candidato foi eleito
                    nome_candidato = candidato['nm']
                    percentual_votos = candidato['pvap']
                    candidatos_info.append(f"{nome_candidato} (ELEITO - {percentual_votos}%)")

    if candidatos_info:
        candidatos_formatado = " - ".join(candidatos_info)
        return f"{cidade} ({urnas_apuradas}% das urnas apuradas): {candidatos_formatado}"
    return None  # Retorna None se não houver candidatos eleitos

def salvar_json(data, filename):
    """Salva os dados em um arquivo JSON."""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

# Dicionários para armazenar os dados de slz e itz
dados_formatados_slz_itz = []
dados_completos_slz_itz = {}  # Dicionário para armazenar os dados completos

# Iterando sobre as cidades slz e itz para obter e formatar os dados
uf_ma = 'ma'  # Unidade Federativa do Maranhão
for cidade, codigo in slz_itz.items():
    urnas_apuradas = get_urnas_apuradas(uf_ma, codigo)
    if urnas_apuradas:
        dados_completos_slz_itz[cidade] = urnas_apuradas  # Salvando os dados completos
        try:
            dados_formatados_slz_itz.append(formatar_dados_percentuais(cidade, urnas_apuradas))
            print(f"Dados processados para {cidade}.")
        except KeyError as e:
            print(f"Erro ao processar dados da cidade {cidade}: {e}")

# Criando o JSON com uma única linha para slz e itz
resultado_slz_itz = " | ".join(dados_formatados_slz_itz)

# Salvando o resultado formatado no arquivo SLZ_ITZ_resultado_urnas.json
resultado_json_ma = {"resultado": resultado_slz_itz}
with open(os.path.join(save_path_local, 'SLZ_ITZ_resultado_urnas.json'), 'w', encoding='utf-8') as json_file:
    json.dump([resultado_json_ma], json_file, ensure_ascii=False)

with open(os.path.join(save_path_remote, 'SLZ_ITZ_resultado_urnas.json'), 'w', encoding='utf-8') as json_file:
    json.dump([resultado_json_ma], json_file, ensure_ascii=False)

# Salvando os dados completos da API no arquivo apiTse.json
with open(os.path.join(save_path_local, 'SLZ_ITZ_apiTse.json'), 'w', encoding='utf-8') as api_file:
    json.dump([dados_completos_slz_itz], api_file, ensure_ascii=False)

with open(os.path.join(save_path_remote, 'SLZ_ITZ_apiTse.json'), 'w', encoding='utf-8') as api_file:
    json.dump([dados_completos_slz_itz], api_file, ensure_ascii=False)

print("Dados formatados e salvos no arquivo SLZ_ITZ_resultado_urnas.json")
print("Dados completos salvos no arquivo SLZ_ITZ_apiTse.json")


# Processamento para cidades do Maranhão
dados_formatados_cidades_ma = []
dados_completos_cidades_ma = {}

for index, (cidade, codigo) in enumerate(cidades_ma.items()):
    urnas_apuradas = get_urnas_apuradas('ma', codigo)
    if urnas_apuradas:
        dados_completos_cidades_ma[cidade] = urnas_apuradas
        dados_formatados_cidades_ma.append(formatar_dados_eleitos(cidade, urnas_apuradas))
        print(f"Dados processados para {cidade}.")

resultado_ma = " | ".join(filter(None, dados_formatados_cidades_ma))
resultado_json_ma = {"resultado": resultado_ma}

# Salvando resultados
salvar_json([resultado_json_ma], os.path.join(save_path_local, 'cidades_ma_resultado_urnas.json'))
salvar_json([resultado_json_ma], os.path.join(save_path_remote, 'cidades_ma_resultado_urnas.json'))
salvar_json([dados_completos_cidades_ma], os.path.join(save_path_local, 'cidades_ma_apiTse.json'))
salvar_json([dados_completos_cidades_ma], os.path.join(save_path_remote, 'cidades_ma_apiTse.json'))

print("Dados formatados e salvos no arquivo cidades_ma_resultado_urnas.json")
print("Dados completos salvos no arquivo cidades_ma_apiTse.json")

# Processamento para outras capitais
dados_formatados_outros = []
dados_completos_outros = {}

for cidade, (uf, codigo) in cidades_outros.items():
    urnas_apuradas = get_urnas_apuradas(uf, codigo)
    if urnas_apuradas:
        dados_completos_outros[cidade] = urnas_apuradas
        dados_formatados_outros.append(formatar_dados_percentuais(cidade, urnas_apuradas))
        print(f"Dados processados para {cidade}.")

resultado_outros = " | ".join(dados_formatados_outros)
resultado_json_outros = {"resultado": resultado_outros}

# Salvando resultados
salvar_json([resultado_json_outros], os.path.join(save_path_local, 'outras_capitais_resultado_urnas.json'))
salvar_json([resultado_json_outros], os.path.join(save_path_remote, 'outras_capitais_resultado_urnas.json'))
salvar_json([dados_completos_outros], os.path.join(save_path_local, 'outras_capitais_apiTse.json'))
salvar_json([dados_completos_outros], os.path.join(save_path_remote, 'outras_capitais_apiTse.json'))

print("Dados formatados e salvos no arquivo outras_capitais_resultado_urnas.json")
print("Dados completos salvos no arquivo outras_capitais_apiTse.json")

# Exibir o tempo total de execução
tempo_total = time.time() - start_time
print(f"Tempo total de execução: {tempo_total:.2f} segundos")
