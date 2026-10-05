import streamlit as st
import time
import random

st.set_page_config(
    page_title="BRAIN SPARK",
    page_icon="🧠",
    layout="centered"
)

riddles = [
    {"question": "I have keys but cannot open locks. What am I?", "options": ["Keyboard", "Door", "Map"], "answer": "Keyboard", "explanation": "A keyboard has keys used for typing."},
    {"question": "What has hands but cannot clap?", "options": ["Clock", "Robot", "Tree"], "answer": "Clock", "explanation": "A clock has hands that show the time."},
    {"question": "What gets wetter as it dries?", "options": ["Towel", "Paper", "Book"], "answer": "Towel", "explanation": "A towel gets wet while drying something."},
    {"question": "What has many teeth but cannot bite?", "options": ["Comb", "Dog", "Tiger"], "answer": "Comb", "explanation": "A comb has many teeth used for arranging hair."},
    {"question": "What has one eye but cannot see?", "options": ["Needle", "Camera", "Cat"], "answer": "Needle", "explanation": "The hole in a needle is called its eye."},
    {"question": "What can travel around the world while staying in one corner?", "options": ["Stamp", "Airplane", "Sun"], "answer": "Stamp", "explanation": "A stamp stays in one corner of an envelope while the envelope travels."},
    {"question": "What has a neck but no head?", "options": ["Bottle", "Shirt", "Guitar"], "answer": "Bottle", "explanation": "A bottle has a neck but no head."},
    {"question": "What has words but never speaks?", "options": ["Book", "Radio", "Person"], "answer": "Book", "explanation": "A book contains words but cannot speak."},
    {"question": "What has legs but cannot walk?", "options": ["Table", "Dog", "Horse"], "answer": "Table", "explanation": "A table has legs but cannot walk."},
    {"question": "What goes up but never comes down?", "options": ["Age", "Rain", "Ball"], "answer": "Age", "explanation": "Age increases as time passes."},
    {"question": "What has a thumb and four fingers but is not alive?", "options": ["Glove", "Hand", "Tree"], "answer": "Glove", "explanation": "A glove has spaces for a thumb and four fingers."},
    {"question": "What has a head and a tail but no body?", "options": ["Coin", "Snake", "Fish"], "answer": "Coin", "explanation": "A coin has a head side and a tail side."},
    {"question": "What has a ring but no finger?", "options": ["Telephone", "Hand", "Tree"], "answer": "Telephone", "explanation": "A telephone can ring but has no finger."},
    {"question": "What is full of holes but can still hold water?", "options": ["Sponge", "Basket", "Net"], "answer": "Sponge", "explanation": "A sponge has many tiny holes and can absorb water."},
    {"question": "What has four wheels and flies?", "options": ["Garbage truck", "Car", "Bicycle"], "answer": "Garbage truck", "explanation": "A garbage truck has wheels and can attract flies."},
    {"question": "What begins with T, ends with T, and has T in it?", "options": ["Teapot", "Tent", "Toast"], "answer": "Teapot", "explanation": "A teapot begins and ends with T and contains tea."},
    {"question": "What can you catch but cannot throw?", "options": ["Cold", "Ball", "Stone"], "answer": "Cold", "explanation": "You can catch a cold."},
    {"question": "What has cities but no houses, forests but no trees, and rivers but no water?", "options": ["Map", "Book", "Globe"], "answer": "Map", "explanation": "A map shows cities, forests and rivers."},
    {"question": "What has a bark but no bite?", "options": ["Tree", "Dog", "Wolf"], "answer": "Tree", "explanation": "A tree has bark but cannot bite."},
    {"question": "What comes down but never goes up?", "options": ["Rain", "Smoke", "Age"], "answer": "Rain", "explanation": "Rain falls down from clouds."},
    {"question": "What is always in front of you but can never be seen?", "options": ["Future", "Past", "Shadow"], "answer": "Future", "explanation": "The future is ahead of us but cannot be seen."},
    {"question": "What has many branches but no leaves?", "options": ["Bank", "Tree", "Plant"], "answer": "Bank", "explanation": "A bank can have many branches."},
    {"question": "What has an end but no beginning?", "options": ["Stick", "Circle", "Line"], "answer": "Stick", "explanation": "A stick has an end."},
    {"question": "What belongs to you but other people use it more than you do?", "options": ["Your name", "Your shoes", "Your phone"], "answer": "Your name", "explanation": "Other people usually say your name more often than you do."},
    {"question": "What has a face but no eyes?", "options": ["Clock", "Person", "Cat"], "answer": "Clock", "explanation": "A clock has a face but no eyes."}
]

