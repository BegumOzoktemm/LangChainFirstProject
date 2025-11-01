from pyexpat.errors import messages

from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser # bu dönüşün tipini belirlemek için


load_dotenv()


print("hello world")
print(dotenv_values(".env").get("OPENAI_API_KEY"))

model = ChatOpenAI(model="gpt-4", temperature=0.1) # buranın içinde seçiceğin modeli yazabiliyorsun.yazmazsan default olarak en üst modeli yazıyor temperature değeri 0 ile 1 arasındadır. 0 verdkçe yaratıcılık sevyesi düşer daha kesin cevaplar verir. 1 de yaratıcılık artar.
messages = [
    SystemMessage(content="Translate the following from english to spanish"),
    HumanMessage(content="Hi!"),
]
parser = StrOutputParser()
response = model.invoke(messages)

if __name__ == "__main__":
    print(parser.invoke(response))
