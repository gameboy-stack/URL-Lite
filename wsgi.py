from app import app
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env_sample')
load_dotenv(dotenv_path)
  
if __name__ == "__main__":
        app.run(debug=True,port=os.environ.get("port"))