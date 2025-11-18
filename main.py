from dotenv import load_dotenv
load_dotenv()
import os
import numpy as np
import soundfile as sf
from crewai import Agent, Task, Crew, LLM


def extract_basic_features(audio_path):
    audio, sr = sf.read(audio_path)
    volume=float(np.mean(np.abs(audio)))
    zero_cross=float(np.mean(np.diff(np.sign(audio))!=0))
    pitch=float(np.mean(np.abs(np.fft.fft(audio)[:800])))
    return {"volume":volume,"pitch":pitch,"zero_cross":zero_cross}

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)


feature_agent=Agent(
    role="Audio Feature Interpreter",
    goal="Interpret acoustic features safely.",
    backstory="Expert in sound pattern interpretation.",
    llm=llm
)

expert_agent=Agent(
    role="Baby Cry Expert",
    goal="Give safe non-medical baby cry interpretation.",
    backstory="Understands typical baby cues.",
    llm=llm
)

def process_baby_sound(path):
    features=extract_basic_features(path)

    task1=Task(
        agent=feature_agent,
        description=f"Interpret baby sound features: {features}",
        expected_output="Human-friendly meaning of sound."
    )

    task2=Task(
        agent=expert_agent,
        description="Classify cry & give safe soothing suggestions.",
        expected_output="Caregiver-friendly guidance."
    )

    crew=Crew(agents=[feature_agent,expert_agent],tasks=[task1,task2])
    return crew.kickoff()
