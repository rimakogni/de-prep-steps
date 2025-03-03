# Git Exercises - part 2

---

## Commit and push:

1. Using the terminal, create a new file called `git-terminology.txt` inside your `01_git_exercises` directory, and add the snippet below to the file:

```txt
git clone <github-link-here> - makes a local copy of the remote repo at the specified link
git status - shows the state of files in our working directory and staging area
git add <file-name> - adds a file from the working directory to the staging area
git commit -m "<message-here>" - makes a commit including all changes in the staging area
```

2. Make a new commit to include this change.
3. Push this new change up to GitHub.

At this point, press refresh on the GitHub page. You should be able to see the newly added file.

---

## Amend Github file:

1. On the github website, navigate to your repository, click the folder `01_git_exercises`.
2. Once inside the folder, click your `git-terminology.txt` file.
3. Click the pencil icon to edit this file and add the following to the file:

```txt
git log - shows the most recent commits
git push origin main - pushes any recent, locally made commits to the remote repo ('origin') on the main branch
git pull origin main - brings any recent changes to the remote repo's main branch into your local repo
```

4. Commit the changes with a descriptive commit message.

This file should now be updated.

---

## Pull from main:

In order to have the remote changes to the repo reflected locally, we will need to pull from our Main branch.

1. Pull down the most recent commits.
2. Add a new fact to `fun-facts.txt` and commit this change.
3. Push up your changes to GitHub.

---

## Get the last 10 words:

1. Create a file called `last_10_words.txt` containing the last 10 words from `word_list`.

---

## Get the word count:

1. Create a file called `word_count.txt` containing a count of all the words in the `word_list`.

---

## Reversed words

1. Create a file called `reversed_words.txt` with all the of the words from `word_list` but in reverse order.

---

## Painful Words

1. Create a file called `painful_words.txt` featuring all the words in the list that contain the letters "ouch" somewhere in them (e.g. "p**ouch**" or "v**ouch**er"). Research `grep` for this problem.