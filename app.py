import streamlit as st
import datetime

# ==============================================================================
# [Vibe 設定] 頁面核心配置與主題高級感塑造
# ==============================================================================
st.set_page_config(
    page_title="Larry Lai | 數位轉型專家簡歷",
    page_icon="⚡",
    layout="centered",  # 讓內容聚焦在中間，極具現代網頁的呼吸感
    initial_sidebar_state="collapsed"
)

# 用極簡 CSS 注入靈魂：霓虹藍調 (Cyber Blue Vibe)
st.markdown("""
    <style>
    /* 全域色調與科技感暗色背景 */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0f19;
        color: #f1f5f9;
        font-family: '-apple-system', BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 移除 Streamlit 頂部預設的多餘空白 */
    [data-testid="stHeader"] {
        background: transparent;
    }
    
    /* 頂級宣傳標語外框 (Slogan Badge) */
    .promo-banner {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(99, 102, 241, 0.15) 100%);
        border: 1px solid rgba(14, 165, 233, 0.3);
        color: #38bdf8;
        padding: 8px 18px;
        border-radius: 30px;
        font-size: 0.95rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1.5rem;
        letter-spacing: 1.5px;
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);
    }
    
    /* 名字的高級漸層字體 */
    .name-gradient {
        font-size: 3.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 30%, #64748b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    /* 公司與職稱樣式 */
    .subtitle-text {
        font-size: 1.35rem;
        color: #38bdf8;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    .subtitle-text span {
        color: #94a3b8;
        font-weight: 300;
        margin: 0 10px;
    }
    
    /* 聯絡資訊卡片區 */
    .contact-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 2.5rem;
    }
    .contact-line {
        font-size: 1.05rem;
        color: #cbd5e1;
        margin: 10px 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    /* 網路資訊公司常見服務卡片效果 */
    .service-box {
        background: #131c2e;
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 28px;
        height: 100%;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .service-box:hover {
        transform: translateY(-6px);
        border-color: rgba(56, 189, 248, 0.35);
        background: #17223b;
        box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.7);
    }
    .service-icon {
        font-size: 2.2rem;
        margin-bottom: 15px;
    }
    .service-h3 {
        color: #f8fafc;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 12px;
    }
    .service-p {
        color: #94a3b8;
        font-size: 0.98rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# [Layout 佈局] 主視覺 Hero Section (左側核心文字 / 右側精緻頭像)
# ==============================================================================
hero_left, hero_right = st.columns([1.4, 1], gap="large")

with hero_left:
    # 網路資訊公司熱血宣傳標語
    st.markdown('<div class="promo-banner">⚡ 網通天下 • 智領未來 ｜ 企業數位轉型的堅實後盾</div>', unsafe_allow_html=True)
    
    # 姓名與身份
    st.markdown('<h1 class="name-gradient">Larry Lai</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">南台資訊有限公司<span>|</span>學生</p>', unsafe_allow_html=True)
    
    # 聯絡資訊元件
    st.markdown(
        """
        <div class="contact-card">
            <div class="contact-line">📧 <b>電子郵件:</b> 6b4p1012@stust.edu.tw</div>
            <div class="contact-line">📞 <b>連絡電話:</b> 06-253-3131</div>
            <div class="contact-line">📍 <b>技術基地:</b> 台灣，台南市 (STUST)</div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # 互動式行動呼籲按鈕 (Vibe 互動加強)
    if st.button("💬 點擊此處，即刻洽談合作"):
        st.balloons()  # 噴出慶祝氣球，拉滿情緒價值！
        st.toast("正在複製信箱並準備開啟郵件客戶端...", icon="🚀")
        st.markdown(f'<meta http-equiv="refresh" content="1;URL=\'mailto:6b4p1012@stust.edu.tw\'">', unsafe_allow_html=True)

with hero_right:
    st.write("") # 留空微調垂直對齊
    st.write("")
    # 載入並渲染上傳的個人頭像圖片
    try:
        st.image("下載.jfif", caption="Larry Lai | 專案代表留影", use_column_width=True)
    except FileNotFoundError:
        st.error("⚠️ 未偵測到 '下載.jfif'，請確認圖檔已放入同級目錄。")

# 優雅的科技質感分割線
st.markdown("<br><hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.07);'><br>", unsafe_allow_html=True)

# ==============================================================================
# [Content 內容區] 網路資訊公司常見四大頂級服務項目 (2x2 Grid)
# ==============================================================================
st.markdown("<h2 style='text-align: center; font-size: 2rem; font-weight: 800; margin-bottom: 2.5rem; letter-spacing: 1px;'>🛠️ 南台資訊有限公司 • 核心服務範疇</h2>", unsafe_allow_html=True)

# 建立兩列佈局
grid_row1_col1, grid_row1_col2 = st.columns(2, gap="large")
grid_row2_col1, grid_row2_col2 = st.columns(2, gap="large")

with grid_row1_col1:
    st.markdown("""
        <div class="service-box">
            <div class="service-icon">🌐</div>
            <div class="service-h3">企業網路架構與高速機房規劃</div>
            <div class="service-p">專為企業量身打造高頻寬、低延遲的網通基建。包含智慧路由配置、跨國 VPN 串聯、硬體防火牆部署及伺服器機房動態負載平衡設定。</div>
        </div>
    """, unsafe_allow_html=True)

with grid_row1_col2:
    st.markdown("""
        <div class="service-box">
            <div class="service-icon">🛡️</div>
            <div class="service-h3">全方位資訊安全防護與滲透測試</div>
            <div class="service-p">提供全網端點安全防護、白帽駭客級資安防禦滲透。進行漏洞掃描與 DDoS 惡意流量清洗，建立無懈可擊的企業數位資產防護牆。</div>
        </div>
    """, unsafe_allow_html=True)

# 行動端適應留白
st.write("") 

with grid_row2_col1:
    st.markdown("""
        <div class="service-box">
            <div class="service-icon">☁️</div>
            <div class="service-h3">混合雲端部署與無縫數位轉型</div>
            <div class="service-p">協助傳統產業與中小企業將核心業務「系統上雲」(AWS / Azure / GCP)。導入高可用性容器技術（Docker / K8s），實現彈性擴充。</div>
        </div>
    """, unsafe_allow_html=True)

with grid_row2_col2:
    st.markdown("""
        <div class="service-box">
            <div class="service-icon">💻</div>
            <div class="service-h3">客製化商務軟體與大數據系統開發</div>
            <div class="service-p">因應特定商務邏輯，開發高度自動化的 ERP、CRM 管理系統與高併發 Web App，並進行自動化 API 對接，完美消除企業資訊孤島。</div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# [Footer 頁尾區]
# ==============================================================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
this_year = datetime.datetime.now().year
st.markdown(
    f"<p style='text-align: center; color: #475569; font-size: 0.9rem; font-weight: 400;'>"
    f"&copy; {this_year} <b>Larry Lai</b> ｜ 南台資訊有限公司. All rights reserved.</p>", 
    unsafe_allow_html=True
)