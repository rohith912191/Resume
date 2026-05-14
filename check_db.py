import sqlite3
conn = sqlite3.connect('App/resume_analyzer.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM user_data")
user_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM user_feedback")
feedback_count = cursor.fetchone()[0]
print(f'user_data records: {user_count}')
print(f'user_feedback records: {feedback_count}')
conn.close()