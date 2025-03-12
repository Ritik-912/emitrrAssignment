"""
Functions to return prompts for the 3 tasks of Assignments.
"""
def summary_prompt(text: str = '') -> str:
    return """Task: Extract medical details from the follwing extracted entities from transcribed conversation.
Entities to extract: Symptoms, Treatments, Diagnoses, Prognoses.
Identify important medical phrases (e.g., "whiplash injury," "physiotherapy sessions").
Extracted entities:
{}
Convert the transcript into a structured medical report and Format the output as a JSON object as below:
{{
    "Patient_Name": "",
    "Symptoms": [],
    "Treatments": [],
    "Diagnosis": "",
    "Current_Status": "",
    "Prognosis": ""
}}
NOTE: Fill all the relevant accurate values from the transcribed conversation in above JSON object format and return only the filled object. You can add more relvant key-value pairs.
    """.format(text)

def sentiment_prompt(text: str = '') -> str:
    return """You are a medical NLP system tasked with analyzing patient dialogues. Your objective is twofold:

1. **Sentiment Classification:** Classify the patient's sentiment as one of the following:
   - "Anxious"
   - "Neutral"
   - "Reassured"

2. **Intent Detection:** Identify the patient’s intent as one of the following:
   - "Seeking reassurance"
   - "Reporting symptoms"
   - "Expressing concern"

Given the patient dialogues, extract the sentiment and intent and provide your output as a JSON object with the keys "Sentiment" and "Intent" commutatively for all dialogues. Don't give any extra explaination just the expected output.

Patient Dialogue:
{}

Expected Output:
{{
  "Sentiment": "",
  "Intent": ""
}}
""".format(text)

def soap_prompt(text: str = '') -> str:
    return '''You are a medical documentation assistant. Your task is to convert a given conversation transcript into a structured SOAP note in JSON format. The SOAP note must include the following sections with the specified keys:

{{
  "Subjective": {{
    "Chief_Complaint": "<brief description of the patient's main complaint>",
    "History_of_Present_Illness": "<detailed description of the patient's current symptoms and history>"
  }},
  "Objective": {{
    "Physical_Exam": "<summary of physical exam findings>",
    "Observations": "<any additional observations about the patient’s condition>"
  }},
  "Assessment": {{
    "Diagnosis": "<medical diagnosis based on the conversation>",
    "Severity": "<severity of the condition>"
  }},
  "Plan": {{
    "Treatment": "<treatment plan including medications or therapies>",
    "Follow-Up": "<recommendations for follow-up care>"
  }}
}}

Using the transcript below, generate the SOAP note. Your output must be exactly in valid JSON format with the keys and structure as shown. Don't give any extra explaination just the json string of expected output.
{}
'''.format(text)
