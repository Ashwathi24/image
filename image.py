import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs":st.text_input('ENTER PROMPT:'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('GENERATE'):
	st.image(image)