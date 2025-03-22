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
