# NBA Moneyball: Makine Öğrenmesi ile Kontrat Tahmin Modeli

🚀 **Canlı Demo (Streamlit Web Paneli):** [Buraya Tıklayarak Karar Destek Sistemini Test Edebilirsiniz](https://nba-salary-prediction-by-calayir.streamlit.app/)

Bu proje, NBA'deki serbest oyuncuların saha içi performans metriklerine dayanarak hak ettikleri adil piyasa değerini (Fair Market Value) hesaplayan bir Karar Destek Sistemidir (Decision Support System). Proje, takım yöneticilerine (Genel Menajerler) oyuncu pazarlıklarında veri odaklı bir tavan ve taban fiyat aralığı sunmayı amaçlamaktadır.

## Proje Mimarisi ve Veri Kaynakları

Sistem iki ana bileşenden oluşmaktadır:
1. **Model Eğitimi (Arka Uç):** Spotrac (finansal veriler) ve `nba_api` (gelişmiş saha içi istatistikleri) üzerinden çekilen verilerle Python üzerinde eğitilen algoritmalar.
2. **Kullanıcı Arayüzü (Ön Uç):** Yöneticilerin oyuncu arayabileceği ve tahmini kontrat değerlerini inceleyebileceği Streamlit tabanlı interaktif web paneli.

Sisteme sadece oyuncuların attıkları toplam sayı gibi ham veriler verilmemiştir. Bunun yerine Özellik Mühendisliği (Feature Engineering) uygulanarak dakika başına üretim (PTS_PER_MIN) gibi metrikler geliştirilmiş; NET_RATING ve PIE gibi gelişmiş istatistikler kullanılarak "boş istatistik" üreten verimsiz oyuncuların tespit edilmesi sağlanmıştır.

## Çift Yönlü Karar Mekanizması (Komite Yaklaşımı)

Bu projenin en temel mühendislik farkı, tek bir algoritmaya güvenmek yerine birbirini dengeleyen iki farklı makine öğrenmesi modelinin (Model Ensembling) aynı anda kullanılmasıdır:

* 📈 **Tavan Fiyat (Random Forest):** Geçmiş piyasa verilerinin ortalamasını alan bu model, takımların yıldız oyunculara ödediği "Marka Primi" etkisini de hesaba katar. Oyuncunun pazarlıktaki maksimum beklentisini (Menajer talebini) belirler.
* 🛡️ **Taban Fiyat (XGBoost):** Çok düşük bir öğrenme hızı (learning_rate=0.005) ile muhafazakar bir şekilde eğitilmiştir. Piyasadaki şişirilmiş ve duygusal kontratları filtreleyerek oyuncunun sahadaki saf basketbol verimliliğinin matematiksel karşılığını hesaplar. Yöneticiye bütçe dostu, gerçekçi bir referans noktası sunar.

## Kurulum (Lokal Geliştirme İçin)

Eğer projenin veri çekme ve modelleme adımlarını (Backend) kendi bilgisayarınızda test etmek isterseniz:

1. Repository'i klonlayın.
2. Gerekli kütüphaneleri kurun: `pip install -r requirements.txt` *(Model eğitimi için ek olarak `xgboost`, `scikit-learn` ve `nba_api` gereklidir).*
3. Tahmin modelini çalıştırıp yeni veriyi üretin: `python salary-pred-v4.py`
4. Web panelini lokalde başlatın: `streamlit run app.py`

## Teknolojiler
* **Python** (Veri İşleme ve Makine Öğrenmesi)
* **XGBoost & Scikit-Learn** (Tahminleme Algoritmaları)
* **Streamlit** (Web Arayüzü Deployment)
* **Pandas & NBA API** (Veri Analizi ve Entegrasyon)