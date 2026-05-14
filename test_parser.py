from App.custom_resume_parser import CustomResumeParser
import os

# Test with a sample resume
resume_path = 'App/Uploaded_Resumes/Analyzer Test Resume .pdf'
if os.path.exists(resume_path):
    try:
        parser = CustomResumeParser(resume_path)
        data = parser.get_extracted_data()
        print("Resume parsing successful!")
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Email: {data.get('email', 'N/A')}")
        print(f"Skills: {data.get('skills', [])}")
        print(f"No of pages: {data.get('no_of_pages', 0)}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Resume file not found")