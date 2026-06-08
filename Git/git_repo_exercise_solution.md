# GitHub Basics Exercise

## Objective
Learn the fundamentals of Git and GitHub, including repository creation, branching, committing changes, merging branches, resolving conflicts, and pushing code to GitHub.

---

## Exercise Steps

### 1. Create a Local Repository
Create a new Git repository on your local machine.

```bash
mkdir github-basics
cd github-basics
git init
```

---

### 2. Create a GitHub Repository
Create a new repository on GitHub and give it any name you prefer.

---

### 3. Connect Local Repository to GitHub

Replace `<repository-url>` with your GitHub repository URL.

```bash
git remote add origin <repository-url>
```

Verify the remote:

```bash
git remote -v
```

---

### 4. (Optional) Rename the Default Branch

Rename the default branch from `master` to `main`.

```bash
git branch -M main
```

---

### 5. Create `preferences.txt`

Create a new file named `preferences.txt`.

```bash
touch preferences.txt
```

Leave the file empty.

Stage and commit the file:

```bash
git add preferences.txt
git commit -m "Initial commit with empty preferences file"
```

---

### 6. Push the Main Branch to GitHub

Push the branch to GitHub:

```bash
git push -u origin main
```

Verify that the empty `preferences.txt` file appears in your GitHub repository.

---

### 7. Create Two New Branches

Create branches named `foods` and `movies`.

```bash
git branch foods
git branch movies
```

---

### 8. Update the Foods Branch

Switch to the `foods` branch:

```bash
git checkout foods
```

Add three or more favorite foods to `preferences.txt`.

Example:

```text
Pizza
Biryani
Pasta
```

Stage and commit the changes:

```bash
git add preferences.txt
git commit -m "Add favorite foods"
```

---

### 9. Update the Movies Branch

Switch to the `movies` branch:

```bash
git checkout movies
```

Add three or more favorite movies to `preferences.txt`.

Example:

```text
Interstellar
The Dark Knight
3 Idiots
```

Stage and commit the changes:

```bash
git add preferences.txt
git commit -m "Add favorite movies"
```

---

### 10. Push the Foods Branch

Push the `foods` branch to GitHub:

```bash
git push -u origin foods
```

Verify that the branch is visible on GitHub.

---

### 11. Push the Movies Branch

Push the `movies` branch to GitHub:

```bash
git push -u origin movies
```

Verify that the branch is visible on GitHub.

---

### 12. Merge Branches into Main

Switch to the `main` branch:

```bash
git checkout main
```

Merge the `foods` branch:

```bash
git merge foods
```

Merge the `movies` branch:

```bash
git merge movies
```

#### Handling Merge Conflicts

If a merge conflict occurs:

1. Open `preferences.txt`.
2. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Keep both the foods and movies entries.

Example final content:

```text
Pizza
Biryani
Pasta

Interstellar
The Dark Knight
3 Idiots
```

Stage and commit the resolved file:

```bash
git add preferences.txt
git commit -m "Resolve merge conflict and combine preferences"
```

---

### 13. Push the Updated Main Branch

Push the latest changes to GitHub:

```bash
git push origin main
```

Verify that the updated `preferences.txt` file contains both your favorite foods and favorite movies.

---

## Expected Outcome

You should have:

- A GitHub repository connected to a local Git repository.
- A `main` branch containing the final merged content.
- Two feature branches: `foods` and `movies`.
- Experience creating commits, pushing branches, merging changes, and resolving merge conflicts.
````
