from openai import OpenAI 

client = OpenAI() #Create an object from OpenAI class & store it in a variable called client

previous_response_id = None

while True:
    question = input("You: ")

    if question.lower() == "exit": #Stopping condition for while loop
        break

    if not question.strip(): #Check if the input is empty or contains only whitespace
        continue

    try: 
        # Call the Responses API and store the returned Response object in a variable called response.
        # Use the "gpt-5.6-luna" model, pass the question variable as input,
        # and limit the generated output to a maximum of 100 tokens.
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions = "You are Sarathi, a helpful assistant. Keep your responses concise and conversational.",
            input = question,
            max_output_tokens = 100,
            previous_response_id=previous_response_id
            )
        
        print("AI:", response.output_text) #Print the output text of the response object.
        print(response.usage) #Print the usage of the response object.
        # print(response)

        previous_response_id = response.id #Store the id of the response object in the previous_response_id variable.
    
    except Exception as e:
        print("Error:", e) #Print the error message if an exception occurs.

