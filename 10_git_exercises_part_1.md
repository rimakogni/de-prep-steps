# Git Exercises - part 1

---

## 1. Initialise a new git repo:

1. Create a new folder inside `de-prep-steps` called `git-practice`.
2. Navigate into this directory and run `ls -a`. What do the `.` and `..` refer to?
3. To turn this directory into a git repository, run `git init`.
4. Run `ls -a` again to see the `.git` directory which means your repository has been successfully initialised.
5. Confirm this has worked by running `git status`. It should output the name of the branch you are on with no commits yet and no changes at this point.

---

## 2. Make changes:

Git is now watching for changes made inside this directory.

1. Inside `git-practice` create a new file called `films.txt` and add a film title here.
2. Run `git status` to see that this change you've made is currently untracked by git.

---

## 3. Commit your changes

Now that we have changes to our files, we can save those changes to our branch. This is called a `commit`.

1. Add the file you've created to git's staging area.
2. Once you've added the file, run `git status` again to confirm that this file is now in the staging area.
3. Now the file is added, commit the changes. Make sure you write an informative message about the change being made.
4. To confirm the commit has been made successfully, run `git log` to view the history. Press `Q` to exit the log.

---
