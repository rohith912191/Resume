import sys
import os

# Get the directory of this file
script_dir = os.path.dirname(os.path.abspath(__file__))
app_file = os.path.join(script_dir, 'App', 'App.py')

# Execute the App.py file
exec(open(app_file).read())
