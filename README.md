# Simple Alexa Skill

This the the simplest handler for an Alexa Skill using Zappa and Flask that I've been able to put together.

I was having a nightmare getting [flask-ask](https://github.com/johnwheeler/flask-ask) to behave with Python3 and Zappa so came up with this to get me moving. Hopefully it's useful for someone else.

*For anyone wondering, I was getting a NoneType error whenever I importing the Ask library from flask-ask*

## Installing and Deploying

For full instructions please see [Zappa's GitHub page](https://github.com/Miserlou/Zappa). Their instructions are awesome.

For a quick example, assuming you've configured your lambda credentials: you need to setup your virtual environment, attatch yourself to it, install the required python packages and then run zappa...

```
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  zappa init
  zappa deploy dev
```

## Tutorials and Links

Here's some of the tutorials I was following to get this far:
  - [Creating an AWS Lambda Function for a Custom Skill](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function)
  
  - [Deploy Flask-Ask Skills to AWS Lambda with Zappa](https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa)
