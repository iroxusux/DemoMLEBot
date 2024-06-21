@echo on

call .\.venv\Scripts\activate.bat

python -m pip install --upgrade PyDiscoBot
python -m pip install --upgrade MLEBot
python myBot.py

PAUSE