import openai

def call_gpt(string):
    # Set the API key
    openai.api_key = "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"

    # Define the model and prompt
    model_engine = "text-davinci-003"
    prompt = string
    #prompt = "chatGPT script in detail with 500 lines to make Youtube Videos on upcoming financial crisis in 2023 in India"

    # Generate a response from the model
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response text
    message = completion.choices[0].text

    # Print the response
    #print(message)
    return message
