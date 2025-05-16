# Overview

1. Introduce Google GenAI repo
2. Introduce Gemini getting-started notebooks and GenAI SDK
3. Introduce Gemini sample-apps repo and Streamlit + Cloud Run
4. Introduce Cloud Shell Editor and run streamlit locally
5. Deploy streamlit on Cloud Run

## 1. Introduce Google GenAI repo

[Google GenAI Repo](https://github.com/GoogleCloudPlatform/generative-ai/tree/main)

## 2. Introduce Gemini getting-started notebooks and GenAI SDK

[Getting-started](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/getting-started)

[Python Google GenAI SDK](https://googleapis.github.io/python-genai/index.html)

## 3. Introduce Gemini sample-apps repo and Streamlit + Cloud Run

[Sample-apps](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/sample-apps)

[Streamlit](https://docs.streamlit.io/)

[Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run)

4. Introduce Cloud Shell Editor and run streamlit locally

- [General set up](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/sample-apps/SETUP.md)

```
gcloud auth list

gcloud config list project

gcloud config set project <PROJECT_ID>

echo $GOOGLE_CLOUD_PROJECT

gcloud services enable cloudbuild.googleapis.com cloudfunctions.googleapis.com run.googleapis.com logging.googleapis.com storage-component.googleapis.com aiplatform.googleapis.com
```

- Repo set up and run locally

```
python3 -m venv gemini-streamlit
source gemini-streamlit/bin/activate
pip install -r requirements.txt

export GOOGLE_CLOUD_PROJECT='<Your Google Cloud Project ID>'
export GOOGLE_CLOUD_REGION='us-central1' # If you change this, make sure the region is supported.

streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

5. Deploy streamlit on Cloud Run

```
export GOOGLE_CLOUD_PROJECT='<Your Google Cloud Project ID>'
export GOOGLE_CLOUD_REGION='us-central1' # If you change this, make sure the region is supported.

export SERVICE_NAME='gemini-streamlit-app' # This is the name of our Application and Cloud Run service. Change it if you'd like.

gcloud run deploy "$SERVICE_NAME" \
  --port=8080 \
  --source=. \
  --allow-unauthenticated \
  --region=$GOOGLE_CLOUD_REGION \
  --project=$GOOGLE_CLOUD_PROJECT \
  --set-env-vars=GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,GOOGLE_CLOUD_REGION=$GOOGLE_CLOUD_REGION
```
