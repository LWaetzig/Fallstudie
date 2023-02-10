# Fallstudie
GitHub repository for class Fallstudie

## Important information
- We use python 3.8.6 -> [download from here](https://www.python.org/downloads/release/python-386/)
- All used packages  -> [requirements.txt](requirements.txt)
- Project is also available -> [fideo](http://fideo.pythonanywhere.com)

## Run it on your local machine
1. Clone the repository via ssh or https -> `git clone <ssh url>`
2. Create and activate a virtual environment for this project -> ```python -m venv .ve_name-for-venv-env```
3. Install required packages listed in [requirements](requirements.txt) -> ```pip install -r requirements.txt```
4. To make sure everything is installed correctly run ```python manage.py check``` 
(The prompt should look like this: "System check identified no issues (0 silenced)")
5. Run this project by executing ```python manage.py runserver``` -> click the url or open browser and enter `http://127.0.0.1:8000`
