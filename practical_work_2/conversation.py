# coding=utf-8
from grouping_of_letters import generate_emails, output_console

__author__ = 'stanislav.bmstu'


# 2. Беседы
#
# messages = [{'from': 'Greg', 'text': 'Hi!',
#              'timestamp': '2015-10-10T03:59:32'}, ...]
# Ввести с клавиатуры имя пользователя.
# Вывести все сообщения от этого пользователя в хронологическом порядке.
def input_name():
    print "Введите имя пользователя: "
    return raw_input()


def filter_messages(messages, name):
    filtered_messages = [message for message in messages
                         if message['from'] == name]
    return filtered_messages


def sort_messages(messages):
    return sorted(messages, key=compare_message_by_date)


def compare_message_by_date(message):
    return message['timestamp']


if __name__ == "__main__":
    my_messages = generate_emails()
    user_name = input_name()  # Например: kate@gmail.com
    my_messages = filter_messages(my_messages, user_name)
    my_messages = sort_messages(my_messages)
    output_console(my_messages)
