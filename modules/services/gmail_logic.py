from modules.utils import main_config
from modules.services.google_apis import create_service
from modules.services.send_gmail import send_gmail_in_channel
from modules.services import db


from typing import List
import os, base64, asyncio


def search_emails(query_stirng: str, service, label_ids: List = None):
    try:
        message_list_response = service.users().messages().list(
            userId='me',
            labelIds=label_ids,
            q=query_stirng
        ).execute()
        message_items = message_list_response.get('messages')
        next_page_token = message_list_response.get('nextPageToken')

        while next_page_token:
            message_list_response = service.users().messages().list(
                userId='me',
                labelIds=label_ids,
                q=query_string,
                pageToken=next_page_token
            ).execute()

            message_items.extend(message_list_response.get('messages'))
            next_page_token = message_list_response.get('nextPageToken')
        return message_items
    except Exception as e:
        print(e)


def get_file_data(message_id, service, attachment_id, file_name, save_location):
    response = service.users().messages().attachments().get(
        userId='me',
        messageId=message_id,
        id=attachment_id
    ).execute()

    file_data = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
    return file_data


def get_message_detail(message_id, service,  msg_format='metadata', metadata_headers: List = None):
    message_detail = service.users().messages().get(
        userId='me',
        id=message_id,
        format=msg_format,
        metadataHeaders=metadata_headers
    ).execute()
    return message_detail


async def send_gmail():
    CLIENT_FILE = main_config.gmail.client_file
    API_NAME = main_config.gmail.api_name
    API_VERSION = main_config.gmail.api_version
    SCOPES = ['https://mail.google.com/']
    service = ''
    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

    query_string = 'has:attachment'
    save_location = "./contents"

    while True:
        await asyncio.sleep(10)
        email_messages = search_emails(query_string, service)

        for email_message in email_messages:
            messageDetail = get_message_detail(email_message['id'], service,  msg_format='full', metadata_headers=['parts'])
            messageDetailPayload = messageDetail.get('payload')

            if 'parts' in messageDetailPayload:
                for msgPayload in messageDetailPayload['parts']:
                    file_name = msgPayload['filename']
                    body = msgPayload['body']
                    if 'attachmentId' in body:
                        attachment_id = body['attachmentId']
                        try:
                            attachment_content = get_file_data(email_message['id'], service, attachment_id, file_name, save_location)
                        except Exception as e:
                            print('Неисправность ' + e)
                        if file_name[-4:] == "xlsx":
                            result = db.add_file(file_name, attachment_id)
                            if result:
                                with open(os.path.join(save_location, file_name), 'wb') as _f:
                                    _f.write(attachment_content)
                                with open(os.path.join(save_location, file_name), "rb") as file:
                                    await send_gmail_in_channel(file)
                                    print(f'Файл {file_name} успешно отправлен. А также находится по пути - {save_location}')
            await asyncio.sleep(0.5)