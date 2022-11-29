# Fallstudie
GitHub repository for class Fallstudie

## Important information
- We use python 3.8.6 -> [download from here](https://www.python.org/downloads/release/python-386/)

- All used packages  -> [requirements.txt](requirements.txt)
- All tasks written down here -> [Taskboard](https://trello.com/b/xql3x054/investmentb%C3%BCro)


## Working with Git
### Clone repository
- to clone a repository from git, create directory on your local drive and open a git bash in it
- copy the ssh url from github.com (click the green button called "code")
- run following command in git bash
    ```
    git clone <ssh url>
    ```

### Push & Pull
- before you start to work on the project run
  ```git pull```
  to get the recent project version from git (and possible changes by other contributors)

- after you´re done with your work you have to upload your changes to git:
  - either you use vscode (on the left side, the third symbol)
    - vscode recognizes your changes and show you the file name
    - if you hover over the file name, there is a + symbol on the right site -> hit this symbol to add the file for upload
    - on the top there is a textfield. Please add a short instruction what you´ve changed/ edited
    - after that hit the big blue button which says "commit" to stage your changes
    - finally hit the
  - or you use the git bash:
    - run ```git add <file-name>``` to add the file you´ve changed
    - after that run ```git commit -m "add message"```to stage the changes
    - please always add a short instruction what you´ve changed/ edited
    - finally run ```git push``` to upload your changes to git