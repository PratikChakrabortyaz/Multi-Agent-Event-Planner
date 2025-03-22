from manager_agent import manager_agent, task_prompt  # Import the correct prompt

def main():
    result = manager_agent.run(task_prompt)
    print("🎉 Complete Party Plan: ", result)

if __name__ == "__main__":
    main()