TOTAL_QUESTIONS = 25
TOTAL_TIME = 10 * 60
celebration_words = ["EXCELLENT!", "MARVELOUS!", "FANTASTIC!", "AMAZING!", "GREAT!"]

for key, value in {
    "started": False,
    "current": 0,
    "score": 0,
    "answered": False,
    "selected": None,
    "option_order": [],
    "game_start_time": None,
    "correct_streak": 0,
    "celebration_word": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800;900&display=swap');

.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(70,100,230,.50), transparent 35%),
        radial-gradient(circle at 0% 100%, rgba(0,190,255,.28), transparent 35%),
        radial-gradient(circle at 100% 100%, rgba(200,30,255,.28), transparent 35%),
        linear-gradient(135deg, #07113d 0%, #101b58 50%, #260744 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.brain-title {
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 64px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 5px;
    color: #ffffff !important;
    text-shadow: 0 0 8px #00eaff, 0 0 18px #00eaff, 0 0 35px #8b5cf6, 0 0 50px #ff2bd6;
    margin: 10px 0 15px;
}

.brain-subtitle {
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 22px;
    font-weight: 700;
    text-align: center;
    color: #ffffff !important;
    text-shadow: 0 0 8px #ffffff;
    margin-bottom: 20px;
}

.brain-tagline {
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 18px;
    font-weight: 800;
    text-align: center;
    letter-spacing: 4px;
    color: #00efff !important;
    text-shadow: 0 0 8px #00efff, 0 0 18px #00efff;
    margin-bottom: 30px;
}

[data-testid="metric-container"] {
    background: rgba(15,35,90,.98) !important;
    border: 2px solid rgba(0,235,255,.65) !important;
    border-radius: 18px !important;
    padding: 20px !important;
    box-shadow: 0 0 20px rgba(0,220,255,.20);
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] *,
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {
    color: #ffffff !important;
}

[data-testid="stMetricLabel"] {
    font-family: 'Orbitron', Arial, sans-serif !important;
    font-size: 15px !important;
    font-weight: 800 !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Orbitron', Arial, sans-serif !important;
    font-size: 36px !important;
    font-weight: 900 !important;
    text-shadow: 0 0 8px #00eaff, 0 0 18px #00eaff;
}

