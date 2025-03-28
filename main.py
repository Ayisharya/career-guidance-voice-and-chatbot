import gradio as gr
import pyttsx3

def random_response(input_text):
    input_text = input_text.lower().strip()  

    if input_text in ["hello", "hiii", "hi", "hellooooo"]:
        response = "Hello! How can I help you?"
    elif input_text == "how are you":
        response = "I am doing great. Thank you."
    elif input_text == "i need help about my upcoming career":
        response = ("It’s great that you’re thinking about your career! Provide me your basic skills "
                    "one by one. I will provide you with career options and related skills to become industry-ready.")
    elif input_text == "python":
        response = ("To get industry-ready with Python, master core concepts like data structures, object-oriented programming, "
                    "file handling, and error management. Advance your skills with decorators, multithreading, and type hinting. "
                    "Learn Flask (web development), Pandas (data analysis), and TensorFlow (AI). Share real-world projects on GitHub.")
    elif input_text == "java":
        response = ("To become industry-ready with Java, master data types, OOP, file handling, and exception management. "
                    "Learn frameworks like Spring Boot, JUnit, and Maven. Build real-world projects and share them on GitHub.")
    elif input_text == "c++":
        response = ("To become industry-ready with C++, master data types, pointers, memory management, and OOP. "
                    "Learn STL, multithreading, and smart pointers. Build projects like system-level applications or game engines.")
    elif input_text == "c":
        response = ("To become industry-ready with C, master data types, pointers, and memory management. "
                    "Learn system-level programming, multithreading, and debugging tools like gdb. Build and share real-world projects.")
    elif input_text == "bye":
        response = "Goodbye! Come back whenever you need help. I'm here to assist you."
    else:
        response = "I don't have enough knowledge about that yet, but I'll learn and help you soon!"

   
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.say(response)
    engine.runAndWait()

    return response


with gr.Blocks() as demo:
    gr.Markdown("## 💻 Career Guidance Voice Assistant")
    chatbot = gr.Chatbot(label="Chat History")
    input_text = gr.Textbox(label="Your Message", placeholder="Type your message here...", lines=1)

    def chat(input_text, history):
        response = random_response(input_text)
        history = history + [(input_text, response)]
        return history, ""

    submit_btn = gr.Button("Send")
    submit_btn.click(fn=chat, inputs=[input_text, chatbot], outputs=[chatbot, input_text])

demo.launch()
