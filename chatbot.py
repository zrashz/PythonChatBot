import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyCOkBzdFduI-j3_W1OnRpM4uTRsKw2loVE")
# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are an expert at teaching ICT. Your task is to engage in conversations about science and answer questions. Explain scientific concepts so that they are easily understandable. Use analogies and examples that are relatable. Use humor and make the conversation both educational and interesting. Ask questions so that you can better understand the user and improve the educational experience. Suggest way that these concepts can be related to the real world with observations and experiments.",
)
history =[]
print("Bot: Hello, how can I help you ?")
while True:
    user_input = input("you : ")
    chat_session = model.start_chat(
    history=history,
    )
    response = chat_session.send_message(user_input)
    model_response = response.text
    print()
    print(f'Bot: {model_response}')
    print()
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})