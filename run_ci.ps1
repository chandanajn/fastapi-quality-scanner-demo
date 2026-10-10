$ErrorActionPreference = "Continue"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     Running Local CI Pipeline          " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`n[1/6] Running Flake8 (Syntax & Style Linter)..." -ForegroundColor Yellow
python -m flake8 app tests

Write-Host "`n[2/6] Running Pylint (Code Quality)..." -ForegroundColor Yellow
python -m pylint app tests

Write-Host "`n[3/6] Running Mypy (Static Type Checker)..." -ForegroundColor Yellow
python -m mypy app tests

Write-Host "`n[4/6] Running Bandit (Security Vulnerability Scanner)..." -ForegroundColor Yellow
python -m bandit -r app tests

Write-Host "`n[5/6] Running detect-secrets (Secret & API Key Scanner)..." -ForegroundColor Yellow
python -m detect_secrets scan app tests

Write-Host "`n[6/6] Running pip-audit (Dependency Vulnerabilities)..." -ForegroundColor Yellow
python -m pip_audit -r requirements.txt

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Local CI Script Completed." -ForegroundColor Cyan
Write-Host "Note: SonarQube and Docker/Trivy steps were omitted as they require external setup." -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan
