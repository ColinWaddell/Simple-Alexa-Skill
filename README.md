# Simple Alexa Skill

This the the simplest handler for an Alexa Skill using zappa that I've been able to put together.

I was having a nightmare getting flask-ask to behave with Python3 and Zappa so came up with this to get me moving. Hopefully it's useful for someone else.

## Installing and Deploying

For full instructions please see the Zappa github page. Their instructions are awesome.

For a quick example, assuming you've configured your lambda credentials: you need to setup your virtual environment, attatch yourself to it, install the required python packages and then run zappa...

```
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  zappa init
  zappa deploy dev
```
