import streamlit as st
from PIL import Image
from streamlit_player import st_player

st.set_page_config(page_title="İyi ki Doğdun Emir Selim!", layout="centered")

# Başlık
st.markdown("<h1 style='text-align: center; color: gold;'>🎉 İYİ Kİ DOĞDUN EMİR SELİM! 🎂</h1>", unsafe_allow_html=True)

# Başlık vs... sonra
audio_file = open("media/Simge.mp3", "rb")
audio_bytes = audio_file.read()

st.subheader("🎵 En sevdiğin şarkı çalıyor...")
st.audio(audio_bytes, format="audio/mp3")

# Mesaj
st.markdown("<h3 style='text-align: center;'>Emir seni çok seviyorum, küçük kardeşim! ❤️</h3>", unsafe_allow_html=True)

# Fotoğraflar
st.header("📸 Harika Anılar")
image_paths = [
    "media/1.jpg",
    "media/2.jpg",
    "media/3.jpg",
    "media/4.jpg",
    "media/5.jpg",
    "media/6.jpg",
    "media/7.jpg",
    "media/8.jpg"
]
captions = [
    "Emir Selim 🌟",
    "Gülümsemen yeter 😊",
    "Yakışıklılık burada 😎",
    "TV keyfi zamanı 📺",
    "Bilge çocuk 👓",
    "Abi-kardeş sevgisi 💚",
    "Model gibi pozlar 🧢",
    "Çiçek gibi Emir 🌼"
]

for path, caption in zip(image_paths, captions):
    st.image(path, caption=caption, use_column_width=True)

# Sürpriz kutu
st.header("🎁 Sürpriz")
if st.button("✨ Sürpriz kutuyu aç!"):
    st.balloons()
    st.success("En tatlı Galatasaraylı sensin, Osimhen seni görse çok sevinirdi!")
    video_file = open("media/video.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

# Alt metin
st.markdown("---")
st.write("Hazırlayan: ❤️ Mustafa Abin")
