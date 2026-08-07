import streamlit as st
import requests
import random

# =====================================================================
# ⚙️ CONFIGURAÇÕES FIXAS DO SEU NEGÓCIO
# =====================================================================
NUMERO_WHATSAPP = "5569992813319"  # Seu número com DDD 69
SENHA_PAINEL_ADMIN = "ADMIN_2K_SECRET" 
USUARIO_ADMIN_MESTRO = "admin"

if "clientes_premium" not in st.session_state:
    st.session_state["clientes_premium"] = {}

if "config_app" not in st.session_state:
    st.session_state["config_app"] = {
        "titulo": "🚀 Analisador Viral TikTok Shop",
        "subtitulo": "Descubra o que falta para seu perfil alcançar 2.000 seguidores e liberar as vendas",
        "logo_url": "https://unsplash.com",
        "capa_url": ""
    }

query_params = st.query_params
token_cliente = query_params.get("token", None)
modo_admin = query_params.get("admin", None)

APP_TITULO = st.session_state["config_app"]["titulo"]
APP_SUBTITULO = st.session_state["config_app"]["subtitulo"]
APP_LOGO = st.session_state["config_app"]["logo_url"]
APP_CAPA = st.session_state["config_app"]["capa_url"]

link_suporte_whatsapp = f"https://wa.me{NUMERO_WHATSAPP}?text=Olá!%20Meu%20acesso%20Premium%20bloqueou%20porque%20mudei%20de%20dispositivo.%20Pode%20resetar%20meu%20IP?"

