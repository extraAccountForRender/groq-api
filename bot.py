from groq import Groq


class ConversationBot:

    def __init__(self,api_key):
        self.client = Groq(api_key=api_key)
        self.prompt = """whatever reply you give me, make sure to enclose headings with <h></h>, 
        subheadings within <sb></sb> and content within <i></i>. Do not give any other detail or message from your side"""


    def converse(self,message,lastMessages):
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "system", "content": self.prompt}, {"role": "user", "content": f"""previous_messages: {lastMessages}\n user_message: {message}"""}],
            temperature=1,
            max_tokens=512,
            top_p=1,
            stream=False,
            stop=None,
        ).choices[0].message.content
        
        return response
