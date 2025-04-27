#
#


import streamlit as st
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("BMI Calculator 💪")
    st.write("Calculate your Body Mass Index easily!")

    # User Inputs
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi}")

            # BMI Category
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Weight and height must be greater than 0!")

if __name__ == "__main__":
    main()