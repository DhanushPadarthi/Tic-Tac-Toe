from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve the main page with HTML, CSS, and JavaScript
@app.get("/", response_class=HTMLResponse)
def serve_tic_tac_toe():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tic-Tac-Toe</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #002b36;
                color: #fdf6e3;
                margin: 0;
                padding: 0;
            }
            h1 {
                font-size: 2.5rem;
                color: #ffdc00;
                margin: 20px 0;
            }
            .board {
                display: grid;
                grid-template-columns: repeat(3, 100px);
                grid-gap: 10px;
                justify-content: center;
                margin: 20px auto;
            }
            .cell {
                width: 100px;
                height: 100px;
                font-size: 2rem;
                font-weight: bold;
                display: flex;
                justify-content: center;
                align-items: center;
                border: 2px solid #073642;
                background-color: #586e75;
                cursor: pointer;
                transition: transform 0.2s ease, background-color 0.3s;
            }
            .cell:hover {
                transform: scale(1.1);
                background-color: #657b83;
            }
            .cell.taken {
                cursor: not-allowed;
                color: #eee8d5;
            }
            #message {
                margin-top: 20px;
                font-size: 1.2rem;
                color: #cb4b16;
                font-weight: bold;
                animation: pulse 1s infinite;
            }
            button {
                background-color: #268bd2;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 1rem;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.2s;
            }
            button:hover {
                background-color: #2aa198;
                transform: scale(1.1);
            }
            button:active {
                transform: scale(0.9);
            }
            @keyframes pulse {
                0% { color: #cb4b16; }
                50% { color: #ff4500; }
                100% { color: #cb4b16; }
            }
        </style>
        <script>
            const winningCombinations = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
            ];
            let boardState = ['', '', '', '', '', '', '', '', ''];
            let currentPlayer = 'X';
            let gameActive = true;

            function checkWinner() {
                for (const combination of winningCombinations) {
                    const [a, b, c] = combination;
                    if (
                        boardState[a] &&
                        boardState[a] === boardState[b] &&
                        boardState[a] === boardState[c]
                    ) {
                        gameActive = false;
                        document.getElementById('message').textContent = `Player ${currentPlayer} wins! 🎉`;
                        return;
                    }
                }
                if (!boardState.includes('')) {
                    gameActive = false;
                    document.getElementById('message').textContent = "It's a draw!";
                }
            }

            function handleClick(event) {
                const index = event.target.getAttribute('data-index');
                if (!gameActive || boardState[index]) return;
                boardState[index] = currentPlayer;
                event.target.textContent = currentPlayer;
                event.target.classList.add('taken');
                checkWinner();
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }

            function resetGame() {
                boardState = ['', '', '', '', '', '', '', '', ''];
                currentPlayer = 'X';
                gameActive = true;
                document.getElementById('message').textContent = '';
                document.querySelectorAll('.cell').forEach(cell => {
                    cell.textContent = '';
                    cell.classList.remove('taken');
                });
            }

            document.addEventListener('DOMContentLoaded', () => {
                const cells = document.querySelectorAll('.cell');
                cells.forEach(cell => cell.addEventListener('click', handleClick));
                document.getElementById('reset-button').addEventListener('click', resetGame);
            });
        </script>
    </head>
    <body>
        <h1>Tic-Tac-Toe</h1>
        <div id="board" class="board">
            <div class="cell" data-index="0"></div>
            <div class="cell" data-index="1"></div>
            <div class="cell" data-index="2"></div>
            <div class="cell" data-index="3"></div>
            <div class="cell" data-index="4"></div>
            <div class="cell" data-index="5"></div>
            <div class="cell" data-index="6"></div>
            <div class="cell" data-index="7"></div>
            <div class="cell" data-index="8"></div>
        </div>
        <div id="message"></div>
        <button id="reset-button">Reset Game</button>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
