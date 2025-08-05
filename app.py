import streamlit as st
import random

st.set_page_config(page_title="CosmicMirror.ai — Apex 3D Universe", page_icon="🌌", layout="wide")

# --- 3D Cosmic Background + Card CSS (shared across all tabs) ---
st.markdown("""
<style>
body { background: #090426;}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #0b0435 10%, #27e1fa33 90%);
    min-height: 100vh; overflow: hidden;
}
.cosmic-particles {
    position: fixed; z-index: -1; width: 100vw; height: 100vh; left: 0; top: 0; pointer-events: none;
}
.particle {
  position: absolute; border-radius: 50%; opacity: .6;
  background: linear-gradient(120deg,#27e1fa,#ff27fa);
  pointer-events: none; animation: moveParticle 19s linear infinite;
}
@keyframes moveParticle {
    0% { transform: translateY(0) scale(.8);}
    100% { transform: translateY(-95vh) scale(1.28);}
}
.cosmic-3d-title {
    font-size: 2.5rem; font-weight: bold;
    background: linear-gradient(90deg, #fff, #00e9fa 50%, #ff27fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-shadow: 0 2px 30px #00e9fa88, 0 0 2px #fff;
    letter-spacing: .1em; margin-bottom: 1rem;
}
.cosmic-nav { display: flex; flex-direction: row; gap: 1.2rem; margin-bottom: 1.7rem; justify-content: center; }
.cosmic-nav button {
    border-radius: 1.2rem;
    background: linear-gradient(100deg,#191637,#27e1fa77 100%);
    color: #fff; font-size: 1.05rem; font-weight: 500;
    padding: 0.7rem 2.1rem; border: none;
    box-shadow: 0 0 18px 2px #00e9fa33; margin: 0; cursor: pointer;
    transition: all 0.22s;
}
.cosmic-nav button.selected, .cosmic-nav button:hover {
    background: linear-gradient(100deg, #27e1fa 30%, #ff27fa 100%);
    color: #fff; transform: scale(1.07) rotate(-1deg);
    box-shadow: 0 0 40px 8px #ff27fa77;
}
::-webkit-scrollbar-thumb { background: #27e1fa66; border-radius: 8px;}
::-webkit-scrollbar { width: 10px;}
.cosmic-card {
    border-radius: 2rem;
    box-shadow: 0 0 40px 10px #27e1fa55, 0 0 4px 1px #fff6;
    background: rgba(23,27,44,0.99);
    padding: 2.2rem 2.1rem 2rem 2.1rem;
    margin: 2.1rem auto 1.2rem auto;
    color: #fff;
    max-width: 530px;
    transition: box-shadow 0.4s;
}
.cosmic-card:hover {
    box-shadow: 0 0 60px 16px #ff27facc, 0 0 8px 2px #00e9e966;
}
</style>
""", unsafe_allow_html=True)

# --- Animated Particle Background ---
def particles_html(n=28):
    html = '<div class="cosmic-particles">'
    for _ in range(n):
        left = random.randint(1, 98)
        size = random.randint(9, 26)
        dur = round(random.uniform(10, 22),2)
        delay = round(random.uniform(0,11),2)
        html += f'<div class="particle" style="left:{left}vw; bottom:-7vh;width:{size}px;height:{size}px;animation-duration:{dur}s;animation-delay:-{delay}s;"></div>'
    html += '</div>'
    return html
st.markdown(particles_html(), unsafe_allow_html=True)

# --- 3D Navigation Bar ---
tabs = [
    "Home", "File Conversion", "NFT Gallery", "Voice AI", "AI File Chat",
    "Leaderboard", "Community", "Dashboard", "Profile", "Support"
]
if "tab" not in st.session_state:
    st.session_state.tab = tabs[0]

nav_html = '<div class="cosmic-nav">'
for tab in tabs:
    selected = 'selected' if tab == st.session_state.tab else ''
    nav_html += f'<button class="cosmic-nav button {selected}" onClick="window.location.search=\'?tab={tab.replace(\' \',\'_\')}\'">{tab}</button>'
