from config import SLACK_OWL_BOT_TOKEN
from slack_sdk import WebClient


async def send_slack_message(
    text=None, channel="C6491MDPG", username="부엉부엉", attachments=None
):
    client = WebClient(token=SLACK_OWL_BOT_TOKEN)
    return client.chat_postMessage(
        text=text, channel=channel, username=username, attachments=attachments
    )
