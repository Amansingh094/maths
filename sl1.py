import streamlit as st
# Header
st.header("Mathematics for us")
st.subheader("Hi,this website is devloped by Aman Singh and Saurav BABA of class 12th.We have created this website to help students and teachers make learning easier.")
st.title("Fluid Mechanics")
# Inputs
weight = st.number_input("Enter weight (in grams/kilograms):")
volume = st.number_input("Enter volume (in ml/l):")
# Options
unit_option = st.multiselect("Select output unit:", ["SI", "CGS", "Both"], default=["SI"])
fluid_option = st.checkbox("Use custom fluid density")
if fluid_option:
    fluid_density = st.number_input("Enter fluid density (in kg/m^3):")
else:
    fluid_density = 997 # Default water density
# Calculation
volume = volume/1000 # Convert ml to liters
if "SI" in unit_option or "Both" in unit_option:
    upthrust_si: float = (weight/1000) - (fluid_density*volume)
    st.write(f"Upthrust (SI unit): {upthrust_si} N")
if "CGS" in unit_option or "Both" in unit_option:
    upthrust_cgs = upthrust_si*1000
    st.write(f"Upthrust (CGS unit): {upthrust_cgs} dyne")
# Buoyancy
upthrust = fluid_density*volume*9.81 # 9.81 is the acceleration due to gravity
st.write(f"Buoyancy: {upthrust} N")
st.write("[know more>](http://fma.if.usp.br/~eabdalla/exacta/000m1.pdf)")
# Cheatsheet
with st.container():
    st.write("----")
    st.header("Cheat Sheet")
    image_col, text_col = st.columns((1,1))
    with image_col:
           # add image here
     with text_col:
        st.subheader("physics cheatsheet class 11th")
        st.markdown("[download pdf](https://www.resonance.ac.in/sc/post/attachment/(2232)-gyan-sutra-p.pdf)")
        st.subheader("Differentiation")
        st.markdown("[Download PDF](https://dgtstudy.com/media/media/study_material/2020-04-06/DGT_Differentiation.pdf)")
        st.subheader("intigration")
        st.markdown("[download pdf](https://ncert.nic.in/ncerts/l/lemh201.pdf)")
        st.subheader("slop of line")
        st.markdown("[download pdf](https://www.dunkirkcsd.org/cms/lib/NY19000564/Centricity/Domain/13/slope%20of%20a%20line%20notes.pdf)")
        st.subheader("trigonometric ratios")
        st.markdown("[download pdf](https://tutorial.math.lamar.edu/pdf/trig_cheat_sheet.pdf)")
        st.subheader("graph")
        st.markdown("[download pdf](file:///C:/Users/Avinash/Downloads/functions-and-graphs.pdf)")
        st.subheader("maxima minima value function")
        st.markdown("[download pdf](file:///C:/Users/Avinash/Downloads/functions-and-graphs.pdf)")
#qiez






import streamlit as st
import random

# Define a dictionary of quiz questions with their corresponding answers
quiz_questions = {
    "What is the capital of France?": ["Paris", "Rome", "Madrid", "Berlin"],
    "What is the highest mountain in the world?": ["Mount Everest", "K2", "Makalu", "Cho Oyu"],
    "What is the largest animal in the world?": ["Blue whale", "Elephant", "Giraffe", "Hippopotamus"]
}

# Define a function to display the quiz
def quiz():
    # Loop through each question in the quiz_questions dictionary
    for question, options in quiz_questions.items():
        # Display the question
        st.write(question)
        # Shuffle the answer options to prevent the correct answer from being pre-selected
        random.shuffle(options)
        # Display the answer options as radio buttons
        selected_option = st.radio("", options, key=question)
        # Check if an option has been selected
        if selected_option:
            # Check if the selected answer is correct
            if selected_option == options[0]:
                st.write("Correct!")
            else:
                st.write("Sorry, that's incorrect.")

# Define a function to create a new quiz question
def create_question():
    # Get the question and answer options from the user
    question = st.text_input("Enter the quiz question:")
    options = st.text_input("Enter the answer options, separated by commas:").split(",")
    # Add the question and answer options to the quiz_questions dictionary
    quiz_questions[question] = options
    st.write("Question added!")

# Define the main function to run the app
def main():
    # Create a sidebar menu with options to take the quiz or create a new quiz question
    menu = st.sidebar.selectbox("Menu", ["Take the quiz", "Create a new quiz question"])
    # Display the appropriate page based on the selected menu option
    if menu == "Take the quiz":
        quiz()
    elif menu == "Create a new quiz question":
        create_question()

# Run the main function
if __name__ == "__main__":
    main()









