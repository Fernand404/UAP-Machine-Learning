import streamlit as st
import cnn_page
import mobilenet_page
import resnet_page

# 1. Konfigurasi Halaman
st.set_page_config(page_title="PotatoDoc AI", layout="wide")

# 2. Custom CSS untuk Sidebar Tengah & Menu Box Menyala
# CSS Utama
st.markdown("""
    <style>
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important; /* Membuat transparan */
        border-bottom: none !important;
    }
    
    /* Tombol Deploy dan Menu (Tiga Titik) di pojok kanan agar tetap putih/terlihat jika perlu */
    header[data-testid="stHeader"] svg {
        fill: #ffffff !important;
    }
    
    /* 1. Warna Background Utama */
    .stApp {
        background: linear-gradient(to bottom, #142d59 0%, #0a162b 100%);
        background-attachment: fixed; /* Menjaga gradasi tetap di tempat saat scroll */
        color: #ffffff;

    /* 2. Warna Sidebar */
    [data-testid="stSidebar"] {
        background-color: #63a2d6 !important;
    }

    /* 3. Sidebar Tengah Vertikal */
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100vh;
        background-color: #63a2d6; /* Pastikan konsisten */
    }

    /* 4. Sembunyikan Label Judul Radio */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        display: none;
    }

    /* 5. Styling Box Menu di Sidebar */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        position: relative;
        background-color: rgba(255, 255, 255, 0.2); /* Transparan putih tipis */
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding: 20px !important;
        margin-bottom: 10px;
        width: 100% !important;
        cursor: pointer;
        display: flex !important;
        align-items: center;
    }

    /* Hilangkan teks/bulatan asli Streamlit */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div {
        display: none !important;
    }

    /* 6. Teks Buatan di Sidebar (Warna Putih agar kontras dengan Biru Sidebar) */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-of-type(1)::after { content: "HOME"; }
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-of-type(2)::after { content: "CNN"; }
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-of-type(3)::after { content: "MOBILENET"; }
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-of-type(4)::after { content: "RESNET50"; }

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label::after {
        position: absolute;
        left: 20px;
        color: #ffffff; /* Putih bersih */
        font-size: 16px;
        font-weight: 600;
        visibility: visible;
    }

    /* 7. Efek Menu Aktif (Menyala saat dipilih) */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
        background-color: #142d59 !important; /* Warna Navy (sama dengan background utama) */
        border: 2px solid #ffffff;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* 8. Styling Judul dan Teks di Halaman Utama */
    h1, h2, h3, p, span {
        color: #ffffff !important;
    }
    
    /* Tombol Prediksi agar kontras */
    .stButton>button {
        background-color: #63a2d6;
        color: #142d59;
        font-weight: bold;
        border-radius: 10px;
        border: none;
    }

    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Menu
with st.sidebar:
    # Label visibility tetap collapsed agar tidak ada spasi kosong di atas
    choice = st.radio(
        "Navigation",
        ["HOME", "CNN", "MOBILENET", "RESNET50"],
        label_visibility="collapsed"
    )

# 4. Logika Navigasi Halaman
if choice == "HOME":
# Membuat Title yang lebih besar menggunakan HTML/CSS
    st.markdown("<h1 style='text-align: left; font-size: 60px; color: #4caf50; margin-bottom: 0;'>AkuKentang</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #888; margin-top: 0;'>Web Prediksi Penyakit Kentang</p>", unsafe_allow_html=True)
    # Bagian Deskripsi Utama
    st.write("""
    Dibuat untuk membantu mengidentifikasi penyakit pada kentang
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # Menggunakan kolom untuk menampilkan fitur/deskripsi model
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("CNN")
        st.write("Model arsitektur sederhana yang dibangun dari nol, cocok untuk deteksi dasar dengan performa yang ringan.")

    with col2:
        st.markdown("MobileNetV2")
        st.write("Model yang dioptimalkan untuk kecepatan. Sangat efisien dalam memproses gambar tanpa membebani memori.")

    with col3:
        st.markdown("ResNet50")
        st.write("Arsitektur paling kuat dengan *Residual Connections* untuk mengenali detail penyakit yang sulit sekalipun.")

    st.markdown("---")
    
    # Menambahkan instruksi singkat
    st.info("Pilih Menu di Kiri")
    
    
elif choice == "CNN":
    cnn_page.show_page()

elif choice == "MOBILENET":
    mobilenet_page.show_page()

elif choice == "RESNET50":
    resnet_page.show_page()