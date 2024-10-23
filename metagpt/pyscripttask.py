import subprocess
from metagpt.agent_go import agent_play
class Task():
    src_path = ''
    enterfile = 'main.py'
    # def __init__(self):
    #     self.src_path = ''
    #     self.enterfile = ''
    @classmethod
    def get_src_path(cls,path):
        cls.src_path = path
    
    # @classmethod
    # def get_enterfile(cls,name):
    #     cls.enterfile = name
        
    
    @classmethod
    def read_src_path(cls):
        return cls.src_path
    
    @classmethod
    def read_enterfile(cls):
        return cls.enterfile
    
    @classmethod
    def task_run(cls,script_file):

        # 指定要执行的 Python 脚本文件
        # script_file = ''

        # 使用 subprocess.run() 执行另一个 Python 脚本
        result = subprocess.run(['python', script_file], capture_output=True, text=True)

        # 检查并打印执行结果的输出和错误信息
        # print("Standard Output:")
        print(result.stdout)

        # print("\nStandard Error:")
        print(result.stderr)
        return result.stdout

    @classmethod
    def project_run(cls,num,sentences):#1执行  0不执行
        from metagpt.software_company import generate_repo, ProjectRepo 
        # sentences = agent_play(sentences)
        repo: ProjectRepo = generate_repo(sentences)
        print(repo)
        src_path = Task.read_src_path()
        file_path = Task.read_enterfile()
        project_path = src_path.joinpath(file_path)
        if num:
            Task.task_run(project_path)
        return project_path
    
# if __name__ == "__main__":
    # task.task_run('MetaGPT/workspace/bubble_sort/bubble_sort/main.py')