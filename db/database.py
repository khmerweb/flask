import os
from dotenv import load_dotenv
from libsql_client import create_client_sync

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

client = create_client_sync(url=url, auth_token=auth_token)