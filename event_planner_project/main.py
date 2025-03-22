from agents import theme_agent

def main():
    theme_query = "Superhero Party"
    result = theme_agent.run(theme_query)
    print("🎯 Suggested Theme Idea:", result)

if __name__ == "__main__":
    main()
