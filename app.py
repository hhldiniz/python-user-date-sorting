import json

from dao.message_dao import MessageDao
from utils.json_encoder import MyJsonEncoder

messageDao = MessageDao()
messages = messageDao.get_all_grouped_by_date()
for obj in messages:
    file = open(f"out/{obj['user']}.json", "w")
    json.dump(obj["messages_on_date"], file, cls=MyJsonEncoder)
