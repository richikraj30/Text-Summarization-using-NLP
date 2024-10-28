# Text Summarization using NLP

This project implements a text summarization model using natural language processing (NLP) techniques, leveraging the powerful `google/pegasus-cnn_dailymail` model for generating summaries from input text.

## Features

- **Model Used**: `google/pegasus-cnn_dailymail` for state-of-the-art text summarization.
- **FastAPI Integration**: A RESTful API built with FastAPI for making predictions.
- **Configuration Management**: YAML-based configuration for easy parameter management.
- **Prediction Pipeline**: A structured pipeline for loading the model, tokenizer, and making predictions.
- **Customizable Parameters**: Easily modify parameters like `max_length`, `num_beams`, and `length_penalty` to fine-tune the summarization output.

## Installation

### Requirements

- Python 3.x
- FastAPI
- Transformers
- PyTorch
- uvicorn
- pydantic


### Steps
1. Clone the repository:
   
   ```bash
   git clone https://github.com/richikraj30/Text-Summarization-using-NLP.git
   cd Text-Summarization-using-NLP
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## Usage
### Running the FastAPI Application

1. Start the FastAPI server:
   
   ```bash
   uvicorn app:app --reload
2. Access the API documentation at
   http://127.0.0.1:8000/docs

3. To generate a summary, send a POST request to the /predict endpoint with a JSON body containing the text to summarize:
   ```bash
   {
    "text": "Your input text goes here."
   }
### Model Training

  - To train or fine-tune the summarization model, consider using a Jupyter Notebook on Google Colab.
    
### Error Handling

  - The application includes error handling for various scenarios, such as invalid input or model loading failures. In case of an error, a meaningful message will be returned to help diagnose the issue.



## Contributing
- Contributions are welcome! Please feel free to submit a pull request or raise an issue if you have suggestions or improvements.

### Notes
- Replace `link_to_your_colab_notebook` with the actual link to your Google Colab notebook if you create one.
- Make sure the paths for your application match the project structure you have.
- Adjust any section based on your project specifics or additional features you may have. 

Feel free to ask if you need further customization or additional sections!

