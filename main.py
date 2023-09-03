import streamlit as st
import webbrowser

def main():
    st.title("My Personal Details")

    # Your personal details
    name = "Mukund Prasad H S"
    age = 21
    email = "mukundprasadhs@gmail.com"
    address = "65/114,2nd cross,3rd A Main, Krishna Nagar, Bengaluru-560061, India"


    # Display details
    st.write("## Personal Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Email:** {email}")
    st.write("Contact number:8618473742")
    st.write(f"**Address:** {address}")
    st.write("Engineering Specialization: Artificial Intelligence and Machine Learning")
    row1, row2, row3 = st.columns(3)

    # Row 1: Engineering CGPA and Marksheet Button
    with row1:
        st.write("Engineering CGPA (6th sem): 7.66")
        # Center-align the "View Engineering Marksheet" button
        # Display the "View Engineering Marksheet" button
        if st.button("View Engineering Marksheet", key='view_eng_marksheet'):
            # Replace this link with the direct link to your engineering marksheet on Google Drive
            eng_marksheet_link = "https://drive.google.com/file/d/1YlPH6Ulbxgu5xYMZV6U_SHaXDB1deFMG/view?usp=sharing"
            webbrowser.open_new_tab(eng_marksheet_link)

    # Row 2: PUC Percentage and Marksheet Button
    with row2:
        st.write("PUC Percentage: 72.66%")
        # Display the "View PUC Marksheet" button
        if st.button("View PUC Marksheet", key='view_puc_marksheet'):
            # Replace this link with the direct link to your PUC marksheet on Google Drive
            puc_marksheet_link = "https://drive.google.com/file/d/1S39CxzbSwbhfuXsgD1y40fzhX7cdUNVh/view?usp=sharing"
            webbrowser.open_new_tab(puc_marksheet_link)
    with row3:
        st.write("SSLC Percentage: 78.88%")
        # Display the "View PUC Marksheet" button
        if st.button("View SSLC Marksheet", key='view_sslc_marksheet'):
            # Replace this link with the direct link to your PUC marksheet on Google Drive
            sslc_marksheet_link = "https://drive.google.com/file/d/1RbR2twx1qWYeU9RBo4z5drFqFT_IhGLk/view?usp=sharing"
            webbrowser.open_new_tab(sslc_marksheet_link)
if __name__ == "__main__":
    main()
