This project is a Ludo game implemented in Python, focusing solely on the procedural paradigm as part of my university module.

Below is my initial high-level design plan:

- ~Choose to start or continue a game~
- ~Add human or computer players (min 2 pl)~
- ~Display players with assigned colours~
- ~Save and quit options~
- ~Display game board~
- ~Random dice roll generator~
- ~Player exits base after the first roll of 6~
    - ~Print board to console~
        - ~Get Player coordinates~ 
        - ~Update board using player coordinates~
    - ~User rolls dice - press enter to roll~
        - ~Update player coordinates~
    - ~Print board to console~
        - ~Get player coordinates~
        - ~Update board using player coordinates~
- Players move around the board
- Roll 6
    - (1) No players on board
        - Move first player
    - (2) One or more player on board
        - Prompt to release new player or move 'playing' player
- Roll anything but 6
    - (1) No players on board
    - (2) One or more players on board
        - Prompt to move a 'playing' player
- Players can reach home
- The game ends when all players are home
- Players can eliminate others

I plan to expand on each component in greater detail before implementation, with the goal of finding the most optimal solution.