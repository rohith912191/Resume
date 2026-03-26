import sys
import os

# Set up paths properly
script_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(script_dir, 'App')

# Add to Python path
sys.path.insert(0, app_dir)
sys.path.insert(0, script_dir)

# Change working directory to App directory for relative imports
os.chdir(app_dir)

# Now execute App.py
exec(open(os.path.join(app_dir, 'App.py')).read())
