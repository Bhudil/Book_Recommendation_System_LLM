# Book Recommendation System Using LLM

## Description

This Book Recommendation System is an interactive Streamlit web application that leverages the power of LangChain and Google's Generative AI to provide personalized book recommendations. Users can explore top books in various genres, narrow down to the best 10 selections, and get detailed information about specific titles.

## Features

- Genre-based book recommendations
- Top 100 books list generation
- Top 10 books selection
- Detailed information about selected books
- User-friendly interface with Streamlit

## Technologies Used

- Python 3.7+
- Streamlit
- LangChain
- Google Generative AI (Gemini Pro model)

## Demo 

![Screenshot (162)](https://github.com/Bhudil/Book_Recommendation_System_LLM/assets/99169324/f0b6e702-184c-4bdf-a4c2-255a9dea37d9)


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bhudil/Book_Recommendation_System_LLM.git
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Google API key:
- Obtain an API key from the [Google AI Studio](https://makersuite.google.com/app/apikey)
- Replace `'YOUR_GOOGLE_API'` in the code with your actual API key

## Usage

1. Run the Streamlit app:
```bash
streamlit run BRS_app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Use the interface to:
- Select a book genre
- Get top 100 books in the selected genre
- Narrow down to top 10 books
- Get detailed information about a specific book

## How It Works

1. **Genre Selection**: Users choose from a variety of genres including Science Fiction, Non-Fiction, Romance, and more.

2. **Top 100 Books**: The app uses LangChain to query the Google Generative AI model for the top 100 books in the selected genre.

3. **Top 10 Books**: From the list of 100 books, the AI model selects the top 10 based on popularity and relevance.

4. **Book Details**: Users can select a book from the top 10 list to get more detailed information about it.

5. **Exit**: Users can exit the application, which clears the session state for a fresh start.

## Code Structure

- `BRS_app.py`: Main Streamlit application file
- `requirements.txt`: List of Python dependencies
- `README.md`: Project documentation (this file)

## Future Enhancements

- Integration with book databases for more accurate recommendations
- User accounts and personalized recommendations based on reading history
- Book cover image display
- Direct links to purchase or read selected books

## Contributing

Contributions to improve the Book Recommendation System are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - bhudil.mallick@gmail.com

Project Link: [https://github.com/Bhudil/Book_Recommendation_System_LLM](https://github.com/Bhudil/Book_Recommendation_System_LLM)

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Generative AI](https://cloud.google.com/ai/generative-ai)




