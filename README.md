🧬 Proje Açıklaması
Modül Açıklama
Kullanıcıdan alınan biyopsi ölçümleriyle, tümörün iyi huylu (Benign) mu yoksa kötü huylu (Malignant) mu olduğunu tahmin eder.
Akıllı Tahmin Sistemi
Naive Bayes algoritmasıyla çalışır. Kullanıcının girdiği değerlere göre sonucu anlık olarak tahmin eder.
Yapay Zeka Destekli Geri Bildirim
Tahmin sonrası sınıflandırma raporu, doğruluk oranı, ROC eğrisi gibi performans metrikleri sunar.
Raporlama Paneli
Model doğruluğu, confusion matrix, sınıflandırma skoru gibi görsel ve metinsel raporlar üretir.
🔧 Uygulama Özellikleri
Gaussian Naive Bayes algoritması (scikit-learn)
Streamlit ile kullanıcı dostu web arayüzü
Hasta verileri için manuel giriş paneli
Gerçek zamanlı tahmin
Görselleştirmeler: ROC eğrisi, Confusion Matrix
Performans metrikleri: Doğruluk, Precision, Recall, F1-score
Uyarı: Sonuçlar yalnızca öngörü amaçlıdır, tıbbi teşhis yerine geçmez
👨‍🏫 Hedef Kitle
Tıp öğrencileri
Veri bilimi ve makine öğrenmesi öğrenen öğrenciler
Sağlık alanında çalışan yapay zeka geliştiricileri
Eğitim amaçlı demo projeler arayan akademisyenler
Medikal yazılım girişimcileri
🚀 Sprint 1 Süreci
Sprint Planlaması – SmartDiagnosis Projesi
Toplam Backlog Puanı: 120 Sprint 1 Hedefi: 40 puan Sprint 3 aşamada yürütülecek şekilde planlandı
Görev Renk Kodları:
🟧 Veri Analizi & Ön İşleme
🟥 Model Geliştirme (Naive Bayes)
🟩 Streamlit Arayüz Geliştirme
🟦 Görselleştirme & Raporlama
🟨 Dokümantasyon ve Uyarı Sistemleri
Sprint 1'de Tamamlanan Görevler (Toplam 40 puan):
Naive Bayes algoritması eğitildi (%80 eğitim, %20 test)
Kullanıcı arayüzü geliştirildi (sol panel giriş – tahmin butonu)
ROC eğrisi ve Confusion Matrix eklendi
Uyarı metni ve sonuç açıklamaları hazırlandı
💬 Daily Scrum
Toplantılar WhatsApp üzerinden yürütüldü. 4 Kişilik takımımızdan 2 kişi projeyi ghostlamaya başladı.Mentörümüze ilettik.
📌 Sprint Board
Miro platformu kullanıldı Akış: Backlog → To-Do → In Progress → Done Sürekli güncellendi, ilerleme anlık olarak takip edildi
🧪 Sprint Review
Model 10 farklı hasta verisiyle test edildi Doğruluk oranı %95+ Uygulama arayüzü kullanıcılar tarafından anlaşılır bulundu
🔄 Sprint Retrospective
Grup 1 (Berk): Yeni algoritmaların entegrasyonu (ör. Random Forest karşılaştırması). Yeni veri kümeleri ile genişletme planlandı.
Grup 2 (Tuba): Hata kontrolü ve kullanıcı deneyiminin artırılması. Form validasyonu, görsel tutarlılık ve uyarı sistemleri geliştirilecek
📂 Veri Kümesi
Dataset: Breast Cancer Wisconsin Diagnostic Dataset
Özellikler: radius_mean, texture_mean, area_mean, compactness_mean, …
Hedef değişken: diagnosis (M = Malignant, B = Benign)
🔗 Uygulama Çalıştırma
streamlit run app1.py
⚠️ data.csv dosyasının app1.py ile aynı klasörde bulunması gerekir.



🚀 Sprint 2 Süreci – SmartDiagnosis Projesi
✅ Sprint Planlaması
Toplam Backlog Puanı: 120 Sprint 2 Hedefi: 40 puan Tahmin Mantığı: Geliştirilen temel sistem üzerine yeni özelliklerin entegrasyonu planlandı. Görev puanları önceki sprintteki gerçek tamamlama sürelerine göre yeniden dengelendi.
🗂️ Sprint Notları
Yeni veri giriş doğrulama sistemi planlandı
Karar ağacı (Decision Tree) ile Naive Bayes modelinin karşılaştırılması hedeflendi
Kullanıcı arayüzünde hasta geçmişi görüntüleme modülü eklenecek
🟦 Tamamlanacak Görev Renk Kodları
🟥: Yeni algoritma entegrasyonu (Decision Tree)
🟩: Arayüzde geçmiş teşhisleri listeleme
🟨: Gelişmiş raporlama ekranları
🟦: Model karşılaştırma grafikleri
🟧: Girdi doğrulama sistemleri (hatalı değer engelleme)

💬 Daily Scrum
2 günde bir Zoom toplantıları gerçekleştirildi.

📌 Sprint Board Updates
Miro üzerinden yürütüldü: Backlog → To Do → In Progress → Done Sprint 2 boyunca toplam 5 görev başarıyla tamamlandı.

📸 Screenshot
Tamamlanan modüllerden ekran görüntüleri alındı ve dokümantasyona eklendi (örn. hasta geçmişi tablosu, karşılaştırmalı grafik ekranı).

🧪 Sprint Review
Decision Tree modeli %94 doğrulukla çalıştı, Naive Bayes'e yakın sonuçlar verdi
Kullanıcılar geçmiş sonuçlara ulaşabildi
Hatalı veri girişi engellendi, kullanıcı memnuniyeti arttı

🔄 Sprint Retrospective
Grup 1 (Berk):
Amaç: Yeni algoritmaların kıyaslanması ve kullanıcı arayüzüne yönelik yeniliklerin planlanması
Feedback sonrası grafiksel rapor modülü planlandı
Grup 2 (Tuba):
Amaç: Test kapsamının genişletilmesi ve hata izleme modülü eklenmesi
Kullanıcı deneyimini ölçen basit bir memnuniyet formu geliştirildi


