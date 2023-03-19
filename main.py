import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from profile_bot import Chatbot
from rich.style import Style
from rich.text import Text
from rich.spinner import Spinner
from rich.live import Live

# Define styles for displaying questions and answers
question_style = Style(color="blue")
answer_style = Style(color="green")

# Create a console object for displaying rich text
console = Console()

# Initialize the Chatbot
chat_bot = Chatbot()

def print_summary(resume_path):
    # Print the path of the resume
    console.print(f"Resume path: {resume_path}")

    # Summarize the resume and print the result
    resume_summary = chat_bot.summarize_resume(resume_path)
    console.print(Text(f"Summary: {resume_summary}", style=answer_style))

def process_command(command):
    # Process user commands
    if command == "q":
        console.print("Quitting program.")
        sys.exit(0)
    else:
        console.print("Invalid command.")
        return False

def main():
    # Print a welcome message
    console.print(Panel("Welcome to the Conversational Terminal App"))

    while True:
        # Prompt the user for a resume file path
        resume_path = Prompt.ask(Text("Please enter the path to the resume PDF file:", style=question_style))

        # Display a spinner while loading the resume summary
        with Live(Spinner("dots"), auto_refresh=True):
            print_summary(resume_path)

        # Print instructions for chat mode and available commands
        console.print("Entering chat mode.")
        console.print("Commands: 'q' to quit program.")

        while True:
            # Prompt the user for a question or command
            user_input = Prompt.ask(Text("Ask a question or enter a command:", style=question_style))
            
            # Check if the input is a command or a question
            if len(user_input) <= 2:
                if process_command(user_input):
                    break
            else:
                # Get the chatbot's answer and print it
                with Live(Spinner("dots"), auto_refresh=True):
                    answer = chat_bot.answer(user_input)
                    console.print(Text(f"Answer: {answer}", style=answer_style))

if __name__ == "__main__":
    main()
