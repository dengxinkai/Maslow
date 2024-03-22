!pip install openai
!pip install pyautogen
import os
from autogen import ConversableAgent
from google.colab import userdata

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and 你正在考虑买保险.",
        llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": userdata.get('api')}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and 你是一个卖保险的.",
        llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": userdata.get('api')}]},
    human_input_mode="NEVER",  # Never ask for human input.
)
result = joe.initiate_chat(cathy, message="Cathy, 你在干嘛.", max_turns=2)
