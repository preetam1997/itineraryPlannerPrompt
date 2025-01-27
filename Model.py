
import google.generativeai as genai
from google.api_core import retry
from IPython.display import HTML, Markdown, display
import streamlit as st



def get_model(temperature, top_p, max_output_token, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config=genai.GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_output_token,
        ))


    retry_policy = {
        "retry": retry.Retry(predicate=retry.if_transient_error, initial=10, multiplier=1.5, timeout=300)
    }

    return model