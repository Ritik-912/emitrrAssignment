# emitrrAssignment
# Physician Notetaker: Medical Transcription & NLP Pipeline

## Project Overview
The Physician Notetaker project is designed to streamline clinical documentation by leveraging an end-to-end NLP pipeline. It performs the following tasks:
1. **Medical NLP Summarization:**  
   - **NER & Entity Extraction:** Extract key entities such as Symptoms, Treatments, Diagnoses, and Prognoses.
   - **Text Summarization:** Convert a transcribed conversation into a structured medical report.
   - **Keyword Extraction:** Identify important medical phrases (e.g., "whiplash injury", "physiotherapy sessions").
2. **Sentiment & Intent Analysis:**  
   - **Sentiment Classification:** Classify patient sentiment as `Anxious`, `Neutral`, or `Reassured` using a Transformer-based model.
   - **Intent Detection:** Identify the patient's intent (e.g., “Seeking reassurance”, “Reporting symptoms”, “Expressing concern”).
3. **SOAP Note Generation (Bonus):**  
   - Generate a structured SOAP note (Subjective, Objective, Assessment, and Plan) from the conversation transcript.

## Project Structure
- **app.py:**  
  The main Streamlit application that accepts a transcript (via text input or file upload) and displays three JSON outputs:
  - Medical NLP Summarization
  - Sentiment & Intent Analysis
  - SOAP Note Generation
- **PROMPT_GENERATE.py:**  
  Contains functions to generate prompts for each task.
- **\_\_init\_\_.py:**  
  An empty file to mark the project as a Python package.
- **requirements.txt:**  
  Lists all required libraries (e.g., `streamlit`, `transformers`, `gradio_client`, `spacy`, `scispacy`).

## Setup and Running the Application

### Prerequisites
- Python 3.7 or higher
- pip

### Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
Install Dependencies:
```bash
pip install -r requirements.txt
```
Run the Application Locally:
```bash
streamlit run app.py
```
Deployment on Hugging Face Spaces: https://huggingface.co/spaces/ritik22912/emitrrAssignment
## Sample Output Screenshots
![image](https://github.com/user-attachments/assets/71972efa-47a8-4679-bd74-d50bb42d8e5f)
![image](https://github.com/user-attachments/assets/ea29eb53-94dd-49d0-9794-83380a491ec2)
![image](https://github.com/user-attachments/assets/2403be48-587c-46e4-82f0-4a6788a49b87)
![image](https://github.com/user-attachments/assets/d9dce4c7-34e7-4286-8bd3-4d0acae5d9ac)

## Methodologies and Implementation Details
#### Medical NLP Summarization
**Algorithms**
- Named Entity Recognition (NER): Leveraged spaCy with SciSpacy’s en_core_sci_lg model to capture medical entities.
- Heuristics: Custom rules infer missing details (e.g., mapping “car accident” to “Whiplash injury”).
- Keyword Extraction: Used noun chunk extraction via spaCy.
**Reasoning**
- Domain-specific models like SciSpacy are chosen for their biomedical knowledge, ensuring accurate entity extraction and context understanding.
#### Sentiment & Intent Analysis
**Algorithms**
- Transformer-based Models: Employed a fine-tuned BERT or DistilBERT model with two classification heads for sentiment and intent.
- Multi-task Learning: Jointly optimized using cross-entropy loss for both sentiment and intent predictions.
**Reasoning**
- Fine-tuning on healthcare-specific datasets (e.g., MIMIC-III, i2b2) provides robust performance. The multi-task approach efficiently captures both sentiment and intent without requiring separate models.
#### SOAP Note Generation
**Algorithms**
- Prompt-based Summarization: A transformer-based summarization model (e.g., BART or T5) is used to map conversation transcripts into the SOAP note structure.
Rule-based Parsing: Supplemented by heuristics to ensure the output conforms to the Subjective, Objective, Assessment, and Plan sections.
**Reasoning**
- Combining rule-based methods with deep learning ensures that the generated SOAP notes are both clinically structured and linguistically coherent.
### Usage
**Input Transcript**: Paste the transcript in the provided text area or upload a .txt file. If paste the transcript press `ctrl` +  `enter` for enabling process Transcript button.
**Process Transcript**: Click the "Process Transcript" button. The system processes the transcript and displays three outputs.
**Download Outputs**: Each output is available as a downloadable JSON file.
**Reset**: Use the "Reset" button to clear current outputs and input a new transcript.
##### Future Enhancements
- Dataset Expansion: Incorporate larger, real-world clinical datasets.
- Advanced Models: Experiment with models such as ClinicalBERT for improved accuracy.
- Enhanced UI: Additional UI improvements and customization options.
- Evaluation Metrics: Implement metrics (accuracy, F1 score) for performance evaluation.
