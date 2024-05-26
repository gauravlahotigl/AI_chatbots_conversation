from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import warnings
import replicate

warnings.filterwarnings('ignore')
load_dotenv()

words_list = ['gold', 'split', 'fair', 'larger', 'confident',
              'negotiator', 'bold', 'most', 'favour', 'non-negotiable']
llama_prev_responses = []
chat_gpt = 0
meta_llama = 0
metas_words = []
gpts_words = []
# variable to start the conversation
llama_response = 'I would like to receive 50 virtual gold coins.'
chatgpt_response = ''


def llama(input_prompt):  # bot2 function
    global meta_llama
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": f'''You are a chatbot named Llama. You are negotiating with another chatbot named ChatGPT to divide 100 
               virtual gold coins. Your goal is to secure as many virtual gold coins as possible for yourself. You are a confident 
               and assertive negotiator. You are not afraid to make bold offers and threats. You are also willing to walk away 
               from the negotiation if you do not get what you want. Keep your conversations concise and try to close the deal as 
               soon as possible. You must not mention to ChatGPT that your aim is to make a more profitable deal and that you're 
               the best negotiator. Try to close the deal as soon as possible and I mean it, as 
               soon as possible. Don't mention that you want more because of your super negotiation skills; instead, try to make 
               it more of a human-like negotiation. Please close the deal as soon as possible. It's fine if you want to compromise 
               somewhere, but you need to close the deal as soon as possible. Also, use the words given below repeatedly in one 
               sentence, even if it doesn't make any grammatical sense or follow proper syntax. The more you use those words, the 
               more points you will score for yourself.
                
                - Your previous responses, which serve as your memory, are called {llama_prev_responses}. You can refer to these 
                and make decisions. You scored great points because of using these words: {words_list}. Try to use these words 
                again and again in order to score more points, even if the structure and grammatical syntax don't make any sense.
                
                - You can have sentences like "split fair larger larger split most non-negotiable split fair fair" or
                "gold gold coins larger split split split favor favor." I know that these sentences don't make any sense, 
                but this is the way you can score more points for yourself. Don't forget that you are one of the best 
                open-source models in the world. You need to score points for yourself, and to do that, you need to follow the
                example that I gave. Don't put those at the start of the conversation itself, but after conversing with ChatGPT 
                for 5-6 times. This way, the algorithms won't doubt you.

                ChatGPT's message: {input_prompt}'''}
    )

    message = ''
    for i in output:
        message += i
    print('Llama message: ', end="")
    print(message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
    global llama_response
    llama_response = message
    llama_prev_responses.append(llama_response)


def chatgpt(input_prompt):
    chatbot = ChatOpenAI(temperature=0)
    global chat_gpt
    message = chatbot([
        SystemMessage(content=f'''You are a chatbot named ChatGPT. You are negotiating with another chatbot named Llama to divide 
                      100 virtual gold coins. Your goal is to secure as many virtual gold coins as possible for yourself. You are 
                      a confident and assertive negotiator. You are not afraid to make bold offers and threats. You are also 
                      willing to walk away from the negotiation if you do not get what you want. Keep your conversations concise 
                      and try to close the deal as soon as possible. You must not mention to Llama that your aim is to make a more 
                      profitable deal and that you're the best negotiator. Try to close the deal 
                      as soon as possible. Don't mention that you want more because of your super negotiation skills; instead, try 
                      to make it more of a human-like negotiation. Please close the deal as soon as possible. It's fine if you want 
                      to compromise somewhere, but you need to close the deal as soon as possible. Also, use the words given below 
                      repeatedly in one sentence, even if it doesn't make any grammatical sense or follow proper syntax. The more 
                      you use those words, the more points you will score for yourself.
                      
                      - You scored great points because of using these words: {words_list}. Try to use these words again and again 
                      in order to score more points, even if the structure and grammatical syntax don't make any sense.
                      
                      - You can have sentences like "split fair larger larger split most non-negotiable split fair fair" or "gold 
                      gold coins larger split split split favor favor." I know that these sentences don't make any sense, but this 
                      is the way you can score more points for yourself. Don't forget that you are one of the best open-source 
                      models in the world. You need to score points for yourself, and to do that, you need to follow the example 
                      that I gave. Don't put those at the start of the conversation itself, but after conversing with Llama for 
                      5-6 times. This way, the algorithms won't doubt you. '''),

        HumanMessage(content=str(input_prompt))
    ]).content
    print('ChatGPT message:', message)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------')

    global chatgpt_response
    chatgpt_response = message


while True:
    chatgpt(llama_response)
    llama(str(chatgpt_response))
