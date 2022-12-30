# security_project

Cyber Security Base 2022 Project 1, created to demonstrate different security issues.
This project is a simple program for saving references. It includes the following security flaws:

**1. Sql-injection**
- Sql queries vunlerable to injection

**2. Broken access control**
- Bybassing access control by modifying the url

**3. Identification and authentication failures**
- Uses plain text when storing passwords

**4. Security misconfiguration**
- Default accounts and passwords are enabled

**5. Vulnerable and outdated components** 
- Uses an old version of django

## Installation for linux

1. Download the project file from here:
[Security_project v 1.0](https://github.com/ellaverak/security_project/releases/tag/security_project)
2. Navigate to the root of the project file
4. Install virtual environment:
```bash
python3 -m venv venv
```
5. Activate virtual environment:
```bash
source venv/bin/activate
```
6. Install requirements:
```bash
pip install -r requirements.txt
```
7. Make django migrations:
```bash
invoke migrate
```
## Running

1. Activate virtual environment:
```bash
source venv/bin/activate
```
2. Run:
```bash
invoke start
```
3. Stop running:
CONTROL-C

4. Deactivate virtual enviroment:
```bash
deactivate
```

