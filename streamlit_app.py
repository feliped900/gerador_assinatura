import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

# Caminho para a imagem de assinatura base
imagem_base_path = "assinatura_modelo.png"

# Carregar as fontes
fonte = ImageFont.truetype("C:\\Users\\felip\\OneDrive\\Projetos de Tecnologia\\ass_modelo_sutter\\fontes\\OUTFIT-BLACK.TTF", 14)
fonte_cargo = ImageFont.truetype("C:\\Users\\felip\\OneDrive\\Projetos de Tecnologia\\ass_modelo_sutter\\fontes\\OUTFIT-MEDIUM.TTF", 30)
fonte_nome = ImageFont.truetype("C:\\Users\\felip\\OneDrive\\Projetos de Tecnologia\\ass_modelo_sutter\\fontes\\OUTFIT-MEDIUM.TTF", 56)
fonte_telefone = ImageFont.truetype("C:\\Users\\felip\\OneDrive\\Projetos de Tecnologia\\ass_modelo_sutter\\fontes\\OUTFIT-MEDIUM.TTF", 36)
fonte_email = ImageFont.truetype("C:\\Users\\felip\\OneDrive\\Projetos de Tecnologia\\ass_modelo_sutter\\fontes\\OUTFIT-MEDIUM.TTF", 36)

# Função para gerar uma assinatura
def gerar_assinatura(nome, email, cargo, telefone, foto_path=None):
    with Image.open(imagem_base_path).convert("RGBA") as imagem:
        draw = ImageDraw.Draw(imagem)

        # Adicionar textos
        draw.text((623, 222), nome, font=fonte_nome, fill="white")
        draw.text((623, 294), cargo, font=fonte_cargo, fill="white")
        draw.text((623, 390), telefone, font=fonte_telefone, fill="white")
        draw.text((623, 438), email, font=fonte_email, fill="white")
        
        # Adicionar a foto do rosto, se fornecida
        if foto_path:
            with Image.open(foto_path).convert("RGBA") as foto:
                foto_resized = foto.resize((453, 453))
                foto_position = (112, 74)
                imagem.paste(foto_resized, foto_position, foto_resized)

        # Salvar a imagem em um buffer
        buffer = BytesIO()
        imagem.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer

# Interface Streamlit
st.title("Gerador de Assinaturas")

# Campos de entrada
nome = st.text_input("Nome")
email = st.text_input("Email")
cargo = st.text_input("Cargo")
telefone = st.text_input("Telefone")
foto = st.file_uploader("Upload da foto (opcional)", type=["png", "jpg", "jpeg"])

# Botão para gerar assinatura
if st.button("Gerar Assinatura"):
    if nome and email and cargo and telefone:
        foto_path = None
        if foto:
            foto_path = BytesIO(foto.read())

        # Gerar assinatura
        assinatura = gerar_assinatura(nome, email, cargo, telefone, foto_path)
        
        # Exibir imagem da assinatura
        st.image(assinatura, caption="Assinatura Gerada", use_column_width=True)
        
        # Botão para download
        st.download_button(
            label="Baixar Assinatura",
            data=assinatura,
            file_name=f"{nome}_assinatura.png",
            mime="image/png"
        )
    else:
        st.error("Por favor, preencha todos os campos obrigatórios.")
