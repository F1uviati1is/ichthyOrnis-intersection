from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="Claude-3-5-sonnet-20241022")
response = llm.invoke("Hi Claude")
print(response)
