from fastapi import APIRouter, UploadFile, File
import spacy

router = APIRouter()

nlp = spacy.load("en_core_web_sm")  # Ensure you have this model installed

def parse_resume(text: str):
    doc = nlp(text)
    # A very simple extraction: get nouns as skills keywords
    keywords = [token.text for token in doc if token.pos_ == "NOUN"]
    return keywords

@router.post("/")
def analyze_resume(file: UploadFile = File(...)):
    contents = file.file.read().decode("utf-8")
    keywords = parse_resume(contents)
    
    # For demonstration, a simple match:
    matched_roles = []
    if "python" in [k.lower() for k in keywords]:
        matched_roles.append("Data Scientist")
    if "machine" in [k.lower() for k in keywords] and "learning" in [k.lower() for k in keywords]:
        matched_roles.append("ML Engineer")
    
    return {"filename": file.filename, "matched_roles": matched_roles}
