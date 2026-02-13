import streamlit as st
import time
import base64
from streamlit.components.v1 import html

# ---------- SESSION ----------
if "started" not in st.session_state:
    st.session_state.started = False
if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Yash ❤️ Forever", page_icon="💍")

# ---------- MUSIC ----------
def play_music():
    try:
        with open("love.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            html(f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """, height=0)
    except:
        st.warning("Add love.mp3")

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}
.title {
    font-size: 42px;
    color: #ff4b6e;
    text-align: center;
}
.center {
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 class='title'>Yash ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>This journey is only for you 💕</p>", unsafe_allow_html=True)

# ---------- START BUTTON ----------
if st.button("Start Our Story 💖"):
    st.session_state.started = True

# ---------- STORY FLOW ----------
if st.session_state.started:

    play_music()

    st.subheader("🌙 Yash, do you remember the first time we met?")
    st.write("That day changed my life forever… ❤️")

    st.subheader("💑 Our beautiful memories")
    st.image(["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"], width=250)

    st.subheader("❤️ What I love about you, Yash")
    st.write("Your smile… your kindness… your heart…")
    st.write("You make my life complete 💕")

    st.subheader("🌹 From my heart")
    st.write("तू आहेस म्हणून आयुष्य सुंदर आहे…")
    st.write("तू माझं सर्व काही आहेस Yash ❤️")

    st.subheader("⏳ Something important is coming…")
    for i in range(5, 0, -1):
        st.write(i)
        time.sleep(0.7)

    st.markdown("## 💍 Yash, will you be my Valentine forever?")

    col1, col2 = st.columns(2)

    # ---------- YES ----------
    with col1:
        if st.button("YES 💍"):
            st.session_state.celebrate = True

    # ---------- SMART NO ----------
    with col2:
        html("""
        <button onclick="
        this.innerText='Try again 😏';
        this.style.position='absolute';
        this.style.left=Math.random()*80+'%';
        this.style.top=Math.random()*80+'%';
        "
        style="
        padding:12px 22px;
        border-radius:20px;
        border:none;
        font-size:16px;
        cursor:pointer;
        ">
        NO 🙈
        </button>
        """, height=150)

# ---------- CELEBRATION ----------
if st.session_state.celebrate:

    # 🎆 Fireworks
    html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
    var duration = 6 * 1000;
    var end = Date.now() + duration;

    (function frame() {
      confetti({
        particleCount: 7,
        angle: 60,
        spread: 55,
        origin: { x: 0 }
      });
      confetti({
        particleCount: 7,
        angle: 120,
        spread: 55,
        origin: { x: 1 }
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    }());
    </script>
    """, height=0)

    st.balloons()

    for _ in range(7):
        st.markdown("## ❤️ 💖 💕 💘 💞")
        time.sleep(0.3)

    st.success("Yash said YES ❤️ Forever begins now!")

    st.markdown("""
    ## 💍 Our forever journey starts today  
    ### I promise to love you, support you, and stand beside you always ❤️  
    ### Thank you for being my life, my happiness, my everything 😘  
    """)
