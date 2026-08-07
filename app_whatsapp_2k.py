import streamlit as st
import requests

# =====================================================================
# ⚙️ CONFIGURAÇÕES FIXAS DO SEU NEGÓCIO (WHATSAPP COM DDD 69)
# =====================================================================
NUMERO_WHATSAPP = "5569992813319"  
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

# Puxa a chave mestre dos segredos do Streamlit
CHAVE_MESTRE="AQ.Ab8RN6LgYms6buLc9DAAnMy1lhNGBcEiS4TQkMFRKUpVf0HD9g"

def chamar_gemini_real(prompt_texto):
    url = "https://googleapis.com"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }
    payload = {"contents": [{"parts": [{"text": prompt_texto}]}]}
    try:
        resposta = requests.post(url, json=payload, headers=headers, timeout=15).json()
        return resposta['candidates']['content']['parts']['text']
    except Exception as e:
        return (
            "### 📊 Relatório Estruturado de Crescimento\n\n"
            "❌ **Erro de Comunicação com a IA:** Verifique se a sua chave secreta do Gemini está "
            "corretamente salva na aba 'Secrets' do Streamlit com o nome de `CHAVE_MESTRE`."
        )

def capturar_ip():
    try:
        return requests.get("https://ipify.org", timeout=3).json().get("ip")
    except:
        return "127.0.0.1"

ip_atual = capturar_ip()
query_params = st.query_params
token_cliente = query_params.get("token", None)
modo_admin = query_params.get("admin", None)

APP_TITULO = st.session_state["config_app"]["titulo"]
APP_SUBTITULO = st.session_state["config_app"]["subtitulo"]
APP_LOGO = st.session_state["config_app"]["logo_url"]
APP_CAPA = st.session_state["config_app"]["capa_url"]

link_suporte_whatsapp = f"https://wa.me{NUMERO_WHATSAPP}?text=Olá!%20Meu%20acesso%20Premium%20bloqueou%20porque%20mudei%20de%20dispositivo.%20Pode%20resetar%20meu%20IP?"

st.set_page_config(page_title=APP_TITULO, page_icon="🚀", layout="centered")

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
# 🎛️ FLUXO A: PAINEL ADMINISTRATIVO MESTRE
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
        st.success("🔓 Conectado com sucesso!")
        st.subheader("🎨 Personalizar Visual")
        novo_titulo = st.text_input("Título do Aplicativo:", APP_TITULO)
        novo_subtitulo = st.text_area("Subtítulo da Tela Inicial:", APP_SUBTITULO)
        nova_logo = st.text_input("Link da LOGO:", APP_LOGO)
        nova_capa = st.text_input("Link da Imagem de CAPA:", APP_CAPA)
        
        if st.button("💾 Salvar Novas Configurações Visuais"):
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
                    st.success(f"Link de acesso Premium gerado!")
                    st.code(f"https://streamlit.app{novo_tk}")
                else:
                    st.warning("⚠️ Código já existe.")
        for tk in list(st.session_state["clientes_premium"].keys()):
            st.write(f"🎟️ **Token Premium Ativo:** `{tk}`")
    st.stop()

# =====================================================================
# 💎 FLUXO B: ÁREA PREMIUM COMPRADA
# =====================================================================
if token_cliente:
    if token_cliente in st.session_state["clientes_premium"]:
        ip_g = st.session_state["clientes_premium"][token_cliente]
        if ip_g is not None and ip_g != ip_atual and "sessao_autorizada" not in st.session_state:
            st.error("🔒 Link Bloqueado: Este acesso VIP já foi registrado em outro aparelho.")
            st.link_button("🟢 Chamar Suporte Humano no WhatsApp para Liberar", link_suporte_whatsapp)
            st.stop()
        elif ip_g is None:
            st.session_state["clientes_premium"][token_cliente] = ip_atual
            st.session_state["sessao_autorizada"] = True
            
        if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
        if APP_LOGO: st.image(APP_LOGO, width=80)
        
        st.title("💎 Área VIP - Método 2K")
        nicho = st.selectbox("Qual o nicho do produto que você deseja vender como afiliado?", ["Achadinhos", "Gamer", "Beleza", "Moda", "Saúde"])
        username_premium = st.text_input("Digite o @usuario para auditoria profunda:")
        if st.button("🚀 Iniciar Auditoria Avançada"):
            with st.spinner("🧠 Gerando estratégias exclusivas baseadas no algoritmo 2026..."):
                prompt_vip = (
                    f"Você é o maior mentor de afiliados do TikTok Shop. Crie um diagnóstico profissional e cirúrgico "
                    f"para o perfil @{username_premium} focado no nicho de {nicho}. Forneça de forma detalhada:\n"
                    f"1. Uma análise das fraquezas da biografia dele.\n"
                    f"2. Três ideias completas de vídeos virais copiáveis com o roteiro passo a passo e ações de áudio ASMR.\n"
                    f"3. Estratégia exata de SEO de pesquisa do TikTok para indexar os produtos e ganhar os 2k seguidores compradores rapidamente."
                )
                resultado_ia = chamar_gemini_real(prompt_vip)
                st.markdown(resultado_ia)
        st.stop()

# =====================================================================
# 🚀 FLUXO C: TELA INICIAL PÚBLICA (ISCA DIGITAL REAL)
# =====================================================================
if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
if APP_LOGO: st.image(APP_LOGO, width=100)

st.title(APP_TITULO)
st.subheader(APP_SUBTITULO)
user_teste = st.text_input("Seu @ Nome de Usuário do TikTok:", placeholder="ex: @seu_perfil")

if st.button("🔍 Buscar Perfil e Analisar Grátis"):
    if not user_teste:
        st.warning("⚠️ Digite o seu nome de usuário.")
    else:
        with st.spinner("📡 Escaneando banco de dados do TikTok..."):
            dados = puxar_dados_reais_tiktok(user_teste)
            
            st.markdown("### 📊 Relatório Técnico de Engajamento")
            
            if dados["sucesso"]:
                col1, col2 = st.columns([1, 3])
                with col1:
                    if dados["avatar"]: st.image(dados["avatar"], width=90)
                with col2:
                    st.markdown(f"#### **{dados['nome']}**")
                    st.write(f"👥 **Seguidores:** {dados['seguidores']:,}".replace(",", "."))
                    st.write(f"❤️ **Total de Curtidas:** {dados['curtidas']:,}".replace(",", "."))
                st.markdown("---")
                seguidores_txt = f"{dados['seguidores']} seguidores"
                prompt_free = (
                    f"Diga que localizou o perfil público de {user_teste} com {dados['seguidores']} seguidores. "
                    f"Dê um feedback direto focado no nicho de afiliados. Aponte 1 erro crasso estrutural baseado "
                    f"no volume de seguidores e entregue 1 dica inovadora de gancho de 1.5 segundos para o ano de 2026. "
                    f"Diga de forma curta e atraente que para liberar os roteiros copiáveis avançados ele deve comprar o acesso no botão abaixo."
                )
            else:
                st.info(f"⚡ Análise rápida ativada para o perfil: **{user_teste}**")

            
           
