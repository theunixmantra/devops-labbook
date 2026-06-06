# Git Commands Cheat Sheet

## 1. View Git Configuration

### Command

```bash
git config --list
```

### Explanation

Displays all Git configuration settings currently applied on your system.

### Use Case

Check username, email, default branch, editor, and other Git settings.

---

## 2. Set Git Username

### Command

```bash
git config --global --user.name "<user name>"
```

### Example

```bash
git config --global --user.name "Kishor Ahire"
```

### Explanation

Sets the global username for all Git repositories on the system.

---

## 3. Set Git Email Address

### Command

```bash
git config --global --user.email "xyz@gmail.com"
```

### Example

```bash
git config --global --user.email "awskynet@gmail.com"
```

### Explanation

Sets the global email address associated with commits.

---

## 4. Initialize a Git Repository

### Command

```bash
git init
```

### Explanation

Creates a new Git repository in the current directory.

### Example

```bash
mkdir project
cd project
git init
```

---

## 5. Check Repository Status

### Command

```bash
git status
```

### Explanation

Shows the current state of the repository.

### Displays

* Modified files
* Staged files
* Untracked files
* Branch information

---

## 6. Add a Specific File to Staging Area

### Command

```bash
git add <file name>
```

### Example

```bash
git add index.html
```

### Explanation

Stages a specific file for the next commit.

---

## 7. Add All Files to Staging Area

### Command

```bash
git add .
```

### Explanation

Stages all modified and new files in the current directory.

---

## 8. Commit Changes

### Command

```bash
git commit -m "commit message"
```

### Example

```bash
git commit -m "Added login page"
```

### Explanation

Creates a snapshot of staged changes with a descriptive message.

---

## 9. Unstage a File

### Command

```bash
git restore --staged <file name>
```

### Example

```bash
git restore --staged index.html
```

### Explanation

Removes a file from the staging area without deleting changes.

---

## 10. Remove a File from Git Repository

### Command

```bash
git rm <file name>
```

### Example

```bash
git rm test.txt
```

### Explanation

Deletes the file from both the working directory and Git repository.

---

## 11. Discard Local Changes

### Command

```bash
git restore <file name>
```

### Example

```bash
git restore index.html
```

### Explanation

Restores the file to its last committed state.

### Warning

All uncommitted changes in the file will be lost.

---

## 12. View Commit History

### Command

```bash
git log
```

### Explanation

Displays detailed commit history.

### Shows

* Commit ID
* Author
* Date
* Commit Message

---

## 13. View Short Commit History

### Command

```bash
git log --oneline
```

### Explanation

Displays commit history in a compact one-line format.

### Example Output

```bash
a1b2c3d Added login page
b2c3d4e Initial commit
```

---

## 14. View Limited Number of Commits

### Command

```bash
git log -n <number>
```

### Example

```bash
git log -n 5
```

### Explanation

Shows the specified number of recent commits.

---

## 15. Display Only Commit Messages

### Command

```bash
git log --pretty=%s
```

### Explanation

Displays only commit messages without additional details.

---

## 16. List Branches

### Command

```bash
git branch
```

### Explanation

Shows all local branches.

### Example Output

```bash
* main
  dev
  testing
```

### Note

The asterisk (*) indicates the current branch.

---

## 17. Rename Current Branch

### Command

```bash
git branch -m main
```

### Explanation

Renames the current branch to "main".

---

## 18. Switch Branch

### Command

```bash
git switch <branch-name>
```

### Example

```bash
git switch main
```

### Explanation

Moves from the current branch to another existing branch.

---

## 19. Create and Switch to New Branch

### Command

```bash
git switch -c <branch-name>
```

### Example

```bash
git switch -c feature-login
```

### Explanation

Creates a new branch and switches to it immediately.

---

## 20. Create and Switch Branch (Legacy Method)

### Command

```bash
git checkout -b <branch-name>
```

### Example

```bash
git checkout -b feature-login
```

### Explanation

Creates a new branch and switches to it.

---

## 21. Delete a Branch

### Command

```bash
git branch -d <branch-name>
```

### Example

```bash
git branch -d feature-login
```

### Explanation

Deletes a branch only if it has been merged.

---

## 22. Force Delete a Branch

### Command

```bash
git branch -D <branch-name>
```

### Example

```bash
git branch -D feature-login
```

### Explanation

Deletes a branch even if it contains unmerged changes.

### Warning

May result in data loss.

---

## 23. View Changes Between Working Directory and Staging Area

### Command

```bash
git diff
```

### Explanation

Shows line-by-line differences between modified files and the last commit.

---

## 24. Merge Branches

### Command

```bash
git merge <branch-name>
```

### Example

```bash
git merge feature-login
```

### Explanation

Combines changes from the specified branch into the current branch.

### Example Workflow

```bash
git switch main
git merge feature-login
```

### Result

Changes from the feature branch become part of the current branch.

---

# Basic Git Workflow

```bash
git init

git config --global --user.name "Kishor Ahire"
git config --global --user.email "awskynet@gmail.com"

git status

git add .

git commit -m "Initial Commit"

git branch -m main

git switch -c feature-login

git add .

git commit -m "Added Login Feature"

git switch main

git merge feature-login

git log --oneline
```

---

# Useful Git Log Commands

```bash
git log
git log --oneline
git log -n 5
git log --pretty=%s
```

---

# Useful Branch Commands

```bash
git branch
git switch main
git switch -c dev
git checkout -b testing
git branch -d testing
git branch -D testing
```
