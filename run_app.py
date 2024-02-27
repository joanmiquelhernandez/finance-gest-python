import os
import sys
import ssl

current_dir = os.getcwd()
sys.path.insert(0, current_dir)

activate_this = f'{current_dir}/venv/Scripts/activate_this.py'  # Windows
# activate_this = f'{current_dir}/venv/bin/activate_this.py'    # LINUX
with open(activate_this) as file_:
    
    exec(file_.read(), dict(__file__=activate_this))


from app import app
