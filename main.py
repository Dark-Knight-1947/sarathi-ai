from openai import OpenAI 

client = OpenAI() #Create an object from OpenAI class & store it in a variable called client

question = input("You: ")

# Call the Responses API and store the returned Response object in a variable called response.
# Use the "gpt-5.6-luna" model, pass the question variable as input,
# and limit the generated output to a maximum of 30 tokens.
response = client.responses.create(
    model="gpt-5.6-luna",
    input = question,
    max_output_tokens = 30
    )

print("AI:", response.output_text) #Print the output text of the response object.
#print(response.usage) #Print the usage of the response object.
