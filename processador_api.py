import requests
import csv
import json

def buscar_dados(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar a URL {url}: {e}")
        return None


def agrupar_posts_por_usuario(lista_de_posts):
    posts_agrupados = {}
    if lista_de_posts:
        for post in lista_de_posts:
            userId = post['userId']
            if userId not in posts_agrupados:
                posts_agrupados[userId] = []
            posts_agrupados[userId].append(post)
    return posts_agrupados


def gerar_dados_relatorio(lista_usuarios, posts_por_usuario):
    dados_relatorio = []
    for usuario in lista_usuarios:
        user_id = usuario['id']
        posts_do_usuario = posts_por_usuario.get(user_id, [])
        quantidade_posts = len(posts_do_usuario)

        if quantidade_posts > 0:
            total_caracteres = sum(len(post['body']) for post in posts_do_usuario)
            media_caracteres = total_caracteres / quantidade_posts
        else:
            media_caracteres = 0

        linha = {
            "ID do Usuario": user_id,
            "Nome do Usuario": usuario['name'],
            "Quantidade de Posts": quantidade_posts,
            "Media de Caracteres dos Posts": media_caracteres
        }
        dados_relatorio.append(linha)

    return dados_relatorio


def imprimir_relatorio_console(dados_relatorio):
    print("\n--- Relatório de Atividade dos Usuários ---")
    print(f"{'ID'} | {'Nome do Usuario'} | {'Qtd. Posts'} | {'Media de Caracteres'}")
    print("-" * 80)

    for linha in dados_relatorio:
        print(f"{linha['ID do Usuario']:<5} | "
              f"{linha['Nome do Usuario']:<25} | "
              f"{linha['Quantidade de Posts']} | "
              f"{linha['Media de Caracteres dos Posts']}")


def salvar_relatorio_csv(dados_relatorio, nome_arquivo):
    if not dados_relatorio:
        print("Não há dados para salvar.")
        return

    nomes_colunas = dados_relatorio[0].keys()

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)
            writer.writeheader()
            writer.writerows(dados_relatorio)
        print(f"\nRelatório salvo com sucesso em '{nome_arquivo}'")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")


def enviar_relatorio_simulado(dados_relatorio, destinatario):
    url_simulada = "https://jsonplaceholder.typicode.com/send-email"

    payload = {
        "destinatario": destinatario,
        "assunto": "Relatório de Atividade de Usuários",
        "corpo_relatorio": dados_relatorio
    }

    headers = {
        "Content-Type": "application/json"
    }

    print(f"\nSimulando envio do relatório para o destinatário: {destinatario}...")
    try:
        response = requests.post(url_simulada, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print("Simulação bem-sucedida! O servidor de teste recebeu os dados.")
            return True
        else:
            print(f"Falha na simulação. Status Code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao tentar simular o envio: {e}")
        return False


def main():
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_posts = "https://jsonplaceholder.typicode.com/posts"

    print("Iniciando busca de dados...")
    lista_usuarios = buscar_dados(url_users)
    lista_de_posts = buscar_dados(url_posts)

    if not lista_usuarios or not lista_de_posts:
        print("Não foi possível carregar os dados. Encerrando o script.")
        return

    print("Dados carregados. Organizando posts...")
    posts_por_usuario = agrupar_posts_por_usuario(lista_de_posts)
    dados_para_relatorio = gerar_dados_relatorio(lista_usuarios, posts_por_usuario)

    imprimir_relatorio_console(dados_para_relatorio)

    salvar_relatorio_csv(dados_para_relatorio, 'relatorio_usuarios.csv')

    enviar_relatorio_simulado(dados_para_relatorio, 'alyssoncosta2001@hotmail.com')