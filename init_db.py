"""
Database initialization script for PlanetScale
Run this once to create all required tables
"""
import pymysql
import os
from urllib.parse import urlparse

# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL', None)
if not DATABASE_URL:
    DATABASE_URL = "mysql://root:Rohith%4091@127.0.0.1/CV"
    print("DATABASE_URL not set. Using local fallback:", DATABASE_URL)

try:
    # Parse the URL
    from urllib.parse import unquote
    url = urlparse(DATABASE_URL)
    username = unquote(url.username) if url.username else None
    password = unquote(url.password) if url.password else None
    
    # Connect to database
    connect_args = {
        'host': url.hostname,
        'user': username,
        'password': password,
        'database': url.path.lstrip('/')
    }
    if url.hostname not in ('127.0.0.1', 'localhost'):
        connect_args['ssl_verify_cert'] = True
        connect_args['ssl_verify_identity'] = True

    connection = pymysql.connect(**connect_args)
    cursor = connection.cursor()
    
    # Create user_data table
    print("Creating user_data table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            ID INT NOT NULL AUTO_INCREMENT,
            sec_token varchar(20) NOT NULL,
            ip_add varchar(50) NULL,
            host_name varchar(50) NULL,
            dev_user varchar(50) NULL,
            os_name_ver varchar(50) NULL,
            latlong varchar(50) NULL,
            city varchar(50) NULL,
            state varchar(50) NULL,
            country varchar(50) NULL,
            act_name varchar(50) NOT NULL,
            act_mail varchar(50) NOT NULL,
            act_mob varchar(20) NOT NULL,
            Name varchar(500) NOT NULL,
            Email_ID VARCHAR(500) NOT NULL,
            resume_score VARCHAR(8) NOT NULL,
            Timestamp VARCHAR(50) NOT NULL,
            Page_no VARCHAR(5) NOT NULL,
            Predicted_Field LONGTEXT NOT NULL,
            User_level LONGTEXT NOT NULL,
            Actual_skills LONGTEXT NOT NULL,
            Recommended_skills LONGTEXT NOT NULL,
            Recommended_courses LONGTEXT NOT NULL,
            pdf_name varchar(50) NOT NULL,
            PRIMARY KEY (ID)
        ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """)
    connection.commit()
    print("✓ user_data table created")
    
    # Create user_feedback table
    print("Creating user_feedback table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_feedback (
            ID INT NOT NULL AUTO_INCREMENT,
            feed_name varchar(50) NOT NULL,
            feed_email VARCHAR(50) NOT NULL,
            feed_score VARCHAR(5) NOT NULL,
            comments VARCHAR(500) NULL,
            Timestamp VARCHAR(50) NOT NULL,
            PRIMARY KEY (ID)
        ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """)
    connection.commit()
    print("✓ user_feedback table created")
    
    cursor.close()
    connection.close()
    print("\n✅ Database initialization complete!")
    print("Your app is ready to use with the database.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure:")
    print("1. DATABASE_URL environment variable is set correctly")
    print("2. Connection string format: mysql://user:password@host/database")
    print("3. PlanetScale database exists and is accessible")
