import streamlit as st
import random

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

query_params = st.query_params
token_cliente = query_params.get("token", None)
modo_admin = query_params.get("admin", None)

APP_TITULO = st.session_state["config_app"]["titulo"]
APP_SUBTITULO = st.session_state["config_app"]["subtitulo"]
APP_LOGO = st.session_state["config_app"]["logo_url"]
APP_CAPA = st.session_state["config_app"]["capa_url"]

link_suporte_whatsapp = f"https://wa.me{NUMERO_WHATSAPP}?text=Olá!%20Meu%20acesso%20Premium%20bloqueou%20porque%20mudei%20de%20dispositivo.%20Pode%20resetar%20meu%20IP?"

st.set_page_config(page_title=APP_TITULO, page_icon="🚀", layout="centered")

# Estilo para fixar o botão gigante verde chamativo no celular
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #238636 !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        height: 65px !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0,255,0,0.3) !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #2ea043 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Banco de dados de inteligência de conteúdo integrado (Estratégias de Elite 2026)
def mapear_relatorio_estrategico(username, nicho="Todos", premium=False):
    gargalos = [
        "**Retenção Crítica (0-3s):** Seus vídeos estão perdendo mais de 70% do público nos primeiros segundos porque você inicia apresentando o produto em vez de expor uma dor ou quebra de padrão visual.",
        "**Mapeamento de Algoritmo:** A conta está presa na barreira das 200 visualizações. O TikTok Shop exige metadados claros e SEO refinado nas legendas e falas para direcionar o vídeo ao público comprador correto.",
        "**Estética de Setup / Ambiente:** O visual dos takes está parecendo uma propaganda comercial tradicional. Em 2026, vídeos de afiliados que mais viralizam utilizam o modelo nativo (unboxing realista ou ASMR focado)."
    ]
    
    ganchos = [
        "Eu achei que esse produto de R$ 40 do TikTok Shop era golpe, até que eu decidi testar...",
        "Se o seu setup gamer parece uma zona de guerra por causa de cabos fios, pare tudo e mude para isso...",
        "Não compre esse produto físico no TikTok Shop antes de ver o maior erro que cometi..."
    ]
    
    if not premium:
        return f"""
        ### 📊 Diagnóstico Técnico do Algoritmo para: **{username}**
        
        ❌ **Maior Gargalo Identificado:**
        {random.choice(gargalos)}
        
        💡 **Recomendação de Gancho Viral (2026):**
        Use esta abertura exata nos primeiros 2 segundos do seu próximo vídeo:  
        *"{random.choice(ganchos)}"*
        
        ---
        ⚠️ **ANÁLISE DE CONTA INCOMPLETA:** Por se tratar de uma consulta de teste gratuito, liberamos apenas a amostra inicial do seu relatório. 
        
        Para destravar o **Gerador Automatizado de Roteiros de Alta Retenção**, o **Cronograma Diário Passo a Passo Rumo aos 2.000 seguidores** qualificados e o acesso irrestrito ao painel, clique no **Botão Verde Gigante** abaixo e garanta sua Licença Premium pelo WhatsApp.
        """
    else:
        return f"""
        ### 💎 Relatório VIP e Plano de Contingência para: **{username}**
        
        📈 **Mapeamento de Nicho:** {nicho}
        
        🎯 **Estratégia de SEO Avançada para Legendas (Copie e Use):**
        `#tiktokshop #achadinhos #produtoviral #afiliadotiktokshop #comprasonline`
        
        ---
        
        ### 🎬 Roteiro Viral Otimizado (Modelo 1 - Retenção Máxima)
        *   **[0-3s] O Gancho:** "Esse é o único item que transformou completamente a rotina do meu nicho..." *(Ação visual: take fechado mostrando o produto funcionando).*
        *   **[3-10s] Quebra de Objeção:** Explique o principal problema que o produto resolve de forma curta e dinâmica.
        *   **[10-15s] CTA Estratégica:** "O link com desconto exclusivo de frete grátis do TikTok Shop está no carrinho amarelo aqui no canto inferior esquerdo do vídeo."
        
        ---
        
        ### 📅 Cronograma de Escala Semanal (Rumo aos 2k)
        *   **Dias 1 a 3:** Postagem de 2 vídeos diários focados em Estética e Áudio Nativo (ASMR) para aquecer a conta.
        *   **Dias 4 a 7:** Postagem de 1 vídeo diário focado no modelo 'Review Sincero contra Concorrentes' para gerar alto volume de comentários e compartilhamentos.
        """

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
            st.success("✨ Visual updated!")
            st.rerun()
            
        st.markdown("---")
        st.subheader("🔑 Links Premium (Emissão de Clientes)")
        with st.form("criar_token"):
            novo_tk = st.text_input("Nome do Comprador:").strip()
            cadastrar = st.form_submit_button("➕ Gerar Novo Link de Acesso")
            if cadastrar and novo_tk:
                if novo_tk not in st.session_state["clientes_premium"]:
                    st.session_state["clientes_premium"][novo_tk] = "ativo"
                    st.success(f"Link Premium criado!")
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
        if APP_CAPA: st.image(APP_CAPA, use_container_width=True)
        if APP_LOGO: st.image(APP_LOGO, width=80)
        
        st.title("💎 Área VIP - Método 2K")
        nicho = st.selectbox("Qual o nicho do produto do seu cliente?", ["Achadinhos", "Gamer", "Beleza", "Moda", "Saúde"])
        username_premium = st.text_input("Digite o @usuario para auditoria profunda:")
        if st.button("🚀 Iniciar Auditoria Avançada"):
            with st.spinner("🧠 Gerando plano mestre de contingência..."):
                relatorio_vip = mapear_relatorio_estrategico(username_premium, nicho, premium=True)
                st.markdown(relatorio_vip)
        st.stop()

# =====================================================================
# 🚀 FLUXO C: TELA INICIAL PÚBLICA
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
        st.info(f"⚡ Análise rápida ativada para o perfil: **{user_teste}**")
        st.markdown("---")
        
        resposta_estavel = mapear_relatorio_estrategico(user_teste)
        st.markdown(resposta_estavel)
        
        # Link tratado de forma 100% nativa sem dependências
        texto_limpo = f"Olá! Analisei meu perfil @{user_teste.replace('@','')} no robô Método 2K. Fiz o teste gratuito e quero comprar o acesso Premium para liberar os roteiros avançados!"
        texto_codificado = texto_limpo.replace(" ", "%20").replace("!", "%21").replace("@", "%40")
        link_final = f"https://wa.me{NUMERO_WHATSAPP}?text={texto_codificado}"
        