st.set_page_config(page_title=APP_TITULO, page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #238636 !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        border-radius: 10px !important;
        border: none !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #2ea043 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Gerador inteligente de dicas virais aleatórias para o teste grátis (Sem travar)
def gerar_analise_falsa(username):
    erros = [
        "Seu perfil está sofrendo com o travamento padrão das 200 visualizações por falta de um Gancho de Retenção Visual nos primeiros 1.5 segundos.",
        "O algoritmo do TikTok não conseguiu identificar o nicho claro dos seus vídeos porque a sua Biografia não possui as palavras-chave indexadas de busca.",
        "Seus takes de produtos estão parecendo anúncios tradicionais de televisão. O público de 2026 rejeita propagandas agressivas e busca reviews nativos em formato de ASMR."
    ]
    ganchos = [
        "Eu achei que esse produto de R$ 30 do TikTok Shop era golpe, até que eu decidi testar...",
        "Se você tem menos de 2.000 seguidores e ainda não vendeu nada, pare de postar vídeos e mude para essa estratégia...",
        "O dono da loja secreta do TikTok Shop vai me odiar por revelar o menor preço desse periférico hoje..."
    ]
    return f"""
    ### 📊 Relatório Técnico de Engajamento para: **{username}**
    
    ❌ **Gargalo Identificado:** {random.choice(erros)}
    
    🔥 **Dica de Gancho para o Próximo Vídeo:** Use essa abertura exata na legenda e no áudio: *"{random.choice(ganchos)}"*
    
    ---
    ⚠️ **ATENÇÃO:** O teste gratuito gerou apenas uma amostra do diagnóstico. Para liberar a ferramenta de criação automática de roteiros de alta retenção copiáveis e o cronograma diário de crescimento acelerado rumo aos 2.000 seguidores compradores, adquira seu acesso Premium clicando no botão verde gigante abaixo.
    """

# PAINEL ADMIN
if modo_admin == "true":
    st.title("🎛️ Autenticação Administrativa")
    with st.form("login_admin"):
        usuario_digitado = st.text_input("Usuário do Administrador:")
        senha_digitada = st.text_input("Senha do Administrador:", type="password")
        botao_entrar = st.form_submit_button("🔑 Entrar no Painel Mestre")
    if botao_entrar:
        if usuario_digitado == USUARIO_ADMIN_MESTRO and senha_digitada == SENHA_PAINEL_ADMIN:
            st.session_state["admin_autenticado"] = True
        else:
            st.error("❌ Usuário ou Senha incorretos.")
            
    if st.session_state.get("admin_autenticado", False):
        st.success("🔓 Conectado!")
        st.subheader("🎨 Personalizar Visual")
        novo_titulo = st.text_input("Título do Aplicativo:", APP_TITULO)
        novo_subtitulo = st.text_area("Subtítulo da Tela Inicial:", APP_SUBTITULO)
        nova_logo = st.text_input("Link da LOGO:", APP_LOGO)
        nova_capa = st.text_input("Link da Imagem de CAPA:", APP_CAPA)
        
        if st.button("💾 Salvar Novas Configurações"):
            st.session_state["config_app"]["titulo"] = novo_titulo
            st.session_state["config_app"]["subtitulo"] = novo_subtitulo
            st.session_state["config_app"]["logo_url"] = nova_logo
            st.session_state["config_app"]["capa_url"] = nova_capa
            st.success("✨ Visual atualizado!")
            st.rerun()
            
        st.markdown("---")
        st.subheader("🔑 Links Premium")
        with st.form("criar_token"):
            novo_tk = st.text_input("Nome do Comprador:").strip()
            cadastrar = st.form_submit_button("➕ Gerar Novo Link de Acesso")
            if cadastrar and novo_tk:
                if novo_tk not in st.session_state["clientes_premium"]:
                    st.session_state["clientes_premium"][novo_tk] = "ativo"
                    st.success(f"Link gerado!")
                    st.code(f"https://streamlit.app{novo_tk}")
                else:
                    st.warning("⚠️ Código já existe.")
                    
        for tk in list(st.session_state["clientes_premium"].keys()):
            st.write(f"🎟️ **Token Premium Ativo:** `{tk}`")
    st.stop()

# ÁREA PREMIUM
if token_cliente:
    if token_cliente in st.session_state["clientes_premium"]:
        if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
        if APP_LOGO: st.image(APP_LOGO, width=80)
        
        st.title("💎 Área VIP - Método 2K")
        nicho = st.selectbox("Qual o nicho do produto?", ["Achadinhos", "Gamer", "Beleza", "Moda", "Saúde"])
        username_premium = st.text_input("Digite o @usuario para auditoria profunda:")
        if st.button("🚀 Iniciar Auditoria Avançada"):
            with st.spinner("⚙️ Gerando estratégias..."):
                st.markdown(gerar_analise_falsa(username_premium))
        st.stop()

# TELA PÚBLICA
if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
if APP_LOGO: st.image(APP_LOGO, width=100)

st.title(APP_TITULO)
st.subheader(APP_SUBTITULO)
user_teste = st.text_input("Seu @ Nome de Usuário do TikTok:", placeholder="ex: @seu_perfil")

if st.button("🔍 Buscar Perfil e Analisar Grátis"):
    if not user_teste:
        st.warning("⚠️ Digite o seu nome de usuário.")
    else:
        with st.spinner("📡 Escaneando dados estruturais..."):
            # Exibe o diagnóstico estável gerado pelo sistema
            st.success("✅ Perfil localizado e mapeado com sucesso!")
            resposta_sistema = gerar_analise_falsa(user_teste)
            st.markdown(resposta_sistema)
            
            texto_wpp = f"Olá! Analisei meu perfil @{user_teste.replace('@','')} no robô Método 2K. Fiz o teste gratuito e quero comprar o acesso Premium para liberar os roteiros avançados!"
            link_final = f"https://wa.me{NUMERO_WHATSAPP}?text={requests.utils.quote(texto_wpp)}"
            st.markdown(f'<br><a href="{link_final}" target="_blank"><button style="background-color:#238636;color:white;font-size:22px;font-weight:bold;height:65px;width:100%;border-radius:12px;border:none;cursor:pointer;box-shadow: 0px 4px 15px rgba(0,255,0,0.2);">🟢 QUERO MEU ACESSO PREMIUM VIA WHATSAPP</button></a>', unsafe_allow_html=True)



