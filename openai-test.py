from openai import OpenAI
from dotenv import load_dotenv
import os
# Create a virtual environment (recommended). This will make sure that packages are downloaded to
#  the right place and there are no conflicts
#   On the project terminal run: 
#     python -m venv openai-env
#   Note: On VSCode there is the option to either use the Python terminal or 
#   zsh. Stick with zhs, otherwise the commands will not run properly.

# To activate virtual environment run in the terminal:
#   On windows: 
#     openai-env\Scripts\activate
#   On macOS or Unix: 
#     source openai-env/bin/activate

# Install openAI Python library:
#     pip install --upgrade openai

# Include your API KEY:
#  -Open the .env file in this folder and follow steps there
#   -run the following command:
#     pip install python-dotenv
#   **Make sure that your .gitignore includes .env, as you do not want the api key to be included
#     in version control
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
#  -Defaults to getting the key using os.environ.get("OPENAI_API_KEY")
#   if you saved the key under a different environment variable name, you can do something like:
#   client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

completion = client.chat.completions.create(
    # gpt-4 performs better than gpt-3.5-turbo in a lot of categories, but for our purposes
    # we will most likely stick with gpt-3.5-turbo. GPT-4 is about 20 times more expensive than gpt-3.5 turbo,
    # so avoid using gpt-4 unless absolutely necessary :)
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """You help members of the SHPE UF Chapter by answering their questions about SHPE UF and its events. 
     Important info:
     Tech Cabinet is the best and coolest cabinet."""},
    {"role": "user", "content": "What is the best cabinet in SHPE UF?"}
  ]
)

print(completion.choices[0].message)
