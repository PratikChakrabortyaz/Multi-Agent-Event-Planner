from manager_agent import manager_agent

def main():
    task = "Plan a superhero-themed party with decorations, catering, and entertainment for 20 guests."
    result = manager_agent.run(task)
    
    print("🎉 Complete Party Plan:")
    print(result)

if __name__ == "__main__":
    main()
