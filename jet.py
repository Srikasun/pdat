main.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Sum:", add(5, 3))
test_main.py
from main import add

def test_add():
    assert add(2, 3) == 5
.GitHub/workflows/ci.yml

name: CI/CD Pipeline

on:
  push:
    branches:
      - main
      - master

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Run Tests
        run: pytest -q

      - name: Deploy (Simulated)
        run: echo "Deployment Successful! Application is Live 🚀"

git add .
git commit -m "Added CI/CD pipeline"
git push origin main

