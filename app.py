import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Maaş Tahmini", layout="wide")

st.title("NBA Moneyball: Karar Destek Sistemi")
st.write("Bu panel, oyuncuların saha içi performanslarına göre hak ettikleri Tavan (Piyasa) ve Taban (Verimlilik) maaş aralıklarını listelemektedir.")

@st.cache_data
def load_data():
    return pd.read_csv('nba_2026_maas_tahminleri.csv')

try:
    df = load_data()

    st.sidebar.header("Kontrol Paneli")
    yas_limiti = st.sidebar.slider("Maksimum Yaş Sınırı", int(df['AGE'].min()), int(df['AGE'].max()), 40)
    
    filtrelenmis_veri = df[df['AGE'] <= yas_limiti]

    st.subheader(f"{yas_limiti} Yaş Altı Tüm Tahminler")
    st.dataframe(filtrelenmis_veri, use_container_width=True)

    st.divider()

    st.subheader("Yönetici Ekranı: Oyuncu Özel Pazarlık Analizi")
    secilen_oyuncu = st.selectbox("Pazarlık masasına oturacağınız oyuncuyu seçin:", df['PLAYER'].tolist())
    
    oyuncu_verisi = df[df['PLAYER'] == secilen_oyuncu].iloc[0]
    
    # 1. SATIR: İstatistikler
    st.write("**Oyuncu Profili ve Üretim**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Oyuncu Yaşı", value=oyuncu_verisi['AGE'])
    with col2:
        st.metric(label="Toplam Sayı (PTS)", value=int(oyuncu_verisi['PTS']))
    if 'AST' in oyuncu_verisi:
        with col3:
            st.metric(label="Toplam Asist (AST)", value=int(oyuncu_verisi['AST']))
            
    st.divider()
            
    # 2. SATIR: Finansal Komite Kararı
    st.write("**Komite Kararı: Finansal Değerleme**")
    col4, col5 = st.columns(2)
    with col4:
        st.metric(label="📈 TAVAN FİYAT (Random Forest)", value=oyuncu_verisi['RF_SALARY_2026'], delta="Menajer Beklentisi", delta_color="off")
    with col5:
        st.metric(label="🛡️ TABAN FİYAT (XGBoost)", value=oyuncu_verisi['XGB_SALARY_2026'], delta="Saf Verimlilik Değeri", delta_color="normal")

except FileNotFoundError:
    st.error("Veri dosyası bulunamadı. Lütfen ana Python betiğini çalıştırarak CSV dosyasını oluşturduğunuzdan emin olun.")