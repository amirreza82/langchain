LangChain Text Summarizer

This project demonstrates a text summarization application using the LangChain framework and OpenAI's GPT. The application reads a long text from a file, splits it into manageable chunks, summarizes each chunk, and combines the summaries into a final, comprehensive summary.

Features

- Text Splitting: Splits long text into chunks of manageable size.
- Summarization: Utilizes OpenAI's GPT to generate concise summaries.
- Chunk Processing: Summarizes each chunk individually and combines the results.

Prerequisites

- Python: Ensure Python 3.6 or higher is installed.
- OpenAI API Key: Obtain an API key from OpenAI.

Installation

1. Clone the Repository:
    git clone https://github.com/your-username/langchain-text-summarizer.git
    cd langchain-text-summarizer

2. Install Dependencies:
    pip install langchain openai

3. Set Up Environment Variables:
    - Create a .env file in the root directory of the project.
    - Add your OpenAI API key to the .env file:
        API_KEY=your_openai_api_key_here

Usage

1. Prepare Your Text File:
    - Place your .txt file in the source directory.
    - Ensure the file path in the script matches your file location (e.g., source/english.txt).

2. Run the Script:
    python summarizer.py

3. View the Summary:
    - The script will print the final summary to the console.

Code Explanation

1. Environment Setup:
    - The API key is set as an environment variable for secure access.

2. Text Splitting Function:
    - split_text function splits the input text into chunks of a specified size to handle large texts.

3. Prompt Template:
    - A prompt template is defined for summarizing the text, ensuring the summaries are clear and concise.

4. Text Processing:
    - The script reads the text file, chunks it, and processes each chunk through the summarization chain.

5. Summarization:
    - Uses the map_reduce chain type from LangChain to summarize each chunk and combine the results.

Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any questions or feedback, please reach out to your-email@example.com.
