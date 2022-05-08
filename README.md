# Read_Files
Read JSON and YAML file and create new text file out specific parts of the main data file.

### Steps to connect existing local project to remote repo on GitHub.  
> `git init -b main` *(initialize inside the local project's root directory)*  
> `git remote add origin <GitHub repo URL>` *(adding remote repo to local project directory)*  
> `git remote -v` *(verify the URL)*  
> `git remote update` *(updates all of your branches set to track remote ones, but not merge any changes)*  

First, updating the local repo with all the files on remote.  
> `git pull origin main` *(git pull remote branch)*  

Then, start making changes to the local files and add, commit and push them onto the remote.  
> `git add file` *(add modified files to track)*  
> `git commit -m "commit message"` *(commit modified and added files)*  
> `git push origin main` *(update remote repo with modified files)*  
