import streamlit as st
import random


def convert_to_kg(weight_in_grams):
    return weight_in_grams/1000.00


# Set page config
st.set_page_config(
    page_title="Mathematics for Us",
    page_icon="🧮",
    layout="wide"
)

# Set page background
page_bg = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1557881365-318479f8f707");
background-size: cover;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# Set page heading
st.write("""
# Mathematics for Us
## Weight Converter
""")

# Get user input
num_observations = st.number_input("Enter the number of observations:", min_value=1)

weights_in_grams = []

for i in range(num_observations):
    weight = st.number_input(f"Enter the weight for observation {i + 1} (in grams):", min_value=1)
    weights_in_grams.append(weight)

weights_in_kg = list(map(convert_to_kg, weights_in_grams))

# Display results
st.write("### Results")
st.write(f"The weights you entered (in grams): {weights_in_grams}")
st.write(f"The weights converted to kilograms: {weights_in_kg}")

# Cheatsheet
# Cheatsheet
with st.container():
    st.write("----")
    st.header("Cheat Sheet")
    image_col, text_col = st.columns((1, 1))
with image_col:

    st.subheader("physics cheatsheet class 11th")
st.markdown("[download pdf](https://www.resonance.ac.in/sc/post/attachment/(2232)-gyan-sutra-p.pdf)")
st.subheader("Differentiation")
st.markdown("[Download PDF](https://dgtstudy.com/media/media/study_material/2020-04-06/DGT_Differentiation.pdf)")
st.subheader("intigration")
st.markdown("[download pdf](https://ncert.nic.in/ncerts/l/lemh201.pdf)")
st.subheader("slop of line")
st.markdown("[download pdf](https://www.dunkirkcsd.org/cms/lib/NY19000564/Centricity/Domain/13/slope%20of%20a"
            "%20line%20notes.pdf)")
st.subheader("trigonometric ratios")
st.markdown("[download pdf](https://tutorial.math.lamar.edu/pdf/trig_cheat_sheet.pdf)")
st.subheader("graph")
st.markdown("[download pdf](file:///C:/Users/Avinash/Downloads/functions-and-graphs.pdf)")
st.subheader("maxima minima value function")
st.markdown("[download pdf](file:///C:/Users/Avinash/Downloads/functions-and-graphs.pdf)")

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

        if selected_option:

            if selected_option == options[0]:
                st.write("Correct!")
            else:
                st.write("Sorry, that's incorrect.")


def create_question():
    # Get the question and answer options from the user
    question = st.text_input("Enter the quiz question:")
    options = st.text_input("Enter the answer options, separated by commas:").split(",")
    # Add the question and answer options to the quiz_questions dictionary
    quiz_questions[question] = options
    st.write("Question added!")


def main():
    # Create a sidebar menu with options to take the quiz or create a new quiz question
    menu = st.sidebar.selectbox("Menu", ["Take the quiz", "Create a new quiz question"])
    # Display the appropriate page based on the selected menu option
    if menu == "Take the quiz":
        quiz()
    elif menu == "Create a new quiz question":
        create_question()


if __name__ == "__main__":
    main()
