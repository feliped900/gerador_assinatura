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

1. **Clone o repositório:**

```python
git clone https://github.com/seu-usuario/gerador-de-assinaturas.git
cd gerador-de-assinaturas
```

2. **Instale as dependências:**

```python
pip install -r requirements.txt
```

3. **Adicione os arquivos necessários:**
- Certifique-se de que o arquivo da imagem base assinatura_modelo.png está na raiz do projeto.
  - Insira as fontes no diretório fontes/ com os arquivos:
  - `OUTFIT-BLACK.TTF`
  - `OUTFIT-MEDIUM.TTF`