from openai import OpenAI 

client = OpenAI() #Create an object from OpenAI class & store it in a variable called client

previous_response_id = None

while True:
    question = input("You: ")
    if question.lower() == "exit": #Stopping condition for while loop
        break

    # Call the Responses API and store the returned Response object in a variable called response.
    # Use the "gpt-5.6-luna" model, pass the question variable as input,
    # and limit the generated output to a maximum of 30 tokens.
    response = client.responses.create(
        model="gpt-5.6-luna",
        input = question,
        max_output_tokens = 30,
        previous_response_id=previous_response_id
        )

    print("AI:", response.output_text) #Print the output text of the response object.
    # print(response.usage) #Print the usage of the response object.
    previous_response_id = response.id #Store the id of the response object in the previous_response_id variable.

