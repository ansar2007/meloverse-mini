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

def search_content(items):
    search = st.text_input("Search for something...")
    if search:
        found = False

        for item in items:
            if search.lower() in item["title"].lower():
                st.subheader(item["title"])
                st.caption(item["category"] + " | By " + item["author"])
                st.write(item["description"])
                st.divider()

                found = True
        if search and not found:
            st.warning("Not found...try another search!")

def display_content(items):
    for item in items:
        st.subheader(item["title"])
        st.caption(item["category"] + " | By " + item["author"])
        st.write(item["description"])
        st.divider()


# HOME SECTION
if section == "Home":
    st.title("MELOVERSE")
    st.subheader("A little universe of words, emotions and stories.")

    st.write("Where thoughts find words, and words find a home.")

    st.write("Explore the Universe")
    st.success("Welcome to the world of Verses full of melody!!")
    st.divider()

    name = st.text_input("Enter a Pen Name: ")
    if name:
        st.write("Welcome to MELOVERSE, ",name)


        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("PENZ")
            st.write("Words and thoughts.")
            st.image("assets/shakespear.jpg", width= 100)

        with col2:
            st.subheader("VIBES")
            st.write("Poetry and emotions.")
            st.image("assets/ghalib.jpg", width= 100)

        with col3:
            st.subheader("SCRIPTS")
            st.write("Stories and fiction.")
            st.image("assets/ruskinbond.jpg", width= 100)

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
    

    poems = [
    {
        "title": "The Unsaid",
        "author": "Yeoul",
        "category": "Poetry",
        "description": "Emotions that words could never express."
    },
    {
        "title": "A Quiet Evening",
        "author": "Yeoul",
        "category": "Reflection",
        "description": "Finding peace in the silence of an evening."
    },
    {
        "title": "Fragments of Yesterday",
        "author": "Yeoul",
        "category": "Literature",
        "description": "Memories that refuse to fade away."
    }
]
    search_content(poems)

    display_content(poems)

    st.subheader("Share your poetry")
    with st.form("poetry_form"):
        title = st.text_input("Poem Title")
        author = st.text_input("Enter author's name")
        description = st.text_input("Write the magic...")
        submitted = st.form_submit_button("Submit Poetry")
        if submitted:
            if title and author and description:
                st.success("Your poetry has been submitted!")
            else:
                st.error("Please fill in all the fields.")

# SCRIPTS SECTION
elif section == "SCRIPTS":

    st.title("MLV SCRIPTS")
    st.write("Stories, fiction and book releases.")

    st.info("A universe of stories waiting to unfold.")

    col11, col22, = st.columns(2)

    with col11:
        if st.button("Picrure and the Book"):
            st.video("assets/booknpic.mp4")
            st.caption("A visual representation of the feeling...")
    with col22:
        if st.button("The Sorrow Flower"):
            st.video("assets/flowersorrow.mp4")
            st.caption("A visual representation of the feeling...")

    #ABOUT SECTION
elif section == "ABOUT":

    st.title("About Meloverse")
    st.write("This is a place, a universe built exclusively for art, \nartists and art enthusiasts.")

    if st.button("More Info..."):
        st.success("Not today....hehe!")
