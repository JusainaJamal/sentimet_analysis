import streamlit as st
import pandas as pd
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import pickle

# Load the pickled model
with open('best_model.pkl', 'rb') as f:
   model = pickle.load(f)

# Initialize the tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased', do_lower_case=True)

# Function to predict rating for a given text
def predict_rating(text):
    encoding = tokenizer.encode_plus(text, padding=True, truncation=True, max_length=128, return_tensors='pt')
    input_ids = encoding['input_ids']
    attention_mask = encoding['attention_mask']

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_rating = torch.argmax(logits, dim=1)

    return predicted_rating.item()

# Streamlit UI
st.title("Sentiment Analysis on Amazon Reviews")
text_input = st.text_area("Enter your review here:")
if st.button("Predict Rating"):
    if text_input:
        predicted_rating = predict_rating(text_input)
        st.write(f"Predicted Rating: {predicted_rating}")
        if predicted_rating == 4:
            st.write("Really positive review")
        elif predicted_rating == 3:
            st.write("Positive review")
        elif predicted_rating == 2:
            st.write("Neutral review")
        elif predicted_rating == 1:
            st.write("Negative review")
        elif predicted_rating == 0:
            st.write("Really negative review")
    else:
        st.warning("Please enter a review before predicting.")

st.markdown("---")
st.write("About")
st.write("This Streamlit app uses a fine-tuned DistilBERT model to predict the sentiment (rating) of Amazon reviews.")
