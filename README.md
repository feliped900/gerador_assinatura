# Gerador de Assinaturas

Este projeto é um gerador de assinaturas personalizadas desenvolvido em Python com Streamlit. Ele permite criar imagens de assinatura profissional com nome, cargo, telefone, email e foto de perfil opcional. 

## Funcionalidades

- Interface amigável para entrada de dados.
- Personalização de assinatura com nome, cargo, telefone, email e foto.
- Geração de assinatura em formato de imagem (PNG).
- Opção para baixar a assinatura gerada.

## Requisitos

Antes de iniciar, certifique-se de que os seguintes requisitos estão atendidos:

- **Python 3.8 ou superior**
- Bibliotecas necessárias (instaladas via `pip`):
  - `streamlit`
  - `Pillow`

## Como usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/gerador-de-assinaturas.git
   cd gerador-de-assinaturas

## Instale as dependências:
```bash
pip install -r requirements.txt

Adicione os arquivos necessários:

Certifique-se de que o arquivo da imagem base assinatura_modelo.png está na raiz do projeto.
Insira as fontes no diretório fontes/ com os arquivos:
OUTFIT-BLACK.TTF
OUTFIT-MEDIUM.TTF

Execute a aplicação:

bash
Copiar código
streamlit run app.py
Use a interface:

Preencha os campos: nome, email, cargo, telefone e foto (opcional).
Clique no botão Gerar Assinatura.
Baixe sua assinatura clicando no botão de download.
Estrutura do Projeto
bash
Copiar código
gerador-de-assinaturas/
│
├── app.py                   # Código principal da aplicação
├── assinatura_modelo.png    # Imagem base para a assinatura
├── fontes/                  # Diretório com as fontes
│   ├── OUTFIT-BLACK.TTF
│   └── OUTFIT-MEDIUM.TTF
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
Demonstração

Exemplo de assinatura gerada pelo aplicativo.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.

markdown
Copiar código

### Notas:
1. Altere o URL do repositório para o correto após publicá-lo no GitHub.
2. Inclua um exemplo real em `example-image.png` para demonstrar a funcionalidade.
3. Adicione um arquivo `requirements.txt` com as dependências do projeto.