nav_html += '</div>'
st.markdown('<div class="cosmic-3d-title">🌌 CosmicMirror.ai</div>', unsafe_allow_html=True)
st.markdown('<center><i>The Ultimate 3D Cosmic App — All Phases, All Features Unlocked</i></center>', unsafe_allow_html=True)
st.markdown("---")
st.markdown(nav_html, unsafe_allow_html=True)

# --- Tab Routing ---
import streamlit_javascript as st_js
query_tab = st_js.st_javascript("window.location.search").split("tab=")[-1].replace("_"," ") if "tab=" in st_js.st_javascript("window.location.search") else tabs[0]
if query_tab in tabs:
    st.session_state.tab = query_tab

# --- Helper Card Function
def cosmic_card(title, content):
    st.markdown(f'<div class="cosmic-card"><h3>{title}</h3>{content}</div>', unsafe_allow_html=True)

# --- Home ---
if st.session_state.tab == "Home":
    cosmic_card("Welcome Home, Cosmic Creator 🚀", """
    - Convert any file, mint NFTs, chat with digital twins, earn, and lead!
    - All features, all languages, all countries, all users: now live.
    - Powered by the universe's most advanced cosmic engine.
    """)

# --- File Conversion ---
elif st.session_state.tab == "File Conversion":
    cosmic_card("🛸 3D Cosmic File Converter", "Convert any file—text, image, audio, video—to any format. Fast, secure, cosmic!")
    uploaded_file = st.file_uploader("Upload your file", type=["txt", "pdf", "jpg", "png", "mp3", "mp4", "docx", "csv", "xlsx", "zip"])
    output_format = st.selectbox("Choose Output Format", ["PDF", "TXT", "JPG", "PNG", "MP3", "MP4", "CSV", "XLSX", "ZIP", "Other (AI will decide)"])
    if st.button("🚀 Convert Now"):
        if uploaded_file:
            st.success(f"File '{uploaded_file.name}' received. 🚀 Conversion to {output_format} will begin (add backend logic here)!")
        else:
            st.warning("Please upload a file first.")

