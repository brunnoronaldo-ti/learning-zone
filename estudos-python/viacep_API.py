import requests

def get_cep():
    print("para iniciar, insira um cep válido")

    while True:
        # Recebemos como string para preservar zeros à esquerda
        cep = input("Insira um cep (apenas números):").strip()

        # Verifica se tem exatamente 8 caracteres e se todos são números
        if len(cep) == 8 and cep.isdigit():
            return cep 
        else:
            print("Erro! Um CEP válido deve conter exatamente 8 números, sem letras ou símbolos.")
    
cep_user = get_cep()
print("\n" * 3)


def search_cep(cep_user):
    
    # A URL responsável por buscar os dados
    url = f"https://viacep.com.br/ws/{cep_user}/json/"

    # buscando dados da url
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
    
        if "erro" in dados:
            print("CEP não encontrado na base do ViaCEP.")
        else:
            print(f"CEP:{dados['cep']}")  
            print(f"cidade:{dados['localidade']} - {dados['uf']}" )      
            print(f"bairro:{dados['bairro']}")      
            print(f"logradouro:{dados['logradouro']}")        
            print(f"complemento:{dados['complemento']}")   
            print(f"ddd:{dados['ddd']}")                    
    else:
        print("ocorreu um erro")


search_cep(cep_user)
