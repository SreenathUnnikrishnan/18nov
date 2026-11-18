import streamlit as st
f = open("Exercise1.txt","r+")

st.title("👋 Hello, Streamlit!")

st.write("Click a button below:")

#if st.button("Say Hello"):
# st.success(f.write("hello"))
a=st.text_input("Enter your name")
f.write(a)

if st.button("Say Goodbye"):
    f.seek(0)
    st.warning(f.read())
