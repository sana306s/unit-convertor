import streamlit as st 

st.title("🌎Unit Converter App")
st.markdown("### Converts Length,Weight and time instantly") 
st.write("Welcomw! Select a category, enter a valueand get the convert result in the real-time.")

category = st.selectbox("Choose a gategory",["Lenght","Weight","Time"])
def convert_units(category, value , unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit== "Miles to kilometers":
            return value / 0.621371

    elif category =="Weight":
        if unit == "kilograms to ponds":
             return value * 2.20462
        elif unit == "Ponds to Kilogrms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value /60
        elif unit == "Minutes to second":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    return 0
if category == "Lenght":
    unit = st.selectbox("📏 Select Conversation",["Kilometers to miles", "Miles to kilometer"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation",["Kilograms to pounds", "Pounds to kilograms"])

elif category == "Time":
    unit = st.selectbox("⌚Select Conversation",["Seconds to minutes","Minutes to seconds","Hours to minutes","Minutes to hours","Hours to days","Days to hours"])


value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is{result:.2f}")