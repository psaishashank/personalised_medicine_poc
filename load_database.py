# Creates DB and tables if not exists and writes data
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('drug.db')
    return conn

def create_tables(cur):
    
    #Create Drugs data table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS drugs_data(
            id integer PRIMARY KEY , 
            drug_name text NOT NULL, 
            active_ingredients integer, 

        )''')

    # Create Genome data table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS gene_data(
            id integer PRIMARY KEY, 
            gene text NOT NULL, 
            alleles text, 
            description text    
        )''')

    # Create Prescription data table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS drug_gene_guidance(
            id integer PRIMARY KEY AUTOINCREMENT,
            drug_id integer NOT NULL,
            gene_id integer NOT NULL,
            source text NOT NULL,
            recommendation TEXT NOT NULL,
        )''')
    

def insert_data_tables(cur):

    drug_data = [
                (1,'CELEXA','CITALOPRAM HYDROBROMIDE','Prescription'),
                (),
                (),
                ()
            ]

    gene_data = [
                (),
                (),
                (),
                (),
                (),
                ()
    ]

    drug_gene_data = [
                    (),
                    (),
                    (),
                    (),
                    (),

    ]



def main():

    get_db_connection() # Coreate db if not exists or connect to existing db

    cur = con.cursor()

    create_tables(cur)

    insert_data_tables(cur)

    test_data(curr)

    print("*** Program Exited Successfully ****")


if __name__ == "__main__":
   main()