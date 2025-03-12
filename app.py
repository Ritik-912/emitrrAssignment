import streamlit as st
from gradio_client import Client
from json import dumps
from spacy import load
nlp = load("en_core_sci_lg")

# Import prompt generation functions from PROMPT_GENERATE.py
from PROMPT_GENERATE import summary_prompt, sentiment_prompt, soap_prompt

def trim_string_to_braces(input_string):
  """
  Trims a string from both sides, keeping only the content from the
  first '{' to the last '}' inclusive.

  Args:
    input_string: The string to trim.

  Returns:
    The trimmed string, or the original string if '{' and '}' are not found
    in the correct order or both are not present.
  """
  start_brace_index = input_string.find('{')
  end_brace_index = input_string.rfind('}')

  if start_brace_index != -1 and end_brace_index != -1 and start_brace_index <= end_brace_index:
    return input_string[start_brace_index : end_brace_index + 1]
  else:
    return input_string

# Set up the Streamlit page
st.set_page_config(page_title="Physician Notetaker", layout="wide")
st.title("🩺 Physician Notetaker")
st.write("Upload a transcript or paste the text of a patient conversation, and get structured outputs for:")
st.markdown("""
- **Medical NLP Summarization** (extracts symptoms, treatments, diagnosis, prognosis, etc.)
- **Sentiment & Intent Analysis** (classifies patient sentiment and intent)
- **SOAP Note Generation** (creates a structured SOAP note)
""")

# Initialize session state variables if not already set
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
if "outputs" not in st.session_state:
    st.session_state.outputs = {"summary": None, "sentiment": None, "soap": None}

# Reset button to clear session state
def reset_app():
    st.session_state.transcript = ""
    st.session_state.outputs = {"summary": None, "sentiment": None, "soap": None}

if st.button("Reset"):
    reset_app()

# Input selection: Text box or file upload
input_method = st.radio("Select Input Method:", ("Text Input", "Upload Text File"))
transcript_text = ""

if input_method == "Text Input":
    transcript_text = st.text_area("Enter Transcript", height=200)
elif input_method == "Upload Text File":
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    if uploaded_file is not None:
        transcript_text = uploaded_file.read().decode("utf-8")
        st.text_area("Transcript", transcript_text, height=200)

if transcript_text and (st.session_state.outputs["summary"] is None or st.session_state.outputs["sentiment"] is None or st.session_state.outputs["soap"] is None):
    if st.button("Process Transcript"):
        # Initialize the Gradio client (adjust the endpoint as needed)
        client = Client("deelf/DVchatbot")
        entities = ", ".join(ent.text for ent in nlp(transcript_text).ents)
        patient_dialogues = "\n".join(line for line in transcript_text.split('\n') if 'patient' in line.lower())

        # Medical NLP Summarization
        with st.spinner("Processing Medical NLP Summarization..."):
            med_prompt = summary_prompt(entities)
            med_response = trim_string_to_braces(client.predict(user_input=med_prompt, api_name="/chat_interface"))
            st.session_state.outputs["summary"] = med_response
        
        # Sentiment & Intent Analysis
        with st.spinner("Processing Sentiment & Intent Analysis..."):
            sent_prompt_text = sentiment_prompt(patient_dialogues)
            sent_response = trim_string_to_braces(client.predict(user_input=sent_prompt_text, api_name="/chat_interface"))
            st.session_state.outputs["sentiment"] = sent_response
        
        # SOAP Note Generation (Bonus)
        with st.spinner("Processing SOAP Note Generation..."):
            soap_prompt_text = soap_prompt(transcript_text)
            soap_response = trim_string_to_braces(client.predict(user_input=soap_prompt_text, api_name="/chat_interface"))
            st.session_state.outputs["soap"] = soap_response
        
        # Display the outputs
        if st.session_state.outputs["summary"]:
            st.subheader("Medical NLP Summarization Output")
            st.json(med_response)
            st.download_button("Download Medical Summary JSON",
                               dumps(med_response, indent=2),
                               "medical_summary.json",
                               "application/json")
        if st.session_state.outputs["sentiment"]:
            st.subheader("Sentiment & Intent Analysis Output")
            st.json(sent_response)
            st.download_button("Download Sentiment Analysis JSON",
                               dumps(sent_response, indent=2),
                               "sentiment_analysis.json",
                               "application/json")
        if st.session_state.outputs["soap"]:
            st.subheader("SOAP Note Generation Output")
            st.json(soap_response)
            st.download_button("Download SOAP Note JSON",
                               dumps(soap_response, indent=2),
                               "soap_note.json",
                               "application/json")
else:
    st.info("Please enter or upload a transcript to process.")
