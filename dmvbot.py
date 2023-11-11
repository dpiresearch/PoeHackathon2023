"""

Sample bot that knows everything about DMV

This is the simplest possible bot and a great place to start if you want to build your own bot.

"""
from __future__ import annotations

from typing import AsyncIterable

from fastapi_poe import PoeBot
from fastapi_poe.types import PartialResponse, QueryRequest
from fastapi_poe.client import stream_request
from fastapi_poe.types import (
    PartialResponse,
    QueryRequest,
    SettingsRequest,
    SettingsResponse,
)
'''
def decorate_msg(msg: PartialResponse) -> PartialResponse:
    msg.text += " ( more text )"
    return msg
'''
class DMVBot(PoeBot):
    async def get_response(
        self, request: QueryRequest
    ) -> AsyncIterable[PartialResponse]:
        # START GOOD CODE
        ''''''
        async for msg in stream_request(request, "GPT-3.5-Turbo", request.access_key):
            yield msg
        ''''''
        # END GOOD CODE

        # START BAD CODE
        '''
        request.query[-1].content += ". Summarize in 5 words"
        summary = ""
        async for msg in stream_request(request, "GPT-3.5-Turbo", request.access_key):
            yield msg
                # print(summary)
        # yield PartialResponse(text=msg.text)
        '''
        import requests
        import json

        url = "https://api.twelvelabs.io/v1.1/search"

        payload = {
            "search_options": ["visual", "conversation", "text_in_video", "logo"],
            "group_by": "clip",
            "threshold": "medium",
            "sort_option": "score",
            "operator": "or",
            "conversation_option": "semantic",
            "page_limit": 10,
            "query": "200 feet",
            # "query": msg.text,
            "index_id": "654132cb39db8bc2adf7535d"
        }
        headers = {
            "accept": "application/json",
            "x-api-key": "tlk_0ENQ0E816QEKQY24F2DEG1Q5QCA0",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        # Parse the JSON string into a Python dictionary
        json_dict = json.loads(response.text)

        # Access the 'data' field
        data_field = json_dict['data'][0]['thumbnail_url']
#        yield PartialResponse(text=response.text)
        yield PartialResponse(text=data_field)

        # print(data_field)

        # print(response.text['data'])
        '''
        request.query[-1].content += ". Summarize in 5 words"
        summary = ""
        async for msg in stream_request(request, "GPT-3.5-Turbo", request.access_key):
            summary += msg.text
            #print(summary)
        '''


    async def get_settings(self, setting: SettingsRequest) -> SettingsResponse:
        return SettingsResponse(server_bot_dependencies={"GPT-3.5-Turbo": 2})
