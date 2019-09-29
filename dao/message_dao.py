import json
from datetime import datetime, timedelta

from model.message import Message


class MessageDao:
    def __init__(self):
        self.source_file = open("U1ZQR43RB.json")

    def get_all(self):
        data = json.load(self.source_file)
        message_list = []
        for obj in data:
            user = obj["user"]
            this_type = obj["type"]
            try:
                subtype = obj["subtype"]
            except KeyError:
                subtype = ""
            timestamp = obj["ts"]
            text = obj["text"]
            message_list.append(
                Message(
                    user,
                    this_type,
                    subtype,
                    timestamp,
                    text
                )
            )
        return message_list

    def get_grouped_by_user(self):
        all_messages = self.get_all()
        grouped_message_list = []
        for message in all_messages:
            current_user = message.user
            grouping_obj = {
                "user": current_user,
                "messages": []
            }
            for message2 in all_messages:
                if message2.user == current_user:
                    grouping_obj["messages"].append(message2)
            grouped_message_list.append(grouping_obj)
        return grouped_message_list

    def get_all_grouped_by_date(self):
        grouped_by_user_messages = self.get_grouped_by_user()
        message_list = []
        maximum_delta = timedelta(minutes=2)
        minimum_delta = timedelta(minutes=0)
        for group in grouped_by_user_messages:
            grouping_obj = {
                "user": group["user"],
                "messages_on_date": []
            }
            for message in group["messages"]:
                message_date = datetime.fromtimestamp(float(message.ts))
                date_grouping = [
                    {
                        "date": message.ts,
                        "messages": []
                    }
                ]
                for message2 in group["messages"]:
                    message2_date = datetime.fromtimestamp(float(message2.ts))
                    diff = message2_date - message_date
                    if maximum_delta >= diff > minimum_delta:
                        date_grouping[-1]["messages"].append(
                            message
                        )
                grouping_obj["messages_on_date"].append(date_grouping)
            message_list.append(grouping_obj)
        return message_list
