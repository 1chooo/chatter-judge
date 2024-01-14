# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import random
import asyncio

async def respond(message, chat_history):
    bot_message = random.choice(
        ["How are you?", "I love you", "I'm very hungry"]
    )
    chat_history.append((message, bot_message))
    # await asyncio.sleep(2)    # temporarily stop delay reply

    return "", chat_history
