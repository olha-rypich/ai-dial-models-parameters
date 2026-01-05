from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API

models = [
    'gpt-4o',
    'claude-3-7-sonnet@20250219',
    'gemini-2.5-pro'
]

for model in models:
    print(f"\n--- Testing model: {model} ---")
    try:
        run(
            deployment_name=model,
            print_request=False,
            print_only_content=True,
        )
    except Exception as e:
        print(f"Error for model '{model}': {e}")
        print("Proceeding to the next model...\n")
    print(f"--- Finished testing model: {model} ---\n")
