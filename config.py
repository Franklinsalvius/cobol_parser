# ========== CONFIGURATION ==========



input_csv_file = 'cobol_programs.csv' #replace with the input csv
copybook_folder = 'copybooks'
sample_xml_folder = 'XMLS'
output_csv = 'output_payload.csv'
enable_sample_xml_filtering = False
enable_database_insert = True

db_type = 'mysql'  
db_config = {
    'sqlite': {'url': 'sqlite:///C:/Users/mydb.db'},
    'postgresql': {'url': 'postgresql://user:password@localhost:5432/dbname'},
    'mysql': {'url': 'mysql+pymysql://user:password@localhost/mydb'},
}
