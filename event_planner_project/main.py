from agents import theme_agent, catering_agent

def main():
    theme_query = "Superhero Party"
    theme_result = theme_agent.run(theme_query)
    
    catering_query = "Superhero Party"
    catering_result = catering_agent.run(catering_query)
    
    print("🎯 Suggested Theme Idea:", theme_result)
    print("🍽️ Recommended Catering:", catering_result)

if __name__ == "__main__":
    main()
