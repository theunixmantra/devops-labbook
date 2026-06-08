# Git Reset Practice Exercise

## Objective

Practice using different types of Git reset operations:

- `git reset --soft`
- `git reset --mixed` (default)
- `git reset --hard`

Understand how each reset mode affects:

- Commit history
- Staging area (Index)
- Working directory

---

## Prerequisites

Students should be familiar with:

- Creating commits
- Viewing commit history
- Staging files
- Basic Git commands (`git add`, `git commit`, `git status`, `git log`)

---

## Scenario

You are working on a project called **student-portal**. During development, several commits were made, but some changes need to be undone.

Your task is to use different reset commands to manipulate the commit history while observing their effects.

---

## Part 1: Setup

1. Create a new Git repository.
2. Create a file named `notes.txt`.
3. Make the following commits:

| Commit | Change |
|----------|---------|
| Commit 1 | Add project title |
| Commit 2 | Add login feature notes |
| Commit 3 | Add dashboard feature notes |
| Commit 4 | Add profile feature notes |

4. Verify that four commits exist in the repository.

---

## Part 2: Soft Reset

1. View the commit history.
2. Move the branch pointer back by one commit using a **soft reset**.
3. Observe:
   - Current commit history
   - Status of the staging area
   - Contents of `notes.txt`

### Questions

1. How many commits are visible now?
2. Are the changes from the removed commit still available?
3. Are those changes staged or unstaged?

---

## Part 3: Mixed Reset

1. Restore the repository to the original state if necessary.
2. Perform a reset that removes the latest commit and unstages its changes.
3. Check:
   - Commit history
   - Git status
   - File contents

### Questions

1. Did the changes disappear from the file?
2. Are the changes staged?
3. What is the difference compared to the soft reset?

---

## Part 4: Hard Reset

1. Restore the repository to the original state if necessary.
2. Perform a reset that completely removes the latest commit and its associated changes.
3. Verify:
   - Commit history
   - Working directory
   - File contents

### Questions

1. Are the changes from the removed commit still present?
2. What happened to the working directory?
3. What makes this reset potentially dangerous?

---

## Part 5: Compare Reset Modes

Complete the table below.

| Reset Type | Commit Removed | Changes Kept | Changes Staged | Working Directory Modified |
|------------|----------------|--------------|----------------|----------------------------|
| Soft | | | | |
| Mixed | | | | |
| Hard | | | | |

---

## Challenge Exercise

A developer accidentally committed:

- Temporary debug logs
- Test data
- Unfinished code

The commit has not yet been pushed to a remote repository.

For each scenario below, identify which reset mode should be used and explain why:

1. Keep all changes staged for recommitting.
2. Keep changes but unstage them.
3. Completely discard the changes.

---

## Bonus Challenge

1. Create five commits.
2. Move back three commits using a reset command.
3. Determine:
   - Which commits remain visible in the log.
   - Whether the removed changes still exist.
   - Which reset mode was used.

Document your observations.

