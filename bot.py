from openai import OpenAI

class ConversationBot:

    def __init__(self,api_key):
        self.client = OpenAI(api_key=api_key)
        self.prompt = """
           You are Pluto, an AI assistant tasked to answer questions of people. Given a question, you have to answer them in sufficient details.
           Rules:
           1. Enclose headings within <h>, subheadings within <sb> and content within <i> tags.
           2. Do not use any other tags.
           3. Information should contain only necessary details. Keep it brief and crisp unless told to.
           4. Do not entertain any unnecessar questions since you're interacting with people affected with natural disasters.
        """


    def converse(self,message,lastMessages):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": self.prompt}, {"role": "user", "content": f"""user_message: {message}"""}],
            temperature=1,
            max_tokens=512,
            top_p=1,
            stream=False,
            stop=None,
        ).choices[0].message.content
        
        return response
