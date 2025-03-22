from agents import theme_agent, catering_agent, entertainment_agent, decoration_agent

def main():
    # Step 1: Get theme suggestion
    theme = theme_agent.run("Suggest a superhero party theme.")
    print("🎯 Suggested Theme Idea:", theme)

    # Step 2: Get decoration ideas
    decorations = decoration_agent.run("Suggest superhero-themed decorations.")
    print("🎈 Decoration Idea:", decorations)

    # Step 3: Get catering ideas
    catering = catering_agent.run("Suggest superhero-themed catering ideas.")
    print("🍽️ Recommended Catering:", catering)

    # Step 4: Get entertainment ideas
    entertainment = entertainment_agent.run("Suggest superhero-themed entertainment ideas.")
    print("🎬 Entertainment Idea:", entertainment)

if __name__ == "__main__":
    main()
