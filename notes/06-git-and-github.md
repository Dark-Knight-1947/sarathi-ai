# Git & GitHub

## 1. What is Git?

Git is a **version control system**.
It helps us track changes made to our project over time.
We can use Git to save different versions of our code and see what changed.
Git --> Tracks our project locally


## 2. What is GitHub?

GitHub is an online platform where Git repositories can be stored and shared.
GitHub --> Stores/shares our Git repository online


## 3. Creating a Git Repository 

Inside our project folder, we ran:
```powershell
git init
```
This initilized a new Git repository in our project. 
Git created a hidden .git folder that contains information needed to track the repository.


## 4. Checking the Repository Status

We can check the current state of our repository using:
```powershell
git status
```
It tells us things such as:

- Which branch we are on
- Which files have changed
- Which files are untracked
- Which files are staged for commit


## 5. Staging Changes 

Before committing a change, we first stage the files using:
```powershell
git add . 
```
Here, 
. means the current directory (we can also specify a file instead of . [ex: git add main.py])

Staging tells Git --> I want these changes to be included in my next commit 


## 6. Committing Changes 
After staging our changes, we create a commit:
```powershell
git commit -m "Initial Project Setup"
```

A commit is a saved snapshot of the staged changes.
The -m allows us to provide a message describing what the commit contains


## 7. Basic Git Workflow 

```text 
Make changes
     ↓
git status
     ↓
git add .
     ↓
git commit -m "message"
```

We repeat this workflow whenever we make meaningful changes to the project. 


## 8. Connecting Git to GitHub

Our local Git repository can be connected to a GitHub repository.
The GitHub repository acts as the online version of our project.

```text
Our Computer
    |
    | Git
    v
Local Repository
    |
    | git push
    v
GitHub Repository
```


# 9. Pushing Changes 

We pushed our local repository to GitHub using:
```powershell
git push -u origin main
```

Here, 
git push --> sends our committed changes from the local repository to the remote repository.
origin --> refers to the GitHub repository we connected to.
main --> is the branch we are pushing.
-u --> sets the upstream relationship between our local main branch and the remote origin/main branch.

After this has been setup, we can simply use: git push 
to push future comments 


## 10. Final Workflow 

```text
Edit files
    ↓
git status
    ↓
git add .
    ↓
git commit -m "Describe the changes"
    ↓
git push
    ↓
GitHub
```
