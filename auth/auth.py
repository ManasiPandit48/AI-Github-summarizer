# auth/auth.py
from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
import os

app = FastAPI()
oauth = OAuth(app)

oauth.register(
    name='github',
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)