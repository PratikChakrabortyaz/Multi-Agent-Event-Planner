# Multi-Agent Event Planner

This project is a **Multi-Agent Event Planner** designed to assist users in planning themed events with recommendations for decorations, catering, and entertainment. Leveraging multiple agents, this system efficiently coordinates various elements for a successful event.

## Features
- **Theme Selection:** Provides creative and trending theme ideas based on the given input.
- **Catering Recommendations:** Suggests customized menu options tailored to the chosen theme.
- **Entertainment Ideas:** Proposes engaging entertainment activities suitable for the theme.
- **Decoration Suggestions:** Offers visually appealing decoration ideas aligned with the event theme.

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/PratikChakrabortyaz/Multi-Agent-Event-Planner.git
   cd Multi-Agent-Event-Planner
   ```

2. **Install Dependencies**
   Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Project**
   ```bash
   python event_planner_project/main.py
   ```

2. **Example Prompt**
   The system follows this structure:
   - Theme ideas → `theme_agent`
   - Catering ideas → `catering_agent`
   - Entertainment ideas → `entertainment_agent`
   - Decoration ideas → `decoration_agent`

**Sample Output:**
```
🎯 Suggested Theme Idea: Superhero Party
🍽️ Recommended Catering: Justice League Pizza, Avengers Mocktails, and Spider-Man Cupcakes
🎬 Entertainment Idea: Organize a superhero trivia quiz, set up a Marvel vs DC debate, or host a superhero costume contest
🎈 Decoration Idea: Hang posters of superheroes, use comic strip table covers, and add action figure centerpieces.
```

## Project Structure
```
Multi-Agent-Event-Planner/
├── event_planner_project/
│   ├── agents.py
│   ├── tools.py
│   ├── main.py
│   ├── data/
│   │   ├── catering_data.json
│   │   ├── decoration_data.json
│   │   ├── entertainment_data.json
│   │   ├── theme_data.json
│   └── requirements.txt
```

