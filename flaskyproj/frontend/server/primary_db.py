import psycopg2
import json

# Configure your PostgreSQL connection parametres
db_params = {
    'host':'localhost',
    'database':'vedas_dataset_catelog',
    'user':'postgres',
    'password':'sac123',
    'port':5432
}

def connect_to_database():
    """Connect to PostgreSQL database."""
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_data(name, metadata, id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave):
    """Data added from the form."""
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO datasets (name, metadata, id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, (name, json.dumps(metadata), id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Exception as e:
        print(f"Error inserting data: {e}")
    return False
    




# def insert_data(name, metadata, id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave):
#     """Insert data into datasets."""
#     try:
#         connection = connect_to_database()
#         if connection:
#             cursor = connection.cursor()
#             query = "INSERT INTO datasets (name, metadata, id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             cursor.execute(query, (name, json.dumps(metadata), id, source_location, temporal_frequency, extension, resampling, projections, paused, compression, interleave))
#             connection.commit()
#             cursor.close()
#             connection.close()
#             return True
#     except Exception as e:
#         print(f"Error inserting data: {e}")
#     return False


def get_data():
    """Fetch all data from datasets."""
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM datasets"
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            return data
        
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None 


# def update(id,new_name,new_source_location,new_metadata):
#     """Update the values from datasets."""
#     try:
#         connection = connect_to_database()
#         if connection:
#             cursor = connection.cursor()
#             query = "UPDATE datasets SET name = %s, source_location = %s, metadata = %s WHERE id = %s"
#             cursor.execute(query,(new_name,new_source_location,json.dumps(new_metadata),id))
#             connection.commit()
#             cursor.close()
#             connection.close()
#             return True
#     except Exception as e:
#         print(f"Error updating data: {e}")
#     return False
