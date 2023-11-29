# AI YouTube Assistant 

## Overview

This project is designed to create a YouTube assistant that can read YouTube videos and answer questions asked by users. The system utilizes SentenceTransformerEmbeddings for creating embeddings and relies on Azure-based OpenAI for large language model capabilities.

![YouTube Assistant App](/Project.jpg)


### Key Features

- **Semantic Understanding**: Leverage SentenceTransformerEmbeddings to create rich semantic embeddings, allowing the YouTube Assistant to comprehend the nuances of video content.

- **Language Model Capabilities**: Benefit from the robust language modeling capabilities of Azure-based OpenAI, empowering the assistant to provide articulate and contextually relevant responses to user queries.

- **Dynamic Q&A Interaction**: Engage in dynamic question-and-answer interactions with YouTube videos, as the assistant processes your queries and derives insightful responses from the video content.


## Running it locally
Create a .env file with the environment variables mentioned in env.exmaple :

```bash
OPENAI_API_KEY=
OPENAI_API_TYPE=
OPENAI_API_BASE=
OPENAI_API_VERSION=
OPENAI_API_DEPLOYMENT=
OPENAI_API_LLM_MODEL=
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the streamlit app:

```bash
streamlit run main.py
```

## Acknowledgments

- SentenceTransformerEmbeddings
- Azure-based OpenAI
- Streamlit


Feel free to explore and enhance the capabilities of the YouTube Assistant! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. Thank you for your contributions!



