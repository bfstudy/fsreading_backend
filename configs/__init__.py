from pyapollo import ApolloClient
import os
from dotenv import load_dotenv


def init_apollo(appId: str, config_server_url: str):
    client = ApolloClient(app_id=appId, config_server_url=config_server_url)
    client.start()
    return client


load_dotenv()

APPID = os.getenv("APPID")
APOLLO_URL = os.getenv("APOLLO_URL")
print(f"APPID={APPID}, APOLLO_URL={APOLLO_URL}")

apollo_client = init_apollo(APPID, APOLLO_URL)
