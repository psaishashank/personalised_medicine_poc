# Creates DB and tables if not exists and writes data
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('drug.db')
    print("Connected to DB successfully")
    return conn

def create_tables(cur):
    
    #Create Drugs data table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS drugs_data(
            id integer PRIMARY KEY , 
            drug_name text NOT NULL, 
            active_ingredients text 

        )''')

    #Create Drugs data table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS drug_market_data(
            id integer PRIMARY KEY , 
            drug_id integer NOT NULL,
            strength text , 
            dosage_form text, 
            marketing_status text

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
            recommendation TEXT NOT NULL
        )''')
    
    print("Tables created successfully")

def insert_data_tables(cur,con):

    drug_data = [
                (1,'CELEXA','CITALOPRAM HYDROBROMIDE'),
                (2,'ORILISSA','ELAGOLIX SODIUM'),
                (3,'amitriptyline',None),
                (4,'voriconazole','VORICONAZOLE')
            ]
    
    drug_market_data = [
            (1,1,'EQ 10MG BASE','TABLET;ORAL','Prescription'),
            (2,1,'EQ 60MG BASE','TABLET;ORAL','Discontinued'),
            (3,2,'EQ 150MG BASE','TABLET;ORAL','Prescription'),
            (4,2,'EQ 200MG BASE','TABLET;ORAL','Prescription'),
            (5,4,'50MG','TABLET;ORAL','Prescription'),
            (6,4,'200MG','TABLET;ORAL','Prescription'),
            ]

    gene_data = [
                (1,'CYP2C19','*2/*2','CYP2C19 Poor Metabolizer (*2/*2)'),
                (2,'CYP2C19','*1/*1','Normal Function'),
                (3,'CYP2C19','*1/*17','Increased Function'),
                (4,'SLCO1B1','*1A/*1A','Normal Function'),
                (5,'SLCO1B1','*5/*5','Low function')
            ]

    drug_gene_data = [
                    (1,1,1,'FDA','Per the FDA warning, citalopram 20 mg/day is the maximum recommended dose in CYP2C19 poor metabolizers due to the risk of QT prolongation. FDA product labeling additionally cautions that citalopram dose should be limited to 20 mg/day in patients with hepatic impairment, those taking a CYP2C19 inhibitor, and patients greater than 60 years of age.'),
                    (2,1,1,'CPIC','Consider a clinically appropriate antidepressant not predominantly metabolized by CYP2C19. If citalopram or escitalopram are clinically appropriate, consider a lower starting dose, slower titration schedule and 50% reduction of the standard maintenance dose as compared to normal metabolizers.'),
                    (3,3,1,'CPIC','Avoid tertiary amine use due to potential for sub-optimal response. Consider alternative drug not metabolized by CYP2C19. TCAs without major CYP2C19 metabolism include the secondary amines nortriptyline and desipramine. For tertiary amines, consider a 50% reduction of the recommended starting dose. Utilize therapeutic drug monitoring to guide dose adjustments. Titrate dose to observed clinical response with symptom improvement and minimal  side effects.'),
                    (4,4,1,'CPIC','Choose an alternative agent that is not dependent on CYP2C19 metabolism as primary therapy in lieu of voriconazole. Such agents include isavuconazole, liposomal amphotericin B, and posaconazole. In the event that voriconazole is considered to be the most appropriate agent, based on clinical advice, for a patient with poor metabolizer genotype, voriconazole should be administered at a preferably lower than standard dosage with careful therapeutic drug monitoring.')




            ]

    cur.executemany("INSERT INTO drugs_data VALUES(?, ?, ?)", drug_data)
    con.commit()

    cur.executemany("INSERT INTO drug_market_data VALUES(?, ?, ?, ?, ?)", drug_market_data)
    con.commit()

    cur.executemany("INSERT INTO gene_data VALUES(?, ?, ?, ?)", gene_data)
    con.commit()

    cur.executemany("INSERT INTO drug_gene_guidance VALUES(?, ?, ?, ?, ?)", drug_gene_data)
    con.commit()

    print("Data Inserted into DB successfully")

def main():

    con = get_db_connection() # Coreate db if not exists or connect to existing db

    cur = con.cursor()

    create_tables(cur)

    insert_data_tables(cur,con)

    print("*** Program Exited Successfully ****")


if __name__ == "__main__":
   main()