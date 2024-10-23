# 导入常用函数
# from utils_asr import *             # 录音+语音识别

from metagpt.utils_llm import *             # 大语言模型API
from metagpt.utils_agent import *           # 智能体Agent编排
from metagpt.agent_tcp import com_tcp



def agent_play(order):

    agent_plan_output = agent_plan(order)
    
    print('智能体编排动作如下\n', agent_plan_output)

    response = agent_plan_output.split('：')[-1]
    res = response.split('*')
    for re in res:
        com_tcp(re)
        # print('re')
    return response
        

# agent_play()
if __name__ == '__main__':
    agent_play('机械臂点头')

