import sqlite3
import streamlit as st
import pandas as pd

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('drug.db')
    return conn

# Create a function to query data based on user inputs
def search_recommendations(user_genome, user_source):
    conn = get_db_connection()
    query = f"""
        SELECT  DD.drug_name, DD.active_ingredients, D.source, D.recommendation
        FROM drug_gene_guidance D
        INNER JOIN gene_data gd  ON D.gene_id = gd.id
        INNER JOIN drugs_data DD ON DD.id = D.drug_id
        WHERE gd.gene = ? AND gd.alleles = ? AND (D.source = ? OR ? = 'all');

    """
    df = pd.read_sql(query, conn, params=(user_genome.split(" : ")[0],user_genome.split(" : ")[1],user_source,user_source))
    conn.close()
    return df

# Streamlit UI
def main():
    # Set page configuration and background
    st.set_page_config(page_title="Drug-Genome Search", layout="centered")
    st.markdown(
    """
    <style>
    .main {
        background-color: #D86C70;
    }
    h1 {
        color: #800000;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #800000;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #a52a2a;
    }
    .css-1d391kg p {
        color: #333;
        font-family: 'Arial', sans-serif;
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
        conn = get_db_connection()
        # drugs = pd.read_sql("SELECT drug_name FROM drugs_data", conn)['drug_name'].tolist()
        genomes = pd.read_sql("SELECT gene || ' : ' || alleles as gene FROM gene_data", conn)['gene'].tolist()
        sources = pd.read_sql("SELECT DISTINCT source FROM drug_gene_guidance", conn)['source'].tolist()
        sources.append("all")
        conn.close()
        

        selected_genome = st.selectbox("Select Genome", genomes)
        selected_source = st.selectbox("Select Source, select all to include all sources", sources)
        
        # Search button
        search = st.form_submit_button(label='Search')
    
    # Display search results
    if search:
        # Query the database
        results_df = search_recommendations(selected_genome, selected_source)
        
        # Hide form elements and show results
        st.empty() 
        st.dataframe(results_df, use_container_width=True)
        
        # Back button to reset view
        if st.button('Back to Search'):
            st.experimental_rerun()  # Reload the page

if __name__ == "__main__":
    main()
