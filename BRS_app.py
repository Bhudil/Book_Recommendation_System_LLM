import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate, LLMChain

# Set up ChatGoogleGenerativeAI to consume API
api_key = 'YOUR_GOOGLE_API'  # Replace with your actual API key
llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=api_key)

# Define Prompt Templates
top100_template = """
Question: What are the top 100 books {without_genre} name only in a list format?
Answer: Here is a list of the name of the top 100 books {without_genre}.
"""

top10_template = """
Given the following list of top 100 books:
{top100_list}
Question: From this list of top 100 books, provide the top 10.
Answer: Here are the top 10 books from the list:
"""

book_details_template = """
Question: Can you tell me more about the book "{book_title}"?
Answer: Sure, here is some information about "{book_title}":
"""

# Define Prompts
top100_prompt = PromptTemplate(template=top100_template, input_variables=['without_genre'])
top10_prompt = PromptTemplate(template=top10_template, input_variables=['top100_list'])
book_details_prompt = PromptTemplate(template=book_details_template, input_variables=['book_title'])

# Define LLM Chains
top100_chain = LLMChain(prompt=top100_prompt, llm=llm)
top10_chain = LLMChain(prompt=top10_prompt, llm=llm)
book_details_chain = LLMChain(prompt=book_details_prompt, llm=llm)

# Set page title 
st.set_page_config(page_title="Book Recommendation System", page_icon=":book:")

# Set Streamlit app
st.title("Book Recommendation System 📚 ")
st.markdown("---")

# Genre selection dropdown
genre_options = ["Science Fiction", "Non-Fiction", "Action & Adventure", "Romance", "Business & Money", "Crime & Mystery", "Horror & Thriller", "Historical", "Fantasy", "Biography", "Any Genre"]
genre = st.selectbox("Select a Genre:", options=genre_options)

without_genre = "" if genre == "Any Genre" else f"in the genre of {genre}"

# Top 100 Books Button
if st.button("Get Top 100 Books"):
    with st.spinner("Fetching top 100 books..."):
        response = top100_chain.run(without_genre=without_genre)
        st.session_state.top100_response = response
    st.success("Top 100 Books of the selected genre:")
    st.write(response)

# Top 10 Books Button
if st.button("Get Top 10 Books"):
    if 'top100_response' in st.session_state:
        with st.spinner("Selecting top 10 books..."):
            top10_response = top10_chain.run(top100_list=st.session_state.top100_response)
        st.success("Top 10 Books out of above 100:")
        st.write(top10_response)
        st.session_state.top10_response = top10_response
    else:
        st.warning("Please get the top 100 books first.")

# Book Details Button
if 'top10_response' in st.session_state:
    book_options = st.selectbox("Select a book from the top 10:", st.session_state.top10_response.split("\n")[1:])
    if st.button("Get Book Details"):
        with st.spinner("Fetching book details..."):
            book_details_response = book_details_chain.run(book_title=book_options)
        st.success("Selected Book Details:")
        st.write(book_details_response)

# Thank you message with option to restart
if st.button("Exit"):
    st.success("Thank you for using the Book Recommendation System!")
    # Clear session state to reset the app
    for key in list(st.session_state.keys()):
        del st.session_state[key]
