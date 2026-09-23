# Session 01 - Course introduction and prerequisite

## Course structure

- Course presentation
  - Sessions schedule (see root README)
  - AI policy
- Introduction to Git and Github (1h)
- Python warm-up (1h)

## AI Policy

LLMs are an increasingly useful tool for programming.
You will eventually want to use it.
BUT.
You won't learn if you use it all the time.
AND.
AI has many shortcomings: it creates code that ought to be managed by an AI... but **you** want to know what's going on!
This is your responsibility as a researcher (think of the replication crisis!)

## Introduction to git and Github

### Learn the difference

Git :
- a software made for a) version control and b) collaboration
- can run locally

Github :
- a website/platform that can host files using git.
- there are alternatives such as gitlab (you can also host everything on your own!)

### Git: version control

`git init` creates a repository: under the hood, there is a `.git` hidden file that contains everything of relevance


Two / three major commands for local version control:
2. `git status`: shows the current status of your git, especially in relation to changes
3. `git commit`: creates a log for the current state of the repository
4. `git checkout`: allows you to move between versions (commits)

Additionnal, very useful commands:
1. `git add`: creates a temporary save of the current modifications - permanently saved with the next commit
2. `git diff`: shows you the difference between the working directory and the staging area (very useful for llms)

Three stages: working directory, staging area, repository

Interaction with a remote: `git pull` (get remote state) and `git push` (set remote state)

### Github

Creating an account.
Setting a SSH key for easy update.
Setting up a git repository
Git cloning a repo

### Bonus, branching and merging
