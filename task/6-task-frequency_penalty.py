from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored

penalties = [-2.0, -1.0, 0.0, 1.0, 2.0]

for penalty in penalties:
    print(f"\n--- Testing frequency_penalty={penalty} ---")
    try:
        run(
            deployment_name='gpt-4o',
            print_only_content=True,
            frequency_penalty=penalty
        )
    except Exception as e:
        print(f"Error with frequency_penalty={penalty}: {e}")
    print(f"--- Finished testing frequency_penalty={penalty} ---\n")
