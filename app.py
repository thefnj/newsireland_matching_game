import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config to wide mode for more space
st.set_page_config(layout="wide")

# Get the path to the HTML file
html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

# Open and read the HTML file
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Embed the HTML content in the Streamlit app
    # We set a large, fixed height to try and fit the game.
    # Scrolling=True is a fallback.
    st.title("Profile Matching Game")
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("Error: profile_match_game.html not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
