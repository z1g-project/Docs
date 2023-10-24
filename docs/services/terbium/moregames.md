# Indroduction

It appears you want to add more games to Terbium Games which is compleatly cool! I have specialy designed Terbium Game Center for easy use for game porting.

## Adding the Game to games.html

First and of course navigate to `static/games/games.html` and find an area where you want to add more games (Best if After Line 121.)

### Code for the games

`<div class="game-card" onclick="openGame('gameengine.html?game=https://example.com/games')">
      <img src="pages/game13.jpg" alt="Game 13">
      <h3>An Example Game</h3>
      <p>A good example of what the code should be</p>
    </div>`

## Storing the Game Assets

It is highly recommended you use the .jpg format and store then in the `pages` folder and name the files game{number}.jpg

## Other Information

None as of right now