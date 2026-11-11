import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MELOVERSE",
    page_icon="✍️",
    layout="wide"
)

# Sidebar navigation
section = st.sidebar.radio(
    "Enter the Universe!",
    ["Home", "PENZ", "VIBES", "SCRIPTS","ABOUT"]
)

# HOME SECTION
if section == "Home":

    st.title("MELOVERSE")
    st.subheader("A little universe of words, emotions and stories.")

    st.write("Where thoughts find words, and words find a home.")

    if st.button("Explore the Universe"):
        st.success("Welcome to the world of Verses full of melody!!")


# PENZ SECTION
elif section == "PENZ":

    st.title("MLV PENZ")
    st.write("Thoughts, write-ups and literary works.")

    st.info("A space for words waiting to be written.")

# VIBES SECTION
elif section == "VIBES":

    st.title("MLV VIBES")
    st.write("Shayaris, poetry and artistic expressions.")

    st.info("A space where emotions find their voice.")

# SCRIPTS SECTION
elif section == "SCRIPTS":

    st.title("MLV SCRIPTS")
    st.write("Stories, fiction and book releases.")

    st.info("A universe of stories waiting to unfold.")

#ABOUT SECTION
elif section == "ABOUT":

    st.title("About Meloverse")
    st.write("This is a place, a universe built exclusively for art, \nartists and art enthusiasts.")

    if st.button("More Info..."):
        st.success("Not today....hehe!")
        st.info("Let's see if time permits....")
