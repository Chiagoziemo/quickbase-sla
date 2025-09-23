**Quickbase CI/CD Pipeline with GitHub Actions**

This section demonstrates how to use GitHub Actions to automate testing and deployment of Python automation scripts that interact with Quickbase.

Overview

The pipeline ensures that every code change is:

1. Tested – Runs unit tests with pytest.

2. Validated – Stops the pipeline if tests fail.

3. Deployed – Executes the Quickbase automation script using secure secrets.


**Pipeline Workflow**
File: .github/workflows/quickbase_pipeline.yml



**Secrets Configuration**

In your repository, go to:
Settings → Secrets and variables → Actions → New repository secret

Add the following secrets:

QB_USER_TOKEN → Quickbase User Token (for API authentication).

QB_REALM → Your Quickbase realm URL (e.g. https://example.quickbase.com).

QB_TABLE_ID → The Quickbase table you are working with.


**Unit Tests**

All Python scripts should have unit tests under a tests/ directory.

Run locally before pushing:

_pytest --maxfail=1 --disable-warnings -q_


**Deployment**

Once tests pass, GitHub Actions will:

1. Inject secrets securely.

2. Run your Quickbase automation script (quickbase_pipeline.py).

3. Confirm successful execution in the GitHub Actions logs.


**Benefits**

Automation: No manual steps needed to deploy.

Security: Secrets stored securely in GitHub.

Reliability: Tests must pass before deployment.
