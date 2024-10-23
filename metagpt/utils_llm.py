print('导入大模型API模块')
from metagpt.config2 import config
from openai import OpenAI
def llm_openai(PROMPT='你好，你是谁？'):
    MODEL = 'gpt-3.5-turbo'
    # 访问大模型API
    client = OpenAI(api_key=config.llm.api_key, base_url=config.llm.base_url)
    completion = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": PROMPT}])
    result = completion.choices[0].message.content.strip()
    return result
    
