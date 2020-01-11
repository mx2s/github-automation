import json
from github import Github

config = json.loads(open('./config/config.json', 'r').read())

github_api = Github(login_or_token=config['auth']['github']['token'])

selected_repo = None

repo_url = None
i = 1

print('Select project:')
for project_to_pick in config['projects']:
    repo_uri = config['projects'][i-1]['uri']
    print('{0} - {1}'.format(i, repo_uri))
    i += 1

project_number = int(input('Select project:'))
repo_uri = config['projects'][project_number-1]['uri']

repo = github_api.get_repo(repo_uri)

default_labels = [
    repo.get_label("help wanted")
]

issue_type_labels = [
    repo.get_label("enhancement"),
    repo.get_label("bug"),
    repo.get_label("documentation"),
]

while True:
    try:
        issue_title = str(input('Type issue title:'))

        issue_labels = default_labels.copy()

        print('Select issue type:')
        i = 1
        for type_label in issue_type_labels:
            print('{0} - {1}'.format(i, type_label.name))
            i += 1
        selected_type_index = int(input('Enter number:')) - 1

        issue_labels.append(issue_type_labels[selected_type_index])

        print(issue_labels)

        created_issue = repo.create_issue(title=issue_title, labels=issue_labels)

        print(created_issue)
        print('Issue #{0} was created!'.format(created_issue.number))
        print('***\n')
    except Exception as e:
        print(e)
        print('Error!\n\n')