.ready-card {
    background: linear-gradient(145deg, #142d70, #320c5a);
    border: 2px solid #9966ff;
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 0 25px rgba(130,80,255,.35);
    margin: 15px 0 25px;
}

.ready-title {
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 27px;
    font-weight: 900;
    color: #ffffff !important;
    text-shadow: 0 0 8px #ff4fd8, 0 0 18px #ff4fd8;
    margin-bottom: 12px;
}

.ready-text {
    font-family: Arial, sans-serif;
    font-size: 19px;
    font-weight: 600;
    color: #ffffff !important;
}

.stButton > button {
    min-height: 72px !important;
    border-radius: 16px !important;
    border: 2px solid #00efff !important;
    background: linear-gradient(90deg, #7c3aed, #2563eb, #06b6d4) !important;
    color: #ffffff !important;
    font-family: 'Orbitron', Arial, sans-serif !important;
    font-size: 23px !important;
    font-weight: 900 !important;
    letter-spacing: 1.5px;
    box-shadow: 0 0 20px rgba(0,220,255,.45) !important;
}

.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: #ffffff !important;
}

.exit-button > button {
    background: linear-gradient(90deg, #b91c1c, #dc2626) !important;
    border-color: #ff8a8a !important;
    font-size: 21px !important;
    min-height: 60px !important;
    box-shadow: 0 0 18px rgba(255,70,70,.35) !important;
}

[data-testid="stRadio"] label,
[data-testid="stRadio"] label * {
    color: #ffffff !important;
    font-family: Arial, sans-serif !important;
    font-size: 20px !important;
    font-weight: 700 !important;
}

[data-testid="stRadio"] > label,
[data-testid="stRadio"] > label * {
    color: #00efff !important;
    font-family: 'Orbitron', Arial, sans-serif !important;
    font-size: 20px !important;
    font-weight: 900 !important;
}

.timer-box {
    text-align: center;
    padding: 18px;
    margin: 10px 0 20px;
    border-radius: 17px;
    background: #081c4b;
    border: 2px solid #00ebff;
    color: #ffffff !important;
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 28px;
    font-weight: 900;
    text-shadow: 0 0 10px #00eaff;
}

.game-stat {
    text-align: center;
    color: #ffffff !important;
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 20px;
    font-weight: 900;
    padding: 10px;
    text-shadow: 0 0 8px #00eaff;
}

.question-number {
    text-align: center;
    color: #00efff !important;
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 15px;
    text-shadow: 0 0 10px #00efff;
}

.question-box {
    font-family: 'Orbitron', Arial, sans-serif;
    font-size: 28px;
    font-weight: 800;
    line-height: 1.5;
    color: #ffffff !important;
    padding: 28px;
    border-radius: 20px;
    background: linear-gradient(145deg, #0f2864, #2d0a55);
    border: 2px solid #8b5cf6;
    box-shadow: 0 0 25px rgba(139,92,246,.25);
    margin-bottom: 25px;
}

[data-testid="stAlert"],
[data-testid="stAlert"] * {
    color: #ffffff !important;
}

hr {
    border-color: rgba(0,235,255,.35) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="brain-title">🧠 BRAIN SPARK</div>
<div class="brain-subtitle">Challenge Your Mind. Ignite Your Thinking</div>
<div class="brain-tagline">THINK • SOLVE • SCORE • WIN</div>
""", unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🧩 QUESTIONS", "25")
        st.metric("🎯 OPTIONS", "3")
    with col2:
        st.metric("⏱️ TIME", "10 MIN")
        st.metric("🔥 STREAK", "5")
    st.markdown("---")

    st.markdown("""
<div class="ready-card">
    <div class="ready-title">🧠 READY TO CHALLENGE YOUR BRAIN?</div>
    <div class="ready-text">Solve the riddles, build your streak, and test how quickly you can think!</div>
</div>
""", unsafe_allow_html=True)

    if st.button("🚀 START BRAIN SPARK", use_container_width=True):
        st.session_state.started = True
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.option_order = []
        st.session_state.game_start_time = time.time()
        st.session_state.correct_streak = 0
        st.session_state.celebration_word = None
        st.rerun()
    st.stop()

if st.session_state.current >= TOTAL_QUESTIONS:
    st.markdown('<div class="brain-title" style="font-size:48px;">🏆 GAME COMPLETE</div>', unsafe_allow_html=True)
    score = st.session_state.score
    percentage = (score / TOTAL_QUESTIONS) * 100
    st.markdown("---")

    st.markdown(f"""
<div class="ready-card">
    <div class="ready-title">🎯 FINAL SCORE</div>
    <div style="font-family:Arial,sans-serif;font-size:46px;font-weight:900;color:#ffffff;margin:15px;">
        {score} / {TOTAL_QUESTIONS}
    </div>
    <div style="font-family:Arial,sans-serif;font-size:24px;font-weight:800;color:#00efff;">
        📊 {percentage:.1f}%
    </div>
</div>
""", unsafe_allow_html=True)

    if percentage >= 80:
        st.balloons()
        st.success("🌟 EXCELLENT PERFORMANCE!")
    elif percentage >= 60:
        st.success("👏 GREAT JOB!")
    else:
        st.info("💪 GOOD TRY! KEEP PRACTICING!")

    if st.button("🔄 PLAY AGAIN", use_container_width=True):
        st.session_state.started = True
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.option_order = []
        st.session_state.game_start_time = time.time()
        st.session_state.correct_streak = 0
        st.session_state.celebration_word = None
        st.rerun()
    st.stop()

elapsed = int(time.time() - st.session_state.game_start_time)
remaining = TOTAL_TIME - elapsed

if remaining <= 0:
    st.session_state.current = TOTAL_QUESTIONS
    st.rerun()

minutes = remaining // 60
seconds = remaining % 60

st.markdown(f'<div class="timer-box">⏱️ TIME LEFT: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="game-stat">🏆 SCORE: {st.session_state.score}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="game-stat">🔥 STREAK: {st.session_state.correct_streak}</div>', unsafe_allow_html=True)

current_index = st.session_state.current
current = riddles[current_index]

st.markdown("---")
st.markdown(f'<div class="question-number">🧩 QUESTION {current_index + 1} / {TOTAL_QUESTIONS}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="question-box">{current["question"]}</div>', unsafe_allow_html=True)

if not st.session_state.option_order:
    shuffled_options = current["options"].copy()
    random.shuffle(shuffled_options)
    st.session_state.option_order = shuffled_options

if not st.session_state.answered:
    selected_option = st.radio(
        "🎯 CHOOSE YOUR ANSWER:",
        st.session_state.option_order,
        index=None,
        key=f"question_{current_index}"
    )

    st.markdown('<div class="submit-button">', unsafe_allow_html=True)
    if st.button("✅ SUBMIT ANSWER", use_container_width=True):
        if selected_option is None:
            st.warning("⚠️ PLEASE CHOOSE AN OPTION FIRST.")
        else:
            st.session_state.selected = selected_option
            st.session_state.answered = True

            if selected_option == current["answer"]:
                st.session_state.score += 1
                st.session_state.correct_streak += 1

                if st.session_state.correct_streak % 5 == 0:
                    celebration_index = ((st.session_state.correct_streak // 5) - 1) % len(celebration_words)
                    st.session_state.celebration_word = celebration_words[celebration_index]
                else:
                    st.session_state.celebration_word = None
            else:
                st.session_state.correct_streak = 0
                st.session_state.celebration_word = None

            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="exit-button">', unsafe_allow_html=True)
    if st.button("🚪 EXIT QUIZ", use_container_width=True):
        st.session_state.started = False
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.option_order = []
        st.session_state.game_start_time = None
        st.session_state.correct_streak = 0
        st.session_state.celebration_word = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.answered:
    if st.session_state.selected == current["answer"]:
        st.success("🎉 CORRECT ANSWER!")
        if st.session_state.celebration_word:
            st.success(f"🎉 {st.session_state.celebration_word} 🎉")
    else:
        st.error("❌ WRONG ANSWER!")

    st.markdown(f"""
<div style="
    background:#102b68;
    border:2px solid #00eaff;
    border-radius:15px;
    padding:18px;
    margin-top:15px;
    color:#ffffff;
    font-family:Arial,sans-serif;
    font-size:20px;
    font-weight:800;
">
    ✅ CORRECT ANSWER: {current["answer"]}
</div>
""", unsafe_allow_html=True)

    st.info(f"💡 Explanation: {current['explanation']}")

    if current_index == TOTAL_QUESTIONS - 1:
        st.success("🏆 THIS WAS THE LAST QUESTION!")
        time.sleep(2)
        st.session_state.current = TOTAL_QUESTIONS
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.option_order = []
        st.session_state.celebration_word = None
        st.rerun()

    st.markdown("""
<div style="
    text-align:center;
    color:#00efff;
    font-family:Arial,sans-serif;
    font-size:17px;
    font-weight:800;
    margin-top:18px;
">
    ➡️ NEXT QUESTION LOADING IN 2 SECONDS...
</div>
""", unsafe_allow_html=True)

    time.sleep(2)

    st.session_state.current += 1
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.option_order = []
    st.session_state.celebration_word = None
    st.rerun()

time.sleep(1)
st.rerun()
