import streamlit as st

def calculate_love_score(name1, name2):
    names = (name1 + name2).lower()
    w1 = "true"
    w2 = "love"
    result1 = sum(names.count(ch) for ch in w1)
    result2 = sum(names.count(ch) for ch in w2)
    score = int(f"{result1}{result2}")
    return score

# 🌈 Stylish background and darker readable text
def add_background():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #ffecd2, #fcb69f);
            font-family: 'Segoe UI', sans-serif;
            color: #3c3c3c;
        }
        h1, h2, h4, .stMarkdown {
            color: #61122f;
        }
        .stTextInput > div > div > input {
            background-color: #fff0f0;
            color: #333;
        }
+        </style>
    """, unsafe_allow_html=True)

def show_gif(url):
    st.markdown(f"<div style='text-align:center'><img src='{url}' width='300'></div>", unsafe_allow_html=True)

# Page Config
st.set_page_config(page_title="💘 Love Calculator", page_icon="💖", layout="centered")

add_background()

# Title
st.markdown("<h1 style='text-align: center;'>💘 Love Compatibility Calculator 💘</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Enter two names and check how compatible you are 💑 #CoupleGoals</h4>", unsafe_allow_html=True)

# Input Section
name1 = st.text_input("🧑 Your Name")
name2 = st.text_input("👩 Partner's Name")

if st.button("💓 Calculate Love Score"):
    if not name1.strip() or not name2.strip():
        st.warning("😅 Please enter both names to continue.")
    else:
        score = calculate_love_score(name1, name2)
        st.markdown(f"<h2 style='text-align: center;'>❤️ Love Score: {score}% ❤️</h2>", unsafe_allow_html=True)

        if score > 80:
            show_gif("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif")
            st.success("Perfect match! You're meant to be 💍💑")
            st.balloons()
        elif score > 50:
            show_gif("https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif")
            st.info("A strong bond is forming 💞")
        else:
            show_gif("https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif")
            st.warning("Maybe just friends for now 😅")

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:#61122f'>Made with ❤️ </div>", unsafe_allow_html=True)

