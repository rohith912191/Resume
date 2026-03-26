"""
Custom resume parser that works independently without complex ML dependencies
"""
import re
import io
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter

# Common skills list
COMMON_SKILLS = [
    'Python', 'Java', 'C++', 'JavaScript', 'TypeScript', 'C#', 'PHP', 'Ruby', 'Go', 'Rust',
    'SQL', 'NoSQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Elasticsearch',
    'React', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask', 'Spring', 'ASP.NET',
    'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'Git', 'Linux', 'Windows',
    'HTML', 'CSS', 'SASS', 'Bootstrap', 'Material Design',
    'API', 'REST', 'GraphQL', 'SOAP', 'JSON', 'XML',
    'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn',
    'Data Science', 'Analytics', 'Tableau', 'Power BI', 'Excel',
    'Agile', 'Scrum', 'JIRA', 'Confluence',
]

# Common degrees
DEGREES = ['B.Tech', 'B.E.', 'B.Sc', 'M.Tech', 'M.E.', 'M.Sc', 'MBA', 'BCA', 'MCA', 'PhD', 'Bachelor', 'Master']

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_num = 0
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True):
                interpreter = PDFPageInterpreter(resource_manager, converter)
                interpreter.process_page(page)
                page_num += 1
        text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        return text, page_num
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return "", 0

def extract_name(text):
    """Extract name from resume"""
    lines = text.split('\n')
    # Usually the name is in the first non-empty line or near the top
    for line in lines[:10]:
        line = line.strip()
        if len(line) > 2 and len(line.split()) <= 4:
            # Filter out common non-name lines
            if not any(x in line.lower() for x in ['email', 'phone', 'address', 'linkedin', 'http', '@']):
                return line
    return "Unknown"

def extract_email(text):
    """Extract email address from text"""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else "N/A"

def extract_phone(text):
    """Extract phone number from text"""
    phone_patterns = [
        r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        r'\+91[- ]?\d{4}[- ]?\d{3}[- ]?\d{3}',
    ]
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        if matches:
            return matches[0]
    return "N/A"

def extract_skills(text):
    """Extract skills from resume"""
    skills_found = []
    text_lower = text.lower()
    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            skills_found.append(skill)
    return list(set(skills_found))

def extract_degree(text):
    """Extract degree information"""
    for degree in DEGREES:
        if degree.lower() in text.lower():
            return degree
    return "N/A"

class CustomResumeParser:
    """Simple regex-based resume parser"""
    
    def __init__(self, resume_path):
        self.resume_path = resume_path
        self.text, self.pages = extract_text_from_pdf(resume_path)
    
    def get_extracted_data(self):
        """Return extracted resume data"""
        return {
            'name': extract_name(self.text),
            'email': extract_email(self.text),
            'mobile_number': extract_phone(self.text),
            'skills': extract_skills(self.text),
            'degree': extract_degree(self.text),
            'no_of_pages': self.pages,
        }
