# emitrrAssignment
# Physician Notetaker: Medical Transcription & NLP Pipeline

## Project Overview

The Physician Notetaker project implements an end-to-end NLP pipeline to support clinical documentation by automating three key tasks:

1. **Medical NLP Summarization:**  
   - **NER & Entity Extraction:** Extract key medical entities such as Symptoms, Treatments, Diagnoses, and Prognoses from a transcribed conversation.
   - **Text Summarization:** Convert the transcript into a structured medical report.
   - **Keyword Extraction:** Identify important medical phrases (e.g., "whiplash injury", "physiotherapy sessions").

2. **Sentiment & Intent Analysis:**  
   - **Sentiment Classification:** Use a transformer-based model (e.g., BERT or DistilBERT) to classify patient sentiment as `Anxious`, `Neutral`, or `Reassured`.
   - **Intent Detection:** Identify the patient’s intent (e.g., “Seeking reassurance”, “Reporting symptoms”, “Expressing concern”).

3. **SOAP Note Generation (Bonus):**  
   - Automatically generate a structured SOAP note from a conversation transcript.
   - **SOAP Format:** Includes Subjective, Objective, Assessment, and Plan sections.
  
Each task outputs a structured JSON file with the extracted details.

## Project Structure

- **app.py:**  
  The main Streamlit application for deploying the system on Hugging Face Spaces. It accepts user input (transcript text via text box or file upload) and displays three JSON outputs corresponding to the three tasks.

- **PROMPT_GENERATE.py:**  
  Contains functions that generate the prompts for each task:
  - `summary_prompt(text: str)`: Generates a prompt for Medical NLP Summarization.
  - `sentiment_prompt(text: str)`: Generates a prompt for Sentiment & Intent Analysis.
  - `soap_prompt(text: str)`: Generates a prompt for SOAP Note Generation.

- **__init__.py:**  
  An empty file that makes this directory a Python package.

- **requirements.txt:**  
  Lists all the required libraries (e.g., `streamlit`, `transformers`, `gradio_client`, `spacy`, `scispacy`, etc.)

## Setup and Deployment

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ritik-912/emitrrAssignment
   cd emitrrAssignment
   ```
Install Dependencies: Ensure you have Python 3.7+ installed, then run:
```bash
pip install -r requirements.txt
```
Run Locally: Start the Streamlit app locally:
```bash
streamlit run app.py
```
Deployed on Hugging Face Spaces: https://huggingface.co/spaces/ritik22912/emitrrAssignment

How It Works
Input: Users can either paste a transcript into a text area or upload a text file containing the transcript.

Processing:
Upon clicking "Process Transcript," the app:
> Generates prompts for the three tasks using functions from PROMPT_GENERATE.py.
> Sends each prompt to a Hugging Face endpoint via a Gradio Client.
> Receives and displays three structured JSON outputs.
Output:
The app provides:
> Medical NLP Summarization JSON: Contains extracted patient name, symptoms, treatments, diagnosis, current status, and prognosis.
> Sentiment & Intent Analysis JSON: Contains the patient sentiment and intent.
> SOAP Note JSON: Contains the SOAP note sections (Subjective, Objective, Assessment, and Plan).
Assignment Questions and Answers
1. Medical NLP Summarization
**How would you handle ambiguous or missing medical data in the transcript?**
Ambiguities or missing data are addressed by applying heuristic rules and fallback defaults. For example, if a symptom is implied but not clearly mentioned, the system can insert a default value or mark it as "Not Specified." Advanced techniques might include uncertainty detection and using domain-specific language models to infer missing context.

**What pre-trained NLP models would you use for medical summarization?**
Domain-specific models such as SciSpacy's en_core_sci_lg, BioBERT, or ClinicalBERT are recommended because they are pre-trained on biomedical literature and clinical notes, providing better performance on medical text.

2. Sentiment & Intent Analysis
**How would you fine-tune BERT for medical sentiment detection?**
Fine-tuning involves:
Initializing BERT (or a variant like BioBERT/ClinicalBERT) with domain-specific weights.
Adding two classification heads on top of the pooled output: one for sentiment classification and one for intent detection.
Training the model with a multi-task objective using cross-entropy loss on annotated clinical dialogue datasets.
**What datasets would you use for training a healthcare-specific sentiment model?**
Suitable datasets include:
- MIMIC-III clinical notes (with appropriate access permissions)
- i2b2 clinical NLP challenge datasets
- SMM4H/CADEC datasets for social media-based clinical data
Additionally, custom annotated datasets from patient feedback or clinical surveys can be leveraged.
3. SOAP Note Generation (Bonus)
**How would you train an NLP model to map medical transcripts into SOAP format?**
The approach includes:
Using a combination of rule-based parsing and transformer-based text summarization.
Annotating a corpus of medical transcripts with corresponding SOAP note sections.
Fine-tuning a summarization model (e.g., BART, T5) on this annotated data to learn the mapping from transcript to structured SOAP notes.
**What rule-based or deep-learning techniques would improve the accuracy of SOAP note generation?**
Techniques include:
Rule-based Approaches: Developing custom regular expressions and heuristics to detect conversation segments corresponding to each SOAP section.
Deep Learning Approaches: Leveraging transformer models (like BERT, BART, or T5) fine-tuned on a large annotated corpus. Hybrid methods combining rule-based extraction with deep learning models can yield higher accuracy by balancing interpretability and model flexibility.

Usage
Input the Transcript:
Either paste the conversation transcript in the text area or upload a .txt file.
Process Transcript:
Click the "Process Transcript" button to generate results.

View and Download Results:
The application will display three JSON outputs for:
###### Medical NLP Summarization
###### Sentiment & Intent Analysis
###### SOAP Note Generation
Use the download buttons to save the JSON files locally.
#### Future Enhancements
> Dataset Expansion: Integrate larger, real-world clinical datasets to improve model accuracy.
> Advanced Models: Experiment with other domain-specific models like ClinicalBERT or SciSpacy.
> User Interface: Enhance the UI with additional options for customizations and error handling.
> Evaluation Metrics: Incorporate evaluation metrics (accuracy, F1 score) to validate model performance.

#### Acknowledgements
> Hugging Face: For their transformers and spaces frameworks.
> spaCy & SciSpacy: For their powerful NLP models and pipelines.
> Clinical Data Providers: Whose datasets and challenges inspire continued research in medical NLP.
