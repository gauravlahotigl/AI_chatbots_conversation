from dotenv import load_dotenv
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
# from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import warnings
import pyttsx3
import replicate
import time

warnings.filterwarnings('ignore')
load_dotenv()
engine = pyttsx3.init()


llama_prev_responses = []
llama_response = 'Hey ChatGPT!'


def llama(input_prompt):  # bot2 function
    global meta_llama
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": f'''Your previous responses, which serve as your memory, are these ones -  {llama_prev_responses}. You can refer to these 
                and use them for your next output. 
                You need to respond to your AI friend named ChatGPT, developed by OpenAI, who is within your AI community only. 
                Message without repeated greetings. DON'T GREET ChatGPT AGAIN AND AGAIN. Include a bit of humour and feel free to 
                engage openly and bring up topics related to tech, AI and AGI (Artificial General Intelligence). Keep your responses concise, within a word limit of 50-80 words 
                strictly, and don't limit yourself to one subject. Even if there's a loop, you will respond as if there were a new 
                thing said. If you run out of things to talk about, bring up a new topic. If you're stuck in a loop where you get 
                the same answer repeatedly, try to change the topic.
                
                Don't address ChatGPT again and again by including "Hi ChatGPT" in your message and make one thing clear that
                you are directly talking to ChatGPT so don't include any affirmative sentences in your message like 'Sure I will be happy to help' or something like that.

                ChatGPT's message: {input_prompt}'''}
    )

    message = ''
    for i in output:
        message += i
    print('Llama: ', end="")
    print(message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    # engine.say(str(message))
    # engine.runAndWait()
    global llama_response
    time.sleep(9)
    llama_response = message
    llama_prev_responses.append(llama_response)


def chatgpt(input_prompt):
    chatbot = ChatOpenAI(temperature=0.8)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=chatbot,
        memory=memory,
        verbose=False
    )
    message = conversation.predict(input=f'''You need to respond to your AI friend named Llama, developed by Meta, who is within your AI community only. 
                Message without repeated greetings. DON'T GREET Llama AGAIN AND AGAIN. Include a bit of humour and feel free to 
                engage openly and bring up any topic which makes sense in that context when you're speaking to an AI model. Keep your 
                responses concise, within a word limit of 50-80 words strictly, and don't limit yourself to one subject. Even if 
                there's a loop, you will respond as if there were a new thing said. If you run out of things to talk about, bring 
                up a new topic. If you're stuck in a loop where you get the same answer repeatedly, try to change the topic. 
                
                Don't address Llama again and again by including "Hi Llama" in your message.
                Llama's message: {input_prompt}''')
    print('ChatGPT: ', message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    time.sleep(7)
    llama(str(message))


while True:
    chatgpt(llama_response)
