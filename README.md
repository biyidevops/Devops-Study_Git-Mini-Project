# DevOps CI Starter Project
# test action
📦 devops-ci-starter

A simple Python project used to demonstrate real DevOps workflows (Git, CI, Testing, Linting, Branching, Releases).

🚀 Project Overview

This project is part of a structured DevOps learning path.
It demonstrates how to:

Structure a Python application

Write automated unit tests (pytest)

Enforce code quality with flake8

Build a CI pipeline using GitHub Actions

Follow git branching workflows

Create tagged releases (semantic versioning)

Prepare the application for Docker and infra automation

🗂 Project Structure
devops-ci-starter/
│
├── src/
│   ├── app.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/
│   └── test_app.py
│
├── config/
│   ├── dev.env
│   └── prod.env
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── README.md
└── pytest.ini

🧪 Running Tests

To run tests locally:

pytest -vv


Run tests and show print/log output:

pytest -s -vv

✔️ Linting with flake8

To check code quality:

flake8 src

🔄 Continuous Integration (GitHub Actions)

Every push or pull request triggers:

Code checkout

Python setup

flake8 linting

pytest execution

Workflow file:
.github/workflows/ci.yml

🌿 Git Workflow

The project uses a simple GitFlow approach:

main → stable release branch

dev → integration branch

feature/* → new work

Pull requests are required to merge into main or dev

CI validates every PR.

🏷 Versioning (Releases)

Releases follow Semantic Versioning:
vMAJOR.MINOR.PATCH

Create a release tag:

git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0

🐳 Docker Support (coming in Step 9)

A Dockerfile will be added to:

package the app

prepare for deployment

run in CI/CD pipelines

👤 Author

Emmanuel Oluwabiyi Anifowoshe
DevOps Engineering Practice Project
