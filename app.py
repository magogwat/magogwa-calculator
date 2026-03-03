import streamlit as st
# Kichwa cha Habari kwenye Browser
st.title("🧮 MAGOGWA CALCULATOR")
st.write("Hii ni programu ya Python inayofanya kazi kwenye Browser!")

# Sehemu ya kuingiza namba (Input boxes)
namba1 = st.number_input("Ingiza namba ya kwanza:", value=0)
namba2 = st.number_input("Ingiza namba ya pili:", value=0)

# Chagua operesheni unayotaka
chaguo = st.selectbox("Unataka kufanya nini?", ["Jumlisha (+)", "Toa (-)", "Zidisha (*)", "Gawanya (/)"])

# Mantiki ya kukokotoa
if st.button("Pata Jibu"):
    if chaguo == "Jumlisha (+)":
        jibu = namba1 + namba2
    elif chaguo == "Toa (-)":
        jibu = namba1 - namba2
    elif chaguo == "Zidisha (*)":
        jibu = namba1 * namba2
    elif chaguo == "Gawanya (/)":
        if namba2 != 0:
            jibu = namba1 / namba2
        else:
            jibu = "Haiwezekani kugawa kwa sifuri!"

    # Onyesha jibu kwa rangi ya kijani
    st.success(f"Matokeo yako ni: {jibu}")