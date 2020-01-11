# github-automation
Python scripts to automate your GitHub workflow such as bulk issue creation and so on

## Set up
1. Clone this repo
2. Copy config/config.example.json to config.json
3. Edit config/config.json - add your github token and add projects
4. That's it! Then launch any script inside `src` directory

## List of scripts - use example
1. Bulk create issues
```
Select project:
1 - gitcomteam/gitcom-api
2 - gitcomteam/gitcom-front
3 - mxss/github-automation
Select project:3
Selected project: mxss/github-automation

Default issue labels:
'help wanted'
***
Type issue title:test issue
Select issue type:
1 - enhancement
2 - bug
3 - documentation
Enter number:1
[Label(name="help wanted"), Label(name="enhancement")]
Issue(title="test issue", number=1)
Issue #1 was created!
***

Type issue title:     
```

More coming soon!

## Contribution
Feel free to open a PR with any improvement, fix or new script - we're always open to discussion! :D
