import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve, auc

# Sayfa yapılandırması
st.set_page_config(page_title="Meme Kanseri Teşhisi", layout="wide")
st.title("🧬 Naive Bayes ile Meme Kanseri Teşhisi")

# Veriyi yükle
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.dropna(inplace=True)
    return df

df = load_data()

# Özellikler ve hedef
X = df.drop(['diagnosis'], axis=1)
y = df['diagnosis']
le = LabelEncoder()
y_encoded = le.fit_transform(y)  # B=0, M=1

# Model eğitimi
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)

# Tahmin ve metrikler
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)

# ROC eğrisi verileri
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# 🔍 Kullanıcıdan veri al
st.sidebar.header("🔍 Yeni Hasta Verisi Girin")
input_values = []
for col in X.columns:
    val = st.sidebar.number_input(col, value=float(X[col].mean()), format="%.5f")
    input_values.append(val)

# 🔮 Tahmin et
if st.sidebar.button("Teşhis Et"):
    input_array = pd.DataFrame([input_values], columns=X.columns)
    prediction = model.predict(input_array)[0]
    prediction_prob = model.predict_proba(input_array)[0][prediction]

    st.subheader("🔎 Tahmin Sonucu")

    if prediction == 1:
        st.error("🔴 **Kötü Huylu (Malignant)** tümör tespit edildi!", icon="🚨")
        st.write(f"Modelin bu tahmine olan güveni: **{prediction_prob:.2%}**")
        st.info("Bu tahmin tıbbi bir teşhis yerine geçmez. Lütfen bir uzmana danışınız.")
    else:
        st.success("🟢 **İyi Huylu (Benign)** tümör tespit edildi.", icon="✅")
        st.write(f"Modelin bu tahmine olan güveni: **{prediction_prob:.2%}**")
        st.info("Yine de düzenli kontrolleri ihmal etmeyiniz.")

# 📊 Model Performansı
st.subheader("📊 Model Performansı")
st.metric("Doğruluk Oranı", f"{acc:.2%}")

# 📌 Confusion Matrix
st.write("### ❗ Confusion Matrix")
fig_cm, ax_cm = plt.subplots()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap="Blues",
            xticklabels=le.classes_, yticklabels=le.classes_, ax=ax_cm)
plt.xlabel("Tahmin")
plt.ylabel("Gerçek")
st.pyplot(fig_cm)

# 📈 ROC Eğrisi
st.write("### 📈 ROC Eğrisi")
fig_roc, ax_roc = plt.subplots()
ax_roc.plot(fpr, tpr, label='ROC Eğrisi (AUC = %0.2f)' % roc_auc)
ax_roc.plot([0, 1], [0, 1], 'k--')
ax_roc.set_xlabel('False Positive Rate')
ax_roc.set_ylabel('True Positive Rate')
ax_roc.set_title('ROC Eğrisi')
ax_roc.legend(loc="lower right")
st.pyplot(fig_roc)

# 📃 Sınıflandırma Raporu
st.write("### 🧾 Sınıflandırma Raporu")
st.dataframe(pd.DataFrame(report).transpose().round(2))
