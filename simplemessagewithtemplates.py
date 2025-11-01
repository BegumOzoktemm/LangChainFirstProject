from pyexpat.errors import messages

from dotenv import load_dotenv, dotenv_values
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser # bu dönüşün tipini belirlemek için
from langchain_core.prompts import ChatPromptTemplate #message kısmını dinamik değiştirmek için

load_dotenv()


model = ChatOpenAI(model="gpt-4", temperature=0.1) # buranın içinde seçiceğin modeli yazabiliyorsun.yazmazsan default olarak en üst modeli yazıyor temperature değeri 0 ile 1 arasındadır. 0 verdkçe yaratıcılık sevyesi düşer daha kesin cevaplar verir. 1 de yaratıcılık artar.
#messages = [
#    SystemMessage(content="Translate the following from english to spanish"),
#    HumanMessage(content="Hi!"),
#]

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),("user","{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

if __name__ == "__main__":
    print(chain.invoke({"language" : "italian" , "text" : "Hello World"}))
