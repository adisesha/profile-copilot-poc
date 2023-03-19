# profile-copilot-poc
This is a proof of concept. It's chat bot that helps recruiters to right questions on profile. Check the [blog post](https://medium.com/@adisesha/leveraging-chatgpt-and-langchain-to-enhance-recruitment-a-poc-b97ce2d01e82) for more details.

## How to run
1. Set `OPENAI_API_KEY` environment variable.You can get it from https://platform.openai.com/account/api-keys.
2. Install conda. Follow instructions from https://docs.conda.io/projects/conda/en/latest/user-guide/install/.
3. Go to root directory of the project and run `conda env create -f environment.yml`.
4. Run `conda activate profile-copilot-poc`.
5. Run `python main.py`.
