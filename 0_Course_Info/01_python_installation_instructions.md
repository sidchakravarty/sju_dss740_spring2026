# DSS 740: Analytics with Machine Learning

## Spring 2026: Install Python

### 🐍: Install Python (Windows, macOS, and Linux)

1️⃣Windows Installation

Step 1 - Download Python

1. Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click Download Python 3.1x.x
3. Run the installer

⚠️Important (Do NOT skip)

On the first installation screen:

- [X] Check: Add Python to PATH
  Then click **Install Now**

Step 2 - Verify Installation

```python
python --version
```

If you see something like this ⬇️, you are fine. If not, follow the instructions provided in ==05_python_installation_instructions.md==.

![1772117088445.png](./images/1772117088445.png)

Check if pip is installed

```python
pip --version
```

or

```python
python -m pip --version
```

You should see something like this ⬇️. pip is a python package manager. It gets installed automatically with Python.

![1772117869934.png](./images/1772117869934.png)

2️⃣ macOS Installation

Step 1 - Install Homebrew (if not already installed)

```python
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Step 2 - Install Python

```python
brew install python@3.11
```

Step 3 - Verify Installation

```python
python3 --version
pip3 --version
```

3️⃣Linux (Ubuntu)

Most Linux systems already include Python, but we want to install 3.1x.x + version

Step 1 - Update system and Install Python

```python
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip -y
```

Step 2 -Verify Installation

```python
python3 --version
pip3 --version
```

---

### Install VS Code

Step 1 - Download from [code.visualstudio.com](https://code.visualstudio.com/)

Step 2 - After installation, open VS Code and click on **Extensions icon**

![1772370023340.png](./images/1772370023340.png)

Type Python in the search bar and then Install **Python Extension** by Microsoft

![1772370152561.png](./images/1772370152561.png)

Step 3 - Restart VS Code

Step 4 - Verify Installation

Open VSCode Terminal

![1772116652185.png](./images/1772116652185.png)

Select Command Prompt from the drop down.

![1772116934921.png](./images/1772116934921.png)

Type the following commands in the terminal to verify installation is complete.

![1772370303221.png](./images/1772370303221.png)
