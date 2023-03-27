import pickle
import numpy as np
import streamlit as st
# Load the saved model from the pickle file and do predictions on the new dataset
loaded_model = pickle.load(open("C:/Users/Hp/Desktop/deployment/fifamodeltrained.pkl","rb"))

# Function to predict the rating

def player_rating(input_data):
    
    input_data_numpy_array = np.array(input_data, dtype=object)
    input_data_reshaped = input_data_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    
    return prediction[0]



def main():
    st.title("Player Rating Prediction Application")

    #Get the player features input from the user
    potential = st.number_input("Enter the player' potential score(?/100)", min_value=0, max_value=100) 
    value_eur = st.number_input("Enter the Player's Value in Euros", min_value=0.00)
    wage_eur = st.number_input("Enter the Player's Monthly Wage in Euro", min_value=0.00)
    passing = st.number_input("Enter the Player's Passing Score(?/100)", min_value=0, max_value=100)  
    physic = st.number_input("Enter the Player's Physic Score(?/100)", min_value=0, max_value=100)
    dribbling = st.number_input("Enter the Player's Dribbling Score(? /100)", min_value=0, max_value=100)
    Mentality  = st.number_input("Enter the   Player's Mentality Score(? /100)", min_value=0, max_value=100)
    lcm  = st.number_input("Enter the Player's Last Championships Score(? /100)", min_value=0, max_value=100)
    cm = st.number_input("Enter the Player's Center Midfield Score(? /100)", min_value=0, max_value=100)
    rcm = st.number_input("Enter the Player's Right Center Midfield Score(? /100)", min_value=0, max_value=100)
    
    rating = ""
    
    if st.button("Predict Player Rating"):
        rating = player_rating([potential, value_eur, wage_eur, passing,physic, dribbling, Mentality, lcm, cm, rcm])
    
    st.success(rating)

if __name__ == '__main__':
    main()
    
    
    
    

    