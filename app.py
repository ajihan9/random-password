import streamlit as st
import random
import string

st.title("🔐 랜덤 비밀번호 & PIN 생성기")

st.write("영어 알파벳 + 숫자로만 구성된 랜덤 비밀번호와, 중복 없는 PIN 번호를 생성합니다.")

# ------------------------
# 비밀번호 생성 함수
# ------------------------
def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    all_chars = letters + digits

    password = [
        random.choice(letters),
        random.choice(digits)
    ]

    password += [random.choice(all_chars) for _ in range(length - 2)]
    random.shuffle(password)

    return ''.join(password)

# ------------------------
# PIN 생성 함수
# ------------------------
def generate_unique_pin(length=4):
    digits = list("0123456789")

    if length > 10:
        return "❌ PIN 길이는 10 이하만 가능합니다."

    random.shuffle(digits)
    return ''.join(digits[:length])

# ------------------------
# UI
# ------------------------

st.header("🔑 랜덤 비밀번호 생성")
pw_length = st.slider("비밀번호 길이 선택", 4, 32, 12)

if st.button("비밀번호 생성하기"):
    password = generate_password(pw_length)
    st.success(f"생성된 비밀번호: **{password}**")


st.header("🔢 중복 없는 PIN 생성")
pin_length = st.slider("PIN 길이 선택", 1, 10, 4)

if st.button("PIN 생성하기"):
    pin = generate_unique_pin(pin_length)
    st.success(f"생성된 PIN 번호: **{pin}**")
