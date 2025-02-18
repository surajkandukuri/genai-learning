# Sample Python script for testing AI-generated prompts
import openai

openai.api_key = "your-api-key"

prompt = "Generate a summary of the latest trends in AI governance."
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)

print(response.choices[0].text.strip())