# --- NFT Gallery ---
elif st.session_state.tab == "NFT Gallery":
    nft_data = [
        {"img": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=600&q=80", "name": "Cosmic Tiger", "artist": "Hemanth", "price": "0.11 ETH"},
        {"img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=600&q=80", "name": "Galactic Orb", "artist": "Vēda AI", "price": "0.18 ETH"},
        {"img": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=600&q=80", "name": "Quantum City", "artist": "Cosmic Creator", "price": "0.29 ETH"},
    ]
    st.markdown('<div class="cosmic-card" style="max-width: 1200px;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.4rem;font-weight:700;margin-bottom:.7rem;">🌠 3D NFT Gallery</div>', unsafe_allow_html=True)
    gallery_html = '<div style="display:flex;gap:2.2rem;justify-content:center;flex-wrap:wrap;">'
    for n in nft_data:
        gallery_html += f'''
        <div style="width:270px;height:350px;background:linear-gradient(120deg,#1b1d34 75%,#27e1fa33 100%);border-radius:2rem;box-shadow:0 8px 40px #27e1fa66,0 2px 14px #ff27fa44;overflow:hidden;position:relative;transform-style:preserve-3d;animation:spinCard 7s linear infinite;transition:box-shadow .34s;">
            <img src="{n['img']}" style="width:100%;height:66%;object-fit:cover;border-top-left-radius:2rem;border-top-right-radius:2rem;box-shadow:0 2px 22px #00e9fa77;">
            <div style="padding:1.4rem;color:#fff;font-family:'Segoe UI',sans-serif;">
                <h3 style="margin:0;font-size:1.18rem;font-weight:700;background:linear-gradient(90deg,#fff,#27e1fa 70%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">{n["name"]}</h3>
                <p style="margin:.2rem 0 .1rem 0;"><b>Artist:</b> {n["artist"]}</p>
                <p style="margin:.2rem 0;"><b>Price:</b> <span style="color:#27e1fa;">{n["price"]}</span></p>
                <p style="margin:0;"><b>Status:</b> <span style="color:#ff27fa;">Available</span></p>
            </div>
        </div>
        '''
    gallery_html += '</div>'
    st.markdown(gallery_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Voice AI ---
elif st.session_state.tab == "Voice AI":
    cosmic_card("🎤 Voice AI", "Talk to Vēda or generate audio NFTs. [Plug in Whisper/OpenAI or TTS logic here.]")

# --- AI File Chat ---
elif st.session_state.tab == "AI File Chat":
    cosmic_card("💬 AI File Chat", "Chat, summarize, search, and analyze any file using AI! [Add multimodal logic here.]")

# --- Leaderboard ---
elif st.session_state.tab == "Leaderboard":
    leaders = [
        {"rank": 1, "name": "Hemanth", "score": 10250, "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=hemanth"},
        {"rank": 2, "name": "Vēda AI", "score": 9950, "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=veda"},
        {"rank": 3, "name": "Cosmic Creator", "score": 9250, "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=cosmos"},
    ]
    st.markdown('<div class="cosmic-card" style="max-width:560px;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.23rem;font-weight:700;margin-bottom:.5rem;">🏆 Cosmic Leaderboard</div>', unsafe_allow_html=True)
    for l in leaders:
        st.markdown(f'''
            <div style="margin:0.8rem 0;">
                <img src="{l["avatar"]}" style="width:44px;height:44px;border-radius:50%;margin-right:0.6rem;object-fit:cover;border:2.2px solid #fff9;box-shadow:0 0 18px #27e1fa44;">
                <span style="font-weight:600;font-size:1.13rem;background:linear-gradient(90deg,#fff,#00e9fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">#{l["rank"]} {l["name"]}</span>
                <span style="color:#00e9fa;font-size:1.21rem;margin-left:0.4rem;">{l["score"]}</span>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('<div style="margin-top:1.3rem;color:#fff9;">Anyone can join the leaderboard, earn NFTs, and become a cosmic legend!</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Community Wall ---
elif st.session_state.tab == "Community":
    community = [
        {"name": "Shweta", "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=shweta", "city": "Mumbai", "country": "India", "about": "NFT artist & twin creator"},
        {"name": "Elon", "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=elon", "city": "Austin", "country": "USA", "about": "3D digital twin dev"},
        {"name": "Aliya", "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=aliya", "city": "Istanbul", "country": "Turkey", "about": "AI file converter & marketplace champ"},
    ]
    st.markdown('<div class="cosmic-card" style="max-width:900px;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.2rem;font-weight:700;margin-bottom:.8rem;">🌐 Cosmic Community Wall</div>', unsafe_allow_html=True)
    wall_html = '<div style="display:flex;gap:2.1rem;justify-content:center;flex-wrap:wrap;">'
    for m in community:
        wall_html += f'''
        <div style="background:linear-gradient(120deg,#222166,#27e1fa33 100%);border-radius:2.3rem;box-shadow:0 0 18px #27e1fa99;padding:1.2rem 1.7rem;min-width:210px;max-width:260px;color:#fff;font-size:1.04rem;text-align:left;margin-bottom:1.2rem;border:2px solid #fff4;transition:transform .22s,box-shadow .22s;">
            <img src="{m["avatar"]}" style="width:44px;height:44px;border-radius:50%;margin-right:0.7rem;object-fit:cover;border:2.2px solid #fff9;">
            <span style="font-size:1.1rem;font-weight:600;">{m["name"]}</span><br>
            <span style="color:#27e1fa;">{m["city"]}, {m["country"]}</span><br>
            <span>{m["about"]}</span>
        </div>
        '''
    wall_html += '</div>'
    st.markdown(wall_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Dashboard & Analytics ---
elif st.session_state.tab == "Dashboard":
    metrics = [
        {"title": "Active Users (24h)", "value": "7,352", "note": "+291 today"},
        {"title": "Pro Upgrades (Today)", "value": "391", "note": "New record!"},
        {"title": "NFTs Minted", "value": "102", "note": "All cosmic twins"},
        {"title": "Revenue (Today)", "value": "$210", "note": "Total: $53,400"},
        {"title": "Top City", "value": "Bengaluru", "note": "India"},
        {"title": "Support Requests", "value": "4", "note": "All resolved!"},
    ]
    st.markdown('<div class="cosmic-card" style="max-width:1120px;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.32rem;font-weight:800;margin-bottom:1.1rem;">📊 3D Cosmic Dashboard & Analytics</div>', unsafe_allow_html=True)
    dashboard_html = '<div style="display:flex;gap:2.2rem;justify-content:center;flex-wrap:wrap;">'
    for m in metrics:
        dashboard_html += f'''
        <div style="background:linear-gradient(120deg,#232166,#27e1fa22 100%);border-radius:1.6rem;box-shadow:0 0 14px #27e1fa99;padding:1.3rem 2rem;color:#fff;font-size:1.07rem;text-align:center;margin-bottom:1rem;min-width:250px;">
            <div style="font-weight:700;font-size:1.09rem;background:linear-gradient(90deg,#fff,#27e1fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.2rem;">{m["title"]}</div>
            <div style="font-size:1.83rem;font-weight:900;color:#27e1fa;margin-bottom:.2rem;text-shadow:0 2px 14px #ff27fa77;">{m["value"]}</div>
            <div style="font-size:1rem;color:#ff27fa;font-style:italic;">{m["note"]}</div>
        </div>
        '''
    dashboard_html += '</div>'
    st.markdown(dashboard_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Profile & Achievements ---
elif st.session_state.tab == "Profile":
    avatar = "https://api.dicebear.com/7.x/bottts/svg?seed=hemanth"
    user = {
        "name": "Hemanth",
        "location": "Bengaluru, India",
        "pro": True,
        "joined": "2024-12-30",
        "badges": ["Cosmic Pro", "NFT Creator", "Top Referrer", "Contest Winner"],
        "stats": {
            "NFTs Minted": 48,
            "Twins Created": 191,
            "Total Earnings": "$2,300",
            "Rank": "#1 Cosmic"
        }
    }
    st.markdown('<div class="cosmic-card" style="max-width:470px;">', unsafe_allow_html=True)
    st.markdown(f'<img src="{avatar}" style="width:104px;height:104px;border-radius:50%;object-fit:cover;margin-bottom:0.8rem;border:4px solid #27e1fa;box-shadow:0 0 22px #ff27fa88;">', unsafe_allow_html=True)
    st.markdown(f'<span style="font-size:1.35rem;font-weight:800;background:linear-gradient(90deg,#fff,#27e1fa 60%,#ff27fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.4rem;display:block;">{user["name"]}</span>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:1.09rem;color:#ff27fa;margin-bottom:1.2rem;">🌍 {user["location"]} | Joined: {user["joined"]}</div>', unsafe_allow_html=True)
    if user["pro"]:
        st.markdown('<div style="color:#27e1fa;font-size:1.1rem;font-weight:700;">🌟 Cosmic Pro User</div>', unsafe_allow_html=True)
    st.markdown('<div style="display:flex;gap:1.2rem;justify-content:center;margin:1.5rem 0 1rem 0;flex-wrap:wrap;">' + ''.join(
        f'<div style="background:linear-gradient(90deg,#27e1fa 70%,#ff27fa 100%);color:#fff;border-radius:1.6rem;padding:0.52rem 1.2rem;font-weight:700;box-shadow:0 0 20px #27e1fa44;font-size:1.1rem;margin-bottom:0.5rem;border:2.2px solid #fff4;transition:transform .22s;">{badge}</div>' for badge in user["badges"]
    ) + '</div>', unsafe_allow_html=True)
    st.markdown('<div style="display:flex;gap:1.1rem;justify-content:center;margin-top:1.1rem;flex-wrap:wrap;">' + ''.join(
        f'<div style="background:linear-gradient(120deg,#232166,#27e1fa22 100%);border-radius:1.1rem;box-shadow:0 0 10px #27e1fa99;padding:1rem 1.6rem;color:#fff;font-size:1.05rem;text-align:center;margin-bottom:1rem;"><b>{k}</b><br>{v}</div>' for k,v in user["stats"].items()
    ) + '</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Support / Veda AI ---
elif st.session_state.tab == "Support":
    cosmic_card("🛟 Help & Vēda AI", "Ask anything, get 24/7 AI support. [Live bot, guides, and documentation coming soon!]")

# --- Footer ---
st.markdown("""
<br>
<center><small>© 2025 CosmicMirror.ai | The Ultimate 3D Cosmic App | All Phases, All Features, All Running 🚀</small></center>
""", unsafe_allow_html=True)
