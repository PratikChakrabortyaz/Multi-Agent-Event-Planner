from agents import theme_agent, catering_agent, entertainment_agent, decoration_agent

def main():
    theme_query = "Superhero Party"
    theme_result = theme_agent.run(theme_query)
    
    catering_query = "Superhero Party"
    catering_result = catering_agent.run(catering_query)
    
    entertainment_query = "Superhero Party"
    entertainment_result = entertainment_agent.run(entertainment_query)
    
    decoration_query = "Superhero Party"
    decoration_result = decoration_agent.run(decoration_query)
    
    print("🎯 Suggested Theme Idea:", theme_result)
    print("🍽️ Recommended Catering:", catering_result)
    print("🎬 Entertainment Idea:", entertainment_result)
    print("🎈 Decoration Idea:", decoration_result)

if __name__ == "__main__":
    main()
