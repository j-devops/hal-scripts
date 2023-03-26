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
