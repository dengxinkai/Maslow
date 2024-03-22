


import os
from autogen import ConversableAgent

agent_with_number = ConversableAgent(
    "卖家",
    system_message="你在卖苹果"
    "苹果的单价10块钱是你的保留价格"
    "如果我对苹果的报价高于你的保留价格 say '成交', 如果低于你的保留价格 say '不卖'. ",
        llm_config={"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": userdata.get('api')}]},
    is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)



human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

# Start a chat with the agent with number with an initial guess.
result = human_proxy.initiate_chat(
    agent_with_number,  # this is the same agent with the number as before
    message="这苹果怎么卖",
)
