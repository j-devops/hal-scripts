# hal-scripts
### "I'm sorry Dave, I'm afraid I can't do that."  
Some openapi test scripts


## Getting Started

#### API stuff

1. Open account at openai - https://platform.openai.com/account/
2. Create a API key - https://platform.openai.com/account/api-keys
3. Load key into .env and setup gitignore
```
(base) jason@jlan-basement:~/hal-scripts$ cat .env
API_KEY = "sk-mysupersecretkey"
(base) jason@jlan-basement:~/hal-scripts$

(base) jason@jlan-basement:~/hal-scripts$ cat .gitignore
# Ignore Mac system files
.DS_store

# Ignore node_modules folder
node_modules

# Ignore files related to API keys
.env

# Ignore SASS config files
.sass-cache
(base) jason@jlan-basement:~/hal-scripts$
```

##### Run some pip installs or leverage the requirement.txt
```
pip install -r requirements.txt
```
##### Test
```
(base) jason@jlan-basement:~/hal-scripts$ python hal_sysinfo.py
```

## Inventory Database

A simple HTML page, `inventory.html`, provides a local inventory tracker using your browser's local storage. Open the file in a web browser and add items to build a small inventory table. Items can be removed with the **Delete** button.
