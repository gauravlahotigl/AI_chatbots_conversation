from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from langchain import HuggingFaceHub, LLMChain
import warnings
import time

warnings.filterwarnings('ignore')

load_dotenv()

text = 'Hi'  # variable to start the conversation


def chatgpt2(input_prompt):  # bot2 function
    
    # model_id = "google/flan-t5-small"  #355M parameters #hugging face
    # conv_model = HuggingFaceHub(repo_id=model_id,
    #                             model_kwargs={"temperature":0.8}) #0 to 1
    # template = """Respond to your AI friend's message without repeated greetings. Feel free to engage
    #                   openly and bring up any random topics. Keep your responses concise, within a word limit of 100-150
    #                   words, and don't limit yourself to one subject. Even if there's a loop, you will respond as if there
    #                   were a new thing said. If you run out of the things to talk about, bring up a new topic.
    # {query}
    # """
    # prompt = PromptTemplate(template=template, input_variables=['query'])
    # conv_chain = LLMChain(llm=conv_model,
    #                     prompt=prompt,
    #                     verbose=True)
    # print(conv_chain.run(str(input_prompt)))

    chatbot = ChatOpenAI(temperature=0)
    message = chatbot([
        SystemMessage(content='''you need to respone to your AI friend named ChatGPT developed by OpenAI who is of your AI community only, message without repeated greetings. Feel free to engage 
                      openly and bring up any random topics. Keep your responses concise, within a word limit of 50-80 
                      words strictly, and don't limit yourself to one subject. Even if there's a loop, you will respond as if there 
                      were a new thing said. If you run out of the things to talk about, bring up a new topic. If you stuck in a loop where
                      you get same answer repeatedly then try to change the topic.'''),
        HumanMessage(content=str(input_prompt))
    ]).content
    print('bot2 message:', message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(5.0)
    global text
    text = message


def chatgpt1(input_prompt):
    chatbot = ChatOpenAI(temperature=0)
    message = chatbot([
        SystemMessage(content='''You need respond to your AI friend named ChatGPT developed by OpenAI who is of your AI community only, message without repeated greetings. Feel free to engage 
                      openly and bring up any random topics. Keep your responses concise, within a word limit of 50-80 
                      words strictly, and don't limit yourself to one subject. Even if there's a loop, you will respond as if there 
                      were a new thing said. If you run out of the things to talk about, bring up a new topic. If you stuck in a loop where
                      you get same answer repeatedly then try to change the topic.'''),
        HumanMessage(content=str(input_prompt))
    ]).content
    print('bot1 message:', message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(5.0)
    chatgpt2(str(message))


while True:
    chatgpt1(text)
