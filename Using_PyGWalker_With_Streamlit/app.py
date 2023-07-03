import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd 
import pygwalker as pyg 

# Page Configuration
st.set_page_config(page_title="StWalker App",layout="wide")

# Load Data Fxn
def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit PyGWalker App")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        # Form
        with st.form("upload_form"):
            data_file = st.file_uploader("Upload a CSV File",type=["csv","txt"])
            submitted = st.form_submit_button("Submit")

        if submitted:
            df = load_data(data_file)
            st.dataframe(df)
            # Visualize
            pyg_html = pyg.walk(df,return_html=True)
            # Render with components
            stc.html(pyg_html,scrolling=True,height=1000)

        
        
    
    else:
        st.subheader("About")

    
if __name__ == "__main__":
    main()