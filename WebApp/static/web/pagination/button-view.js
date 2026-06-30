document.addEventListener('DOMContentLoaded', () => {
    const games = document.querySelectorAll('#game-container .product__item');
    const toggleButton = document.getElementById('toggle-button');

    const initialCount = 8;
    let showingMore = false;

    games.forEach((game, index) => {
      if (index >= initialCount) {
        game.style.display = 'none';
      }
    });

    toggleButton.addEventListener('click', (event) => {
      event.preventDefault();
      
      if (showingMore) {
        // Show only the initial 8 games
        games.forEach((game, index) => {
          if (index >= initialCount) {
            game.style.display = 'none';
          }
        });
        toggleButton.textContent = 'View More';
      } else {
        // Show all games
        games.forEach(game => {
          game.style.display = 'block';
        });
        toggleButton.textContent = 'View Less';
      }
      showingMore = !showingMore;
    });
});
