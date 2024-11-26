import joblib

# Load the model from the file
loaded_model = joblib.load('model_RF.pkl')

# Function to convert user input to model input
def convert_user_input(gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain):
    gender = 1 if gender.lower() == 'male' else 2
    smoking = 1 if smoking.lower() == 'yes' else 0
    yellow_fingers = 1 if yellow_fingers.lower() == 'yes' else 0
    anxiety = 1 if anxiety.lower() == 'yes' else 0
    peer_pressure = 1 if peer_pressure.lower() == 'yes' else 0
    chronic_disease = 1 if chronic_disease.lower() == 'yes' else 0
    fatigue = 1 if fatigue.lower() == 'yes' else 0
    allergy = 1 if allergy.lower() == 'yes' else 0
    wheezing = 1 if wheezing.lower() == 'yes' else 0
    alcohol_consuming = 1 if alcohol_consuming.lower() == 'yes' else 0
    coughing = 1 if coughing.lower() == 'yes' else 0
    shortness_of_breath = 1 if shortness_of_breath.lower() == 'yes' else 0
    swallowing_difficulty = 1 if swallowing_difficulty.lower() == 'yes' else 0
    chest_pain = 1 if chest_pain.lower() == 'yes' else 0

    return [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

# Function to predict lung cancer based on user input
def predict_lung_cancer(user_input):
    # Assuming user_input is a list of feature values
    prediction = loaded_model.predict([user_input])
    print(prediction
          )
    return "You have Lung Cancer" if prediction[0] == 1 else "You don't have Lung Cancer"

# Get user input dynamically
def get_user_input():
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))
    smoking = input("Do you smoke? (yes/no): ")
    yellow_fingers = input("Do you have yellow fingers? (yes/no): ")
    anxiety = input("Do you have anxiety? (yes/no): ")
    peer_pressure = input("Do you experience peer pressure? (yes/no): ")
    chronic_disease = input("Do you have a chronic disease? (yes/no): ")
    fatigue = input("Do you experience fatigue? (yes/no): ")
    allergy = input("Do you have allergies? (yes/no): ")
    wheezing = input("Do you wheeze? (yes/no): ")
    alcohol_consuming = input("Do you consume alcohol? (yes/no): ")
    coughing = input("Do you cough? (yes/no): ")
    shortness_of_breath = input("Do you have shortness of breath? (yes/no): ")
    swallowing_difficulty = input("Do you have difficulty swallowing? (yes/no): ")
    chest_pain = input("Do you have chest pain? (yes/no): ")

    return convert_user_input(
        gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain
    )

# Get user input
user_input = get_user_input()

# Make prediction
result = predict_lung_cancer(user_input)
print(result)
