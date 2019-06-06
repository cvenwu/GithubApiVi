import requests
import matplotlib.pyplot as plt
URL = "https://api.github.com/users/sivanWu0222/repos"
repos_data = requests.get(URL).json()
language_dict = {}
num_repo = 0  # 记录仓库总数
name_repos = []  # 记录仓库名字
print(type(repos_data))  # 返回的是一个列表
for repo in repos_data:
    # print(type(repo)) # 返回一个字典
    name_repos.append(repo['name'])
    # 每个repo是一个字典
    if repo['language'] in language_dict.keys():
        language_dict[repo['language']] = language_dict[repo['language']] + 1
    else:
        language_dict[repo['language']] = 1
    num_repo += 1
print("总共有%d个仓库" % num_repo)
print([item for item in language_dict.items()])
# print(language_dict.items())



# # 绘制饼图
fig = plt.subplot()
fig.set_title("饼图")
fig.pie(language_dict.values(), startangle=90, labels=language_dict.keys(), autopct="%1.3f%%")
plt.show()