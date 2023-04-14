# Serve&Save

For MCTC/USBANK Hackathon 2023, we built an innovative app that motivates students to engage in community service by providing them with incentives. Our app rewards students for their volunteering time by adding interest to their flexible savings account, resulting in a higher percentage yield. Join the movement of student volunteers and make a positive impact on your community while growing your savings!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. You can either fork this repoistory and then clone it from your computer or you can download the zip file.

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Requests-oauthlib](https://pypi.org/project/requests-oauthlib/)

### Setup

Once you clone the repo, you will want to install all the modules so that the repo should function properly.

1. Create a [US BANK API Key and Secret](https://developer.usbank.com/).

2. Create an`.env` with your API Key and Secret.
3. To start, open up a terminal or a command prompt and navigate to the directory of your Python project. Once you are there, type the following command: `pip install -r requirements.txt`

To utilize API Key and Secret, you will need to create a .env file in your main directory. You will not be able to upload it to this repo as most .gitignore will ignore the file. This is for security reasons as you do not want to post your API Keys to these services out in the open. When you are done creating the .env file, insert your respective keys into the text below and then save the .env file.

```
export US_BANKING_API_KEY="INSERT US_BANKING_API_KEY KEY HERE"
export US_BANKING_SECRET_KEY="INSERT US_BANKING_SECRET_KEY KEY HERE"

```

## Creating virtual environments

In terminal/command prompt, root directoty of the project.

Set up virtual environment, Mac

```
virtualenv -p python3 venv
source venv/bin/activate
```

Set up virtual environment, PC (assuming lab PC with only Python 3 installed)

```
virtualenv venv
venv/bin/activate
```

## Usage

To run the application, enter the following in the terminal:

```
flask run
```

App will be running on http://127.0.0.1:5000

## Future Intemplemation

- [Figma Wireframe](https://www.figma.com/proto/XeDgl79XSWcydnKrCxImkN/Serve-and-Save?node-id=11-190&scaling=scale-down&page-id=0%3A1&starting-point-node-id=11%3A190)

## Authors

- James Nguyen
- Niman Ahmed
- Sophanda Long
- Thurman Thoma
