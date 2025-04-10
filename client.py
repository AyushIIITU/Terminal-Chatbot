import subprocess
import os
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# Initialize the local model
llm = OllamaLLM(model="granite3.2:8b")

# Prompt to generate task plan
plan_prompt = PromptTemplate.from_template("""
You are a task planning assistant.
Convert this user instruction into a list of shell commands (1 per step).
Only return the commands with numbering. No explanation.

Instruction: {task}
""")

# Create the chain using RunnableSequence
plan_chain = RunnableSequence(plan_prompt, llm)

def execute_shell_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {command}\n{e}")

def run_agent():
    while True:
        task = input("🧠 Task for AI Agent (or 'q' to quit):\n> ")
        if task.lower() == "q":
            break

        print("\n⏳ Thinking...\n")
        # Use invoke instead of ainvoke, keeping it synchronous for simplicity
        plan = plan_chain.invoke({"task": task}).strip()
        commands = [line.strip().split(". ", 1)[-1] for line in plan.splitlines() if line.strip()]

        print("📋 Proposed Plan:\n")
        for i, cmd in enumerate(commands, 1):
            print(f"{i}. {cmd}")
        
        approval = input("\n✅ Approve? (y/n): ").lower().strip()
        if approval == "y":
            print("\n🚀 Executing plan...\n")
            for cmd in commands:
                print(f"$ {cmd}")
                execute_shell_command(cmd)
        else:
            print("❎ Plan cancelled.\n")

if __name__ == "__main__":
    run_agent()