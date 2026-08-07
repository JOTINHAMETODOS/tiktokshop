import streamlit as st
import requests

# =====================================================================
# ⚙️ CONFIGURAÇÕES FIXAS DO SEU NEGÓCIO
# =====================================================================
NUMERO_WHATSAPP = "5569992813319"  # Seu número com DDD 69
SENHA_PAINEL_ADMIN = "ADMIN_2K_SECRET" 
USUARIO_ADMIN_MESTRO = "admin"

# Inicialização segura da memória nativa do servidor (Evita travamentos de tela preta)
if "clientes_premium" not in st.session_state:
    st.session_state["clientes_premium"] = {}

# Área que guarda as imagens e textos mutáveis (Editáveis pelo Painel Admin)
if "config_app" not in st.session_state:
    st.session_state["config_app"] = {
        "titulo": "🚀 Analisador Viral TikTok Shop",
        "subtitulo": "Descubra o que falta para seu perfil alcançar 2.000 seguidores e liberar as vendas",
        "logo_url": "https://unsplash.com", # Logo padrão do app
        "capa_url": "" # Capa opcional começa em branco
    }

GEMINI_API_KEY = st.secrets.get("GEMINI_KEY", "")

def chamar_gemini_gratis(prompt_texto):
    url = "https://googleapis.com"
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"} if GEMINI_API_KEY.startswith("AQ") else {}
    endpoint = f"{url}?key={GEMINI_API_KEY}" if not GEMINI_API_KEY.startswith("AQ") else url
    
    payload = {"contents": [{"parts": [{"text": prompt_texto}]}]}
    try:
        if GEMINI_API_KEY.startswith("AQ"):
            resposta = requests.post(endpoint, json=payload, headers=headers, timeout=15).json()
        else:
            resposta = requests.post(endpoint, json=payload, timeout=15).json()
        return resposta['candidates']['content']['parts']['text']
    except Exception as e:
        return "⚠️ Erro de ativação. Por favor, verifique se a sua chave do Gemini foi colada corretamente na aba 'Secrets' do Streamlit."

def capturar_ip():
    try:
        return requests.get("https://ipify.org", timeout=3).json().get("ip")
    except:
        return "127.0.0.1"

ip_atual = capturar_ip()
query_params = st.query_params
token_cliente = query_params.get("token", None)
modo_admin = query_params.get("admin", None)

# Puxa os dados customizados salvos na memória do app
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

def puxar_dados_reais_tiktok(username):
    user_limpo = username.replace("@", "").strip()
    url = f"https://tikwm.com{user_limpo}"
    try:
        resposta = requests.get(url, timeout=7).json()
        if resposta.get("code") == 0 and "data" in resposta:
            dados_user = resposta["data"]["user"]
            dados_status = resposta["data"]["stats"]
            return {
                "sucesso": True,
                "nome": dados_user.get("nickname", user_limpo),
                "avatar": dados_user.get("avatarLarger"),
                "seguidores": dados_status.get("followerCount", 0),
                "curtidas": dados_status.get("heartCount", 0),
                "assinatura": dados_user.get("signature", "")
            }
    except:
        pass
    return {"sucesso": False}

# =====================================================================
# 🎛️ PAINEL ADMINISTRATIVO MESTRE (EDITÁVEL)
# =====================================================================
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
        
        st.subheader("🎨 Personalizar Visual do Aplicativo (Inovar Sempre)")
        novo_titulo = st.text_input("Título do Aplicativo:", APP_TITULO)
        novo_subtitulo = st.text_area("Subtítulo da Tela Inicial:", APP_SUBTITULO)
        nova_logo = st.text_input("Link da LOGO (URL do ImgBB):", APP_LOGO)
        nova_capa = st.text_input("Link da Imagem de CAPA (URL do ImgBB):", APP_CAPA, placeholder="Cole aqui para exibir um banner no topo")
        
        if st.button("💾 Salvar Novas Configurações Visuais"):
            st.session_state["config_app"]["titulo"] = novo_titulo
            st.session_state["config_app"]["subtitulo"] = novo_subtitulo
            st.session_state["config_app"]["logo_url"] = nova_logo
            st.session_state["config_app"]["capa_url"] = nova_capa
            st.success("✨ Visual atualizado instantaneamente!")
            st.rerun()
            
        st.markdown("---")
        st.subheader("🔑 Links Premium (Emissão de Clientes)")
        with st.form("criar_token"):
            novo_tk = st.text_input("Nome do Comprador (Ex: MARCOS_VIP):").strip()
            cadastrar = st.form_submit_button("➕ Gerar Novo Link de Acesso")
            if cadastrar and novo_tk:
                if novo_tk not in st.session_state["clientes_premium"]:
                    st.session_state["clientes_premium"][novo_tk] = None
                    st.success(f"Link gerado!")
                    st.code(f"https://streamlit.app{novo_tk}")
                else:
                    st.warning("⚠️ Código já existe.")
                    
        for tk, ip_g in list(st.session_state["clientes_premium"].items()):
            col1, col2 = st.columns()
            with col1:
                st.write(f"🎟️ **Token:** `{tk}` | 🔒 **IP:** `{ip_g if ip_g else 'Aguardando clique'}`")
            with col2:
                if st.button("🔄 Resetar IP", key=f"reset_{tk}"):
                    st.session_state["clientes_premium"][tk] = None
                    st.rerun()
    st.stop()

# =====================================================================
# 💎 FLUXO B: ÁREA PREMIUM COMPRADA
# =====================================================================
if token_cliente:
    if token_cliente in st.session_state["clientes_premium"]:
        ip_g = st.session_state["clientes_premium"][token_cliente]
        if ip_g is not None and ip_g != ip_atual and "sessao_autorizada" not in st.session_state:
            st.error("🔒 Link Bloqueado: Este acesso VIP já foi registrado em outro aparelho.")
            st.markdown(f'<a href="{link_suporte_whatsapp}" target="_blank"><button style="background-color:#238636;color:white;font-size:20px;font-weight:bold;height:60px;width:100%;border-radius:10px;border:none;cursor:pointer;">🟢 Chamar Suporte Humano no WhatsApp para Liberar</button></a>', unsafe_allow_html=True)
            st.stop()
        elif ip_g is None:
            st.session_state["clientes_premium"][token_cliente] = ip_atual
            st.session_state["sessao_autorizada"] = True
            
        # Exibição de Capa e Logo Premium Customizadas
        if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
        if APP_LOGO: st.image(APP_LOGO, width=80)
        
        st.title("💎 Área VIP - Método 2K")
        nicho = st.selectbox("Qual o nicho do produto?", ["Achadinhos", "Gamer", "Beleza", "Moda", "Saúde"])
        username_premium = st.text_input("Digite o @usuario para auditoria profunda:")
        if st.button("🚀 Iniciar Auditoria Avançada"):
            with st.spinner("🧠 Gerando estratégias de 2026..."):
                dados_tiktok = puxar_dados_reais_tiktok(username_premium)
                ctx = f"Perfil real com {dados_tiktok['seguidores']} seguidores." if dados_tiktok["sucesso"] else ""
                prompt_vip = f"Você é mentor de TikTok Shop. Crie um plano com 3 roteiros virais copiáveis de 2026 para o usuário {username_premium}. Nicho: {nicho}. {ctx}"
                resultado_ia = chamar_gemini_gratis(prompt_vip)
                st.markdown(resultado_ia)
        st.stop()

# =====================================================================
# 🚀 FLUXO C: TELA INICIAL PÚBLICA
# =====================================================================
# Exibição de Capa e Logo Customizadas na tela do cliente
if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
if APP_LOGO: st.image(APP_LOGO, width=100)

st.title(APP_TITULO)
st.subheader(APP_SUBTITULO)
user_teste = st.text_input("Seu @ Nome de Usuário do TikTok:", placeholder="ex: @seu_perfil")

if st.button("🔍 Buscar Perfil e Analisar Grátis"):
    if not user_teste:
        st.warning("⚠️ Digite o seu nome de usuário.")
    else:
        with st.spinner("📡 Escaneando dados estruturais do perfil..."):
            dados = puxar_dados_reais_tiktok(user_teste)
            
            if not dados["sucesso"]:
