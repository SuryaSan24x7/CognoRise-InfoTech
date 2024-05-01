import React, { useState ,useEffect} from 'react';
import './App1.css';
import { Analytics } from "@vercel/analytics/react"

const X = 'X';
const O = 'O';
const EMPTY = null;

function App() {
  const [board, setBoard] = useState(Array(3).fill(Array(3).fill(EMPTY)));
  const [currentPlayer, setCurrentPlayer] = useState(X);
  const [winner, setWinner] = useState(null);
  const [playerSymbol, setPlayerSymbol] = useState(X);

  const aiSymbol = playerSymbol === X ? O : X;

  // Function to check if a player has won
  const checkWinner = (board, player) => {
    // Check rows, columns, and diagonals
    for (let i = 0; i < 3; i++) {
      if (board[i][0] === player && board[i][1] === player && board[i][2] === player) return true;
      if (board[0][i] === player && board[1][i] === player && board[2][i] === player) return true;
    }
    if (board[0][0] === player && board[1][1] === player && board[2][2] === player) return true;
    if (board[0][2] === player && board[1][1] === player && board[2][0] === player) return true;
    return false;
  };

  // Function to check if the board is full
  const isBoardFull = (board) => {
    return board.every(row => row.every(cell => cell !== EMPTY));
  };

  // Function to make AI move
  const makeAIMove = (board) => {
    let bestMove = null;
    let bestScore = -Infinity;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (board[i][j] === EMPTY) {
          board[i][j] = aiSymbol;
          let score = minimax(board, 0, false);
          board[i][j] = EMPTY;
          if (score > bestScore) {
            bestScore = score;
            bestMove = { row: i, col: j };
          }
        }
      }
    }
    return bestMove;
  };

  // Minimax algorithm
  const minimax = (board, depth, isMaximizing) => {
    if (checkWinner(board, playerSymbol)) return -10 + depth;
    if (checkWinner(board, aiSymbol)) return 10 - depth;
    if (isBoardFull(board)) return 0;
    
    if (isMaximizing) {
      let bestScore = -Infinity;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          if (board[i][j] === EMPTY) {
            board[i][j] = aiSymbol;
            let score = minimax(board, depth + 1, false);
            board[i][j] = EMPTY;
            bestScore = Math.max(bestScore, score);
          }
        }
      }
      return bestScore;
    } else {
      let bestScore = Infinity;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          if (board[i][j] === EMPTY) {
            board[i][j] = playerSymbol;
            let score = minimax(board, depth + 1, true);
            board[i][j] = EMPTY;
            bestScore = Math.min(bestScore, score);
          }
        }
      }
      return bestScore;
    }
  };

  // Function to handle player move
  const handleClick = (row, col) => {
    if (board[row][col] === EMPTY && !winner) {
      const newBoard = board.map((rowArr, rowIndex) => {
        return rowArr.map((cell, colIndex) => {
          return rowIndex === row && colIndex === col ? currentPlayer : cell;
        });
      });
      setBoard(newBoard);

      if (checkWinner(newBoard, currentPlayer)) {
        setWinner(currentPlayer);
      } else if (isBoardFull(newBoard)) {
        setWinner('Tie');
      } else {
        setCurrentPlayer(currentPlayer === playerSymbol ? aiSymbol : playerSymbol);
        setTimeout(() => {
          const aiMove = makeAIMove(newBoard);
          if (aiMove) {
            newBoard[aiMove.row][aiMove.col] = aiSymbol;
            setBoard(newBoard);
            if (checkWinner(newBoard, aiSymbol)) {
              setWinner(aiSymbol);
            } else if (isBoardFull(newBoard)) {
              setWinner('Tie');
            }
            setCurrentPlayer(playerSymbol);
          }
        }, 500);
      }
    }
  };

  // Function to render the game board
  const renderBoard = () => {
    return board.map((rowArr, rowIndex) => (
      <div key={rowIndex} className="row">
        {rowArr.map((cell, colIndex) => (
          <div key={colIndex} className="cell" onClick={() => handleClick(rowIndex, colIndex)}>
            {cell}
          </div>
        ))}
      </div>
    ));
  };

  // Function to display winner or current player
  const renderStatus = () => {
    if (winner) {
      return winner === 'Tie' ? 'It\'s a Tie!' : `Winner: ${winner}`;
    } else {
      return `Current Player: ${currentPlayer}`;
    }
  };
  useEffect(() => {
    setCurrentPlayer(playerSymbol);
    setBoard(Array(3).fill(Array(3).fill(EMPTY)));
    setWinner(null);
  }, [playerSymbol]);
  return (
    <div className="App">
    <div className="text-4xl font-bold mb-4">Tic Tac Toe</div>
    <div className="flex justify-end mt-4">
      <button className="btn bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" onClick={() => {setWinner(null); setBoard(Array(3).fill(Array(3).fill(EMPTY)))}}>Reload</button>
    </div>
    <div className="board">{renderBoard()}</div>
    <div className="status mt-4">{renderStatus()}</div>
    <div className="mt-4">
      <label htmlFor="playerSymbol">Select Player Symbol:</label>
      <select id="playerSymbol" value={playerSymbol} onChange={(e) => setPlayerSymbol(e.target.value)} className="ml-2">
        <option value={X}>X</option>
        <option value={O}>O</option>
      </select>
    </div>
  </div>
  );
}

export default App;
