import sqlite3
import streamlit as st
import pandas as pd

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('pharma.db')
    return conn

# Create a function to query data based on user inputs
def search_recommendations(drug, genome, source):
    data = [{"name":"sai","age":10},{"name":"maxi","age":12},{"name":"cae","age":30}]
    return pd.DataFrame(data)
    # conn = get_db_connection()
    # query = """
    # SELECT D.drug_name, G.genome_name, DR.recommendation, DR.source
    # FROM DosingRecommendations DR
    # JOIN Drugs D ON DR.drug_id = D.drug_id
    # JOIN Genomes G ON DR.genome_id = G.genome_id
    # WHERE D.drug_name = ? AND G.genome_name = ? AND DR.source = ?
    # """
    # df = pd.read_sql(query, conn, params=(drug, genome, source))
    # conn.close()
    # return df

# Streamlit UI
def main():
    # Set page configuration and background
    st.set_page_config(page_title="Drug-Genome Search", layout="centered")
    st.markdown(
        """
        <style>
        .main {
            background-color: #8F20F9;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # Title
    st.title("Drug-Genome Search")
    
    # Initialize search form
    with st.form(key='search_form'):
        # Dropdown for Drugs
        # conn = get_db_connection()
        # drugs = pd.read_sql("SELECT drug_name FROM Drugs", conn)['drug_name'].tolist()
        # genomes = pd.read_sql("SELECT genome_name FROM Genomes", conn)['genome_name'].tolist()
        # sources = pd.read_sql("SELECT DISTINCT source FROM DosingRecommendations", conn)['source'].tolist()
        drugs = ["paracetmol","citrazine","allegra"]
        genomes = ["AABJF","AS2*/3","BBCC"]
        sources = ["FDA","DHA"]
        # conn.close()
        
        selected_drug = st.selectbox("Select Drug", drugs)
        selected_genome = st.selectbox("Select Genome", genomes)
        selected_source = st.selectbox("Select Source", sources)
        
        # Search button
        search = st.form_submit_button(label='Search')
    
    # Display search results
    if search:
        # Query the database
        results_df = search_recommendations(selected_drug, selected_genome, selected_source)
        
        # Hide form elements and show results
        st.empty()  # Clears the form
        st.dataframe(results_df)  # Display the results in a dataframe
        
        # Back button to reset view
        if st.button('Back to Search'):
            st.experimental_rerun()  # Reload the page

if __name__ == "__main__":
    main()
