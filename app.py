import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Code Generator", page_icon="")
st.title("Free AI Code Generator")
st.write("Describe what you want to build and code immediately")


api_key = st.text_input("Enter your Groq API Key:", type="password")
language = st.selectbox("Programming Language:", ["Python", "JavaScript", "HTML/CSS", "SQL", "Other"])
user_request = st.text_area("What should the code do?", placeholder="e.g. A function that sorts a list of names alphabetically")


if st.button("Generate Code"):
    if not api_key:
        st.warning("Please enter your API key above")
    elif not user_request:
        st.warning("Please describe waht yiu want your code to do.")
    else:
        with st.spinner("Generating your code"):
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"You are an expert {language} developer. Write clean, commented, beginner-friendly code. Always explain what the code does after the code block."},
                    {"role": "user", "content": user_request}
                ]
            )
            result = response.choices[0].message.content
            st.success("Here's your code!")
            st.markdown(result)
            
