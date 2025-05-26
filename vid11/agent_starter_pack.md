# Overview

1. Demo project
2. Introduce Gemini Multimodal Live API
3. Introduce agent-starter-pack
4. Explain codebase
5. Explain CICD on GitHub + Cloud Build
6. Explain other deployment components: Cloud Run, Observability, Big Query

## 1. Demo project

- In Cloud Shell Editor:

```
agent-starter-pack create my-awesome-agent

cd my-awesome-agent && make install

make ui

make local-backend
```

- Change preview to port 8000

- Go to `http://localhost:8501`

- Input `https://8000-cs-f62da62b-135d-4d90-ae13-a71994e618df.cs-asia-southeast1-yelo.cloudshell.dev/` to Server URL

- Interact with Agent

## 2. Introduce Gemini Multimodel Live API

[Gemini Multimodal Live API](https://googleapis.github.io/python-genai/genai.html#module-genai.live)

[Demo Notebook](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/multimodal-live-api/intro_multimodal_live_api_genai_sdk.ipynb)

## 3. Introduce agent-starter-pack

[agent-starter-pack GitHub](https://github.com/GoogleCloudPlatform/agent-starter-pack)

[agent-starter-pack Documentation](https://googlecloudplatform.github.io/agent-starter-pack/)

## 4. Explain codebase

[GitHub repo linked to GCP Cloud Build](https://github.com/nhamhung/1)

```
- Makefile
- Dockerfile
- app/
- deployment/
- frontend/
- tests/
```

## 5. Explain CICD on GitHub + Cloud Build

- Prepare STG, PROD and CICD projects

- Set up CI/CD

```
cd my-awesome-agent

agent-starter-pack setup-cicd
```

- Select projects and GitHub repo

- Push code

```
git add -A

git config --global user.email "email@example.com"

git config --global user.name "username"

git commit -m "init"

git push --set-upstream origin main
```

- Check Cloud Build

- Make PR

## 6. Explain other deployment components: Cloud Run, Observability, BigQuery

- Use STG / PROD Server URL from Cloud Run

- View Cloud Logging

- View BigQuery tables
