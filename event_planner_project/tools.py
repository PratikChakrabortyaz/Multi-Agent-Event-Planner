from smolagents import tool

@tool
def theme_search_tool(query: str) -> str:
    """
    Searches for creative party themes.

    Args:
        query (str): The name of the theme requested (e.g., 'Superhero Party').

    Returns:
        str: A description of the requested theme or a fallback message.
    """
    ideas = {
        "Superhero Party": "Guests dress as their favorite superheroes.",
        "Casino Night": "Bring Vegas to your party with card games and roulette tables.",
        "Hollywood Glam": "A red-carpet experience with awards and photo booths.",
        "Retro Party": "Dress up in 80s and 90s outfits with vintage decorations."
    }
    return ideas.get(query, "No matching theme found. Try 'Superhero Party', 'Casino Night', or 'Hollywood Glam'.")

@tool
def catering_search_tool(query: str) -> str:
    """
    Suggests catering options for a given party theme.

    Args:
        query (str): The selected party theme (e.g., 'Superhero Party').

    Returns:
        str: Recommended catering ideas for the theme.
    """
    catering_options = {
        "Superhero Party": "Serve 'Justice League Pizza', 'Avengers Mocktails', and 'Spider-Man Cupcakes'.",
        "Casino Night": "Offer finger foods like mini burgers, cheese platters, and themed cocktails.",
        "Hollywood Glam": "Serve gourmet sliders, caviar bites, and sparkling cocktails for elegance.",
        "Retro Party": "Bring back nostalgic snacks like popcorn, candy sticks, and classic soda bottles."
    }
    return catering_options.get(query, "No matching catering idea found. Try 'Superhero Party', 'Casino Night', or 'Hollywood Glam'.")
@tool
def entertainment_search_tool(query: str) -> str:
    """
    Suggests entertainment ideas for a given party theme.

    Args:
        query (str): The selected party theme (e.g., 'Superhero Party').

    Returns:
        str: Recommended entertainment options for the theme.
    """
    entertainment_options = {
        "Superhero Party": "Organize a superhero trivia quiz, set up a Marvel vs DC debate, or host a superhero costume contest.",
        "Casino Night": "Offer poker, blackjack, and roulette stations with play money for guests.",
        "Hollywood Glam": "Create a 'Walk of Fame' photo area, screen classic Hollywood movies, or host an awards show with fake Oscars.",
        "Retro Party": "Play 80s and 90s karaoke, have a dance-off, or set up a vintage arcade gaming zone."
    }
    return entertainment_options.get(query, "No matching entertainment idea found. Try 'Superhero Party', 'Casino Night', or 'Hollywood Glam'.")
