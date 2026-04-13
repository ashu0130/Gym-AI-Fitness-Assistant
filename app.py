import numpy as np
import pickle

model = pickle.load(open("model.pkl","rb"))
pickle.dump(rf, open("model.pkl","wb"))


def recommend_workout(text):
    text = text.lower()
    
    if "fat" in text or "weight loss" in text:
        return "Cardio + HIIT"
    
    elif "muscle" in text or "gain" in text:
        return "Strength Training"
    
    elif "flexibility" in text or "stress" in text:
        return "Yoga"
    
    elif "beginner" in text:
        return "Light Cardio"
    
    else:
        return "General Fitness"

def predict_calories(age, gender, weight, height, duration, frequency, experience, bmi, goal):

    features = np.array([[age, gender, weight, height, duration, frequency, experience, bmi]])
    
    prediction = model.predict(features)
    
    workout = recommend_workout(goal)
    
    return prediction[0], workout

import gradio as gr

interface = gr.Interface(
    fn=predict_calories,
    
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Gender (0 = Female, 1 = Male)"),
        gr.Number(label="Weight (kg)"),
        gr.Number(label="Height (m)"),
        gr.Number(label="Session Duration (hours)"),
        gr.Number(label="Workout Frequency (days/week)"),
        gr.Number(label="Experience Level"),
        gr.Number(label="BMI"),
        gr.Textbox(label="Enter your fitness goal")
    ],
    
    outputs=[
        gr.Number(label="Predicted Calories Burned"),
        gr.Textbox(label="Recommended Workout")
    ],
    
    title="Gym AI Fitness Assistant",
    
    description="Predict calories burned and get AI-based workout recommendation"
)

interface.launch()