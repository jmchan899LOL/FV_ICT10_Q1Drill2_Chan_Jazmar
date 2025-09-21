from pyscript import document, display
 #define the function to be called on button click
def show_profile(e):
    # these are user inputs to be gathered from HTML input fields
    name = document.getElementById("input1").value
    age = document.getElementById("input2").value
    school = document.getElementById("input3").value
# this is a multiline string in Python using f-string formatting
    multiline = f"""Student Profile
Name   : {name}
Age    : {age}
School : {school}
"""
    # this is the notes section that uses the same variables for name, age, and school and will be the second part of the output for the multiline string
    notes = f"""Notes:
{name} is currently {age} years old and studies at {school}.
This information 
was gathered through 
input fields 
and displayed using
a multiline string
in Python via PyScript."""
# this combines the multiline string and notes into one HTML output to be displayed in the output div
    html_output = f"{multiline}{notes}"
# this displays the final output in the output div
    display(html_output, target="output1")

