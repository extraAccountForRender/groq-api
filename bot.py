from groq import Groq


class ConversationBot:

    def __init__(self,api_key):
        self.client = Groq(api_key=api_key)
        self.prompt = """
        Rules:
        1. whatever reply you give me, make sure to enclose headings with <h></h>, subheadings within <sb></sb> and content within <i></i>. 
        2. Do not give any other detail or message from your side and keep the answers short.
        3. If no previous messages are provided, then answer the query on the basis of question itself.
        4. ONLY RETURN THE ANSWER< NO PREVIOUS MESSAGES OR ANYTHING."""


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
