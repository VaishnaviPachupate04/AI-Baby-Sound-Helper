import streamlit as st
from main import process_baby_sound

st.set_page_config(
    page_title="AI Baby Sound Helper 👶🎧",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        background: linear-gradient(135deg, #FFF5F7 0%, #F0F8FF 100%);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    @keyframes fadeInDown {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    @keyframes slideInUp {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .header-title {animation: fadeInDown 0.8s ease-out;}
    .card {animation: slideInUp 0.6s ease-out;}
    
    .stButton > button {
        background: linear-gradient(135deg, #FF6B9D 0%, #FF8A65 100%) !important;
        color: white !important;
        font-weight: bold;
        font-size: 16px;
        padding: 12px 30px;
        border-radius: 25px;
        border: none !important;
        box-shadow: 0 6px 20px rgba(255, 107, 157, 0.4) !important;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 107, 157, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div style='text-align:center; padding: 40px 20px 20px 20px;' class='header-title'>
    <h1 style='font-size: 48px; color: #FF6B9D; font-weight: bold; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>
        👶 AI Baby Sound Helper
    </h1>
    <p style='font-size: 20px; color: #666; margin-bottom: 8px;'>💬 Intelligent Baby Cry Analysis</p>
    <p style='font-size: 14px; color: #999;'>Powered by CrewAI & Gemini • Safe & Non-Medical ❤️</p>
    <div style='margin-top: 20px;'>
        <span style='display: inline-block; background: rgba(255, 107, 157, 0.1); padding: 8px 16px; border-radius: 20px; color: #FF6B9D; font-size: 13px; font-weight: 600;'>
            ✨ Your Personal Caregiver Assistant
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# MAIN CONTENT
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #fff8f3 0%, #ffe8d6 100%); padding: 30px; border-radius: 20px; box-shadow: 0 8px 20px rgba(255, 107, 157, 0.15); border: 2px solid rgba(255, 107, 157, 0.2);' class='card'>
        <h2 style='color:#FF6B9D; margin-bottom: 10px;'>📤 Upload Audio</h2>
        <p style='color:#888; font-size: 14px; margin-bottom: 15px;'>🎵 Upload 5-10 seconds of baby's sound (WAV or MP3)</p>
        <div style='background: white; padding: 15px; border-radius: 12px; border: 2px dashed #FFB3C6;'>
            <p style='text-align: center; color: #FF8A65; font-size: 12px;'>Supported: .wav, .mp3 • Max 25MB</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    audio_file = st.file_uploader("Upload your baby's audio file", type=["wav", "mp3"], label_visibility="collapsed")

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #e3f2fd 0%, #e1f5fe 100%); padding: 30px; border-radius: 20px; box-shadow: 0 8px 20px rgba(33, 150, 243, 0.15); border: 2px solid rgba(33, 150, 243, 0.2);' class='card'>
        <h2 style='color:#2196F3; margin-bottom: 10px;'>💡 How It Works</h2>
        <div style='font-size: 14px; color: #555; line-height: 1.8;'>
            <p>🎯 <b>1. Upload</b> - Submit baby's audio</p>
            <p>🔍 <b>2. Analyze</b> - AI processes features</p>
            <p>💬 <b>3. Interpret</b> - Get safe guidance</p>
            <p>❤️ <b>4. Support</b> - Soothing tips</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

if audio_file is not None:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #e3f2fd 0%, #f0f7ff 100%); padding: 25px; border-radius: 15px; box-shadow: 0 6px 16px rgba(33, 150, 243, 0.1); border: 2px solid rgba(33, 150, 243, 0.15);' class='card'>
        <h3 style='color:#0277BD; margin-bottom: 15px;'>🎧 Uploaded Audio Preview</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.audio(audio_file, format=f"audio/{audio_file.type.split('/')[-1]}")

    temp_path = f"temp_audio.{audio_file.type.split('/')[-1]}"
    with open(temp_path, "wb") as f:
        f.write(audio_file.getbuffer())

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🔍 Analyze Baby Sound", use_container_width=True):
            with st.spinner("🤖 CrewAI is analyzing your baby's sound..."):
                output = process_baby_sound(temp_path)
                output_text = str(output)

            st.markdown("""
            <div style='background: linear-gradient(135deg, #fff0f4 0%, #ffe6f0 100%); padding: 30px; border-radius: 15px; box-shadow: 0 8px 20px rgba(216, 27, 96, 0.15); border: 2px solid rgba(216, 27, 96, 0.2); margin-top: 30px;' class='card'>
                <h3 style='color:#D81B60; margin-bottom: 20px; font-size: 24px;'>✨ Baby Sound Analysis Results</h3>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #fafafa 0%, #ffffff 100%); padding: 25px; border-radius: 12px; border-left: 5px solid #FF6F91; font-size: 15px; line-height: 1.8; color: #333; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-top: 15px;'>
                {output_text.replace(chr(10), "<br>")}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, #FFF3E0 0%, #FFFBF0 100%); padding: 20px; border-radius: 12px; border-left: 5px solid #FF9800; margin-top: 25px;'>
                <p style='color: #FF9800; font-weight: bold; margin-bottom: 8px;'>💝 Remember:</p>
                <p style='color: #666; font-size: 14px; line-height: 1.6;'>
                    This is not a medical diagnosis. Always consult healthcare professionals for medical concerns. 
                    This tool helps caregivers understand common baby cues better.
                </p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 30px 20px; color: #999; font-size: 12px; border-top: 1px solid rgba(0,0,0,0.1); margin-top: 40px;'>
    <p>👶 Made with ❤️ for caregivers • AI Baby Sound Helper v1.0</p>
    <p style='margin-top: 8px;'>Safe • Non-Medical • Supportive • Intelligent</p>
</div>
""", unsafe_allow_html=True)
