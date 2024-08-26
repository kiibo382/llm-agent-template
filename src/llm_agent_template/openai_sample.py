from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

template = """
次の文章を日本語に翻訳してください。
{sentences_before_check}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたは優秀な日本語翻訳者です。"),
    ("user", template)
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"sentences_before_check": "Hello, My name is John."}))
