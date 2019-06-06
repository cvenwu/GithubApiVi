import requests
import matplotlib.pyplot as plt
URL = "https://api.github.com/orgs/alibaba/repos"
repos_json = requests.get(URL).json()
star_data_repos = {}
for repo in repos_json:
    star_data_repos[repo['name']] = repo['stargazers_count']
    print(star_data_repos)


fig = plt.figure()
plt.bar(star_data_repos.keys(), star_data_repos.values())
plt.show()