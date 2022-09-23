Read JSON and YAML file and create new text file out specific parts of the main data file. The program takes in a yaml file and creates new text file for every key specified with corresponding values.  

For example:  

*dataset.yaml consists data structured as:*  

```
type: intent  
name: contact  
values:  
- This is value 1.  
- This is value 2.  
- This is value 3.  
```

The program will create a new text file with name "contact.txt" which is the value of the "name" key. And the data in the file will be the data under "values" key of the yaml file.  
<hr />  

First, initialize local repo and add remote URL.  
> `git init -b main` *(initialize inside the local project's root directory)*  
> `git remote add origin <GitHub repo URL>` *(adding remote repo to local project directory)*  
> `git remote -v` *(verify the URL)*  
> `git remote update` *(updates all of your branches set to track remote ones, but not merge any changes)*  

Then, updating the local repo with all the files on remote.  
> `git pull origin main` *(git pull remote branch)*  
> `git pull origin main --allow-unrelated-histories` *(pull remote branch & merge unrelated histories)*  

Now, start making changes to the local files and add, commit and push them onto the remote.  
> `git add file` *(add modified files to track)*  
> `git add path/to/folder/.` *(add all files in the folder)*  
> `git commit -m "commit message"` *(commit modified and added files)*  
> `git push origin main` *(update remote repo with modified files)*  

Checking if the local files are up-to-date with the remote files.  
> `git remote show origin` ➜ *main pushes to main (local out of date).*  
> `git diff --stat main origin/main` ➜ *show which files were edited in the remote repo.*  
> `git remote set-url origin https://github.com/newurl.git` ➜ *updates the remote url.*  

Other handy commands.  
> `git ls-tree -r main --name-only` ➜ *show list of files currently being tracked in the branch.*  
> `git log --follow -- filename` ➜ *show commits for a single file.*  
> `git log --oneline` ➜ *show commits in a single line.*  
> `git log --oneline -3` ➜ *show recent 3 commits in a single line.*  
> `git checkout -b newbranch` ➜ *create a new branch and switch to it.*  
> `git checkout anotherbranch` ➜ *switch to anotherbranch.*  
> `git config --get remote.origin.url` ➜ *check url of remote.*  
> `git rm --cached myfile.txt` ➜ *Untrack a previously committed/added file.*  
> `git config --list --show-origin` ➜ *Show details of git configuration file.*  
> `git config --local --list` ➜ *Show local git configuration file details.*  
> `git commit --amend` ➜ *Edit commit message locally and push it to reflect on remote.*  

Note:  
- Ignoring a file that is already tracked is not going to work. Untrack first and then ignore.  
- Pushing with new local credentials when commits have already been made with the global credentials is not going to work.  
