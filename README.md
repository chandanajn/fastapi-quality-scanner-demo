# FastAPI Quality Scanner Demo

A sample FastAPI application demo with PostgreSQL, SQLAlchemy, and Docker.

## Setup & Run Instructions

### 1. Start Database with Docker Compose
```bash
docker compose up -d
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Application
```bash
uvicorn app.main:app --reload
```

### 4. Access API Documentation
Open your browser at:
http://localhost:8000/docs


python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt



# 1. Run Flake8 (Syntax and Style Linter)
python -m flake8 app tests

# 2. Run Pylint (Code Quality & PEP 8 Scorer)
python -m pylint app tests

# 3. Run Mypy (Static Type Checker)
python -m mypy app tests

# 4. Run Bandit (Security Vulnerability Scanner - SAST)
python -m bandit -r app tests

# 5. Run detect-secrets (Secret & API Key Scanner)
python -m detect_secrets scan app tests

# 6. Run pip-audit (Dependency Vulnerabilities)
python -m pip_audit -r requirements.txt


# Requires sonar-scanner to be installed locally
sonar-scanner.bat -D"sonar.projectKey=your_project_key" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=your_sonar_token"

# Build the Docker image
docker build -t fastapi-app:latest .

# Run Trivy vulnerability scanner on the built image
trivy image --exit-code 1 --ignore-unfixed --vuln-type os,library --severity CRITICAL,HIGH fastapi-app:latest


git add .
git commit -m "Update code"
git push


.\run_ci.ps1



Step 1: Generate the Token in SonarCloud
Go to SonarCloud and log in to your account.
Click on your profile avatar in the top right corner.
Select My Account from the dropdown menu.
Click on the Security tab.
In the Generate Tokens section:
Enter a name for your token (e.g., github-actions-scanner).
Choose the token type (a User Token is perfectly fine).
Click the Generate button.
Copy the token immediately! (It will look like a long string of random characters). Note: SonarCloud will only show this to you once. If you lose it, you will have to generate a new one.
Step 2: Add the Token to GitHub
Now that you have the token copied, you need to save it safely inside your GitHub repository:

Go to your repository on GitHub (chandanajn/fastapi-quality-scanner-demo).
Click on the Settings tab at the top.
On the left sidebar, scroll down to the Security section and click on Secrets and variables, then click Actions.
Click the green New repository secret button.
In the Name field, type exactly: SONAR_TOKEN
In the Secret field, paste the token you copied from SonarCloud.
Click Add secret.
Once that is done, you can push the code update we made earlier:

powershell
git add .
git commit -m "Fix SonarCloud configuration"
git push
Your GitHub Action should now automatically trigger and successfully authenticate with SonarCloud!


