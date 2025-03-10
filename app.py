# import streamlit as st
# st.title("Text Analyzer")
# paragraph=st.text_area("Enter your paragraph")
# if paragraph:
#     st.write("you entered")
#     st.text(paragraph)



# # Words And Characters count
# if paragraph:
#     word_count=len(paragraph.split())
#     character_count=len(paragraph)

#     st.write(f"Total Words:{word_count}")
#     st.write(f"Total Characters:{character_count}")

# # Vowels check    


# vowels="aeiouAEIOU"
# vowel_count=sum(1 for char in paragraph if char in vowels)
# st.write(f"Total Vowels : {vowel_count}")


# # search and replace
# search_word=st.text_input("Enter the word you search")
# replace_word=st.text_input("Enter the word you replace")

# if search_word:
#     modifiedparagraph=paragraph.replace(search_word,replace_word)
#     st.write("Modified paragraph")
#     st.text(modifiedparagraph)

# # Uppercase and Lowercase Conversion: 
# upper=paragraph.upper()   
# lower=paragraph.lower()
# st.write("upper text")
# st.text(upper)
# st.write("lower text")
# st.text(lower)

# # Type casting

# word_count_str=str(word_count)
# vowel_count_str=str(vowel_count)
# st.write("Type Casting:")
# st.write(f"Word Count (as string): {word_count_str}")
# st.write(f"Vowel Count (as string): {vowel_count_str}")

# # operators


# avg_word_length = character_count / word_count if word_count > 0 else 0

# st.write("Length of words")  
# st.text(avg_word_length) 

# #  Python Keywords
# if "python" in paragraph:
#        st.write("The paragraph contains the word 'Python'.")
# else:
#         st.write("The paragraph does not contain the word 'Python'.")




import streamlit as st

# Page Config (Title & Layout)
st.set_page_config(page_title="Text Analyzer", layout="centered")

# Custom CSS for Better Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .big-font {
            font-size:22px !important;
            font-weight: bold;
            color: #333;
        }
        .box {
            background-color: green;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            height:0px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📜 Text Analyzer</h1>", unsafe_allow_html=True)

# User Input
paragraph = st.text_area("✍️ Enter your paragraph:", height=150)

# If paragraph is entered, start analysis
if paragraph:
    
 
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>📌 You Entered</p>", unsafe_allow_html=True)
    st.text_area("Your Text:", paragraph, height=100)
    st.markdown("</div>", unsafe_allow_html=True)

    # Words & Characters Count
    word_count = len(paragraph.split())
    character_count = len(paragraph)

    # Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in paragraph if char in vowels)

    # Average Word Length Calculation
    avg_word_length = character_count / word_count if word_count > 0 else 0

    # Display Text Analysis
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>📊 Text Analysis</p>", unsafe_allow_html=True)
    st.write(f"📌 **Total Words:** {word_count}")
    st.write(f"📌 **Total Characters:** {character_count}")
    st.write(f"📌 **Total Vowels:** {vowel_count}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Length of Words (NEW SECTION)
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>📏 Length of Words</p>", unsafe_allow_html=True)
    st.write(f"🔢 **Average Word Length:** {avg_word_length:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Search & Replace
    search_word = st.text_input("🔎 Enter word to search:")
    replace_word = st.text_input("✏️ Enter word to replace with:")
    modified_paragraph = paragraph.replace(search_word, replace_word) if search_word else paragraph

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>🔄 Modified Paragraph</p>", unsafe_allow_html=True)
    st.text_area("Modified Text:", modified_paragraph, height=100)
    st.markdown("</div>", unsafe_allow_html=True)

    # Uppercase & Lowercase Conversion
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown("<p class='big-font'>🔠 Uppercase</p>", unsafe_allow_html=True)
        st.text_area("Uppercase Text:", paragraph.upper(), height=100)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown("<p class='big-font'>🔡 Lowercase</p>", unsafe_allow_html=True)
        st.text_area("Lowercase Text:", paragraph.lower(), height=100)
        st.markdown("</div>", unsafe_allow_html=True)



        # Length of Words (NEW SECTION)
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>📏 Length of Words</p>", unsafe_allow_html=True)
    st.write(f"🔢 **Average Word Length:** {avg_word_length:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Python Keyword Check
    python_check = "✅ The paragraph contains the word 'Python'." if "python" in paragraph.lower() else "❌ The paragraph does NOT contain the word 'Python'."
    
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>🐍 Python Check</p>", unsafe_allow_html=True)
    st.write(python_check)
    st.markdown("</div>", unsafe_allow_html=True)
