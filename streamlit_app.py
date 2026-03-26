import sys
import os

# Add the App directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'App'))

# Run the main app
from App.App import run

if __name__ == '__main__':
    run()
