let inputTrue = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
];

function validSolution(board) {
  const tBoard = [];
  let row = [];
  let column = [];
  let subMatrix = [];
  let checkRow = true;
  let checkColumn = true;
  let checkSubMatrix = true;
  // creo la traspuesta y verifico las columnas.
  for (let i = 0; i < board.length; i++) {
    tBoard.push(column);
    for (let j = 0; j < board.length; j++) {
      column.push(board[j][i]);      
    }
    if (column.sort().toString() === "1,2,3,4,5,6,7,8,9"){     
      checkColumn = checkColumn && true;
    } else {
      checkColumn = false;
    }
    column = [];
  }
  console.table(board);
  // verifico las filas.
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      row.push(board[i][j])
    }
    if (row.sort().toString() === "1,2,3,4,5,6,7,8,9"){     
      checkRow = checkRow && true;
    } else {
      checkRow = false;
    }
    row = [];  
  }
  console.table(board);
  // verifico las sub matrices.
  let matrizPrueba = [];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3 + 3*i; j++) {
      for (let k = 0; k < 3; k++) {
        for (let l = 0; l < 3; l++) {
          subMatrix.push(board[k][l]);  
        }

      }
    }
  }
  console.log(subMatrix);
  return (checkRow && checkColumn);
}
console.log(validSolution(inputTrue));
