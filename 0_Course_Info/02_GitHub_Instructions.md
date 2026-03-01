# DSS 740: Analytics with Machine Learning

## Spring 2026: GitHub Instructions

**Repository Instructions**

This repository is the official distribution source for course materials. You will:

1. Clone it once
2. Pull updates weekly
3. Work only on your own branch
4. Submit assignments via Canvas

When working on course project, you will:

1. Create one repository per team and clone it
2. Create branch for each team member
3. Work on your respective branches and push changes to GitHub
4. Pull updates frequently to ensure everyone is working on the most updated codebase

---

**1. Clone the Repository**

Open Visual Studio

![1772114890801.png](./images/1772114890801.png)

Click on <code>Clone Git Repository</code>

![1772114990767.png](./images/1772114990767.png)

Paste the [Git Repository URL](https://github.com/sidchakravarty/sju_dss740_spring2026.git) for this course

![1772115080495.png](./images/1772115080495.png)

Navigate to a **local** folder on your computer. This is where you will set up your project.

![1772116073822.png](./images/1772116073822.png)

Click Open

![1772116187364.png](./images/1772116187364.png)

Indicate that the contents of this folder are trustworthy.

![1772116284304.png](./images/1772116284304.png)

After this, the project files and folders will appear in the Project Explorer.

![1772116388012.png](./images/1772116388012.png)

---

**2. Pull updates weekly**

Step 1 - Open VSCode Terminal

![1772116652185.png](./images/1772116652185.png)

Step 2 - Select Command Prompt from the drop down.

![1772116934921.png](./images/1772116934921.png)

Step 3 - Let's see the status of git and the branch we are on. We can see that we are in the branch and a lot of files are currently untracked.

```python
git init
git status
```

![1772381327987.png](./images/1772381327987.png)

We can see ⬇️: the active branch in a couple of other places in VSCode, starting with the status bar.

![1772383531678.png](./images/1772383531678.png)

Step 4 - Create a new local branch

```python
git checkout -b feature/data_preprocessing
```

We can see ⬇️ that the branch has changed.

![1772383718533.png](./images/1772383718533.png)

It is recommended to create separate branches so your work is isolated.

![1772383956122.png](./images/1772383956122.png)

Step 5 -
