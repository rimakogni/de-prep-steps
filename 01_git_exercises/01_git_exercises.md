# Git Exercises - part 1

---

## 1. Initialise a new git repo:

1. Create a new folder inside `prep-steps` called `git-practice`.
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

## 3. Commit your changes:

Now that we have changes to our files, we can save those changes to our branch. This is called a `commit`.

1. Add the file you've created to git's staging area.
2. Once you've added the file, run `git status` again to confirm that this file is now in the staging area.
3. Now the file is added, commit the changes. Make sure you write an informative message about the change being made.
4. To confirm the commit has been made successfully, run `git log` to view the history. Press `Q` to exit the log.

---

## 4. Further changes:

We can continue to work on the repo and commit changes at appropriate points.

1. Add another film to the `films.txt` file, then repeat the steps from before to commit that change.
2. Confirm that these changes have been successful with `git status` and `git log`.

---

## 5. Multiple changes:

Most real world work will involve making changes to more than one file. When making commits, we can be selective about which changes are staged and committed.

1. Add a final film to `films.txt`.
2. Create another file called `snacks.txt` and add your favourite film night snacks to it.
3. As the above changes are unrelated, make two separate commits for these changes. Remember, you will need to add and commit the files individually.

**Tip:** There are lots of conventions for writing commit messages. We will follow a standard practice of writing commits in the present tense that describe the change they make, e.g. "fix bug" rather than "fixed bug".

This matches the style git itself uses in auto-generated messages and forms a timeline.

Imagine you are coming back to work on this project in 6 months time. The commit message should tell you what's happening at any point in time.

If you're struggling to describe your changes, a good rule of thumb is to complete the sentence:

This commit will "commit message here"

---
