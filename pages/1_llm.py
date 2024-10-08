import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

# generate embedding
def get_embedding(input, model = 'text-embedding-3-small'):
    response = client.embeddings.create(
        input = input,
        model = model
    )
    return [x.embedding for x in response.data]

# helper function for calling LLM
def get_completion(prompt, model = "gpt-4o-mini", temperature = 0, top_p = 1.0, max_tokens = 1024, n = 1, json_output = False):
    # used to force output as json if specified
    if json_output == True:
      output_json_structure = {"type": "json_object"}
    else:
      output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(  # originally was openai.chat.completions
        model = model,
        messages = messages,
        temperature = temperature,
        top_p = top_p,
        max_tokens = max_tokens,
        n = 1,
        response_format = output_json_structure,
    )
    return response.choices[0].message.content

