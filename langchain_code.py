from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain import OpenAI
import os

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the LLM wrapper using OpenAI's GPT
llm = OpenAI(temperature=0.3)  # Adjust temperature as needed (0.3 for balanced output)

# Function to split text into manageable chunks
def split_text(text, max_chunk_size=2000):
    """
    Splits the text into chunks of a specified maximum size.
    """
    chunks = []
    while len(text) > max_chunk_size:
        # Find the last period before the chunk limit
        split_point = text.rfind('.', 0, max_chunk_size)
        if split_point == -1:  # No period found, use the maximum size
            split_point = max_chunk_size
        chunks.append(text[:split_point + 1].strip())
        text = text[split_point + 1:].strip()
    if text:
        chunks.append(text)
    return chunks

# Prepare the prompt template
prompt_template = """
As a skilled summarizer, your task is to write a concise summary of the following conversations, ensuring to include the main points and key supporting details. Your summary should effectively capture the essential elements of the conversations while maintaining brevity and clarity. Please provide a well-structured and comprehensive summary that highlights the main ideas and key supporting points discussed in the conversations:
{text}
"""

# Define the prompt template structure with the {text} placeholder
prompt = PromptTemplate(
    input_variables=["text"],
    template=prompt_template
)

# Step 1: Read the text from a .txt file
file_path = "source/english.txt"  # Replace with the path to your .txt file

with open(file_path, 'r', encoding='utf-8') as file:
    long_text = file.read()  # This reads the entire file's content as a string

# Step 2: Chunk the long text and prepare the document objects for summarization
chunks = split_text(long_text)
docs = [Document(page_content=chunk) for chunk in chunks]

# Initialize the summarization chain
chain = load_summarize_chain(llm, chain_type="map_reduce", return_intermediate_steps=False)

# Step 3: Summarize each chunk and combine the results
summaries = []
for doc in docs:
    formatted_prompt = prompt.format(text=doc.page_content)
    summary = chain.run([Document(page_content=formatted_prompt)])
    summaries.append(summary)

# Combine the summaries from each chunk into a final summary
final_summary = " ".join(summaries)

# Print the final summary
print(final_summary)
