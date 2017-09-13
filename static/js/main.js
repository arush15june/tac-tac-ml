/*
- Draw The Board 
- Make the PLAYER - O and COMPUTER - X
- Wait for Player's Turn
- Request a move from the server [/predict]
- Complete Turn and Move to Player
-Begin
____- Record the Current Board
____- Record the PLAYER's move
____- Generate training sample JSON
____- POST new training sample to /add    
____- Request a move from the server 
- Repeat until someone wins
- Display winner and reset option
- Reset the board if requested.
- Repeat from start
*/

var board = document.getElementById(`board`) // board is a canvas
var Screen = board.getContext('2d')

// Helper Functions
function clearBoardArray(board_arr) {
  for(var i = 0;i<board_arr.length;i++)
      for(var j = 0;j<board_arr[0].length;j++) {
          board_arr[i][j] = boardVals.EMPTY;   
      }
}

// Board Components
board.width = 320px;
board.height = 320px;
var boardVals =  {
  // Values the board can assume 
  TIC : 0, // O
  TAC : 1, // X
  EMPTY : -1 // Empty Space
}
var boardArray[3][3] = clearBoardArray(boardArray);
var moveState = { 
  // Turn State 
  PLAYER : 0,
  COMPUTER : 1
}

// Graphics Objects
var cross;
var circle;

// Event Variables
var mouseClicked = false;

// Event Listeners
document.addEventListener("mousedown",function() { mouseClicked = true;} ,false);
document.addEventListener("mouseup",function() { mouseClicked = false;} ,false);

// Drawing Helpers

function drawText(text) {

}

function drawImage(image) {

}

function drawCircle(circ) {

}

function drawRect(rect) {
  
}

// Drawing Functions

function drawStaticContent() {
  drawBackground()
  drawHUD()
  drawGrid()

}

function initDraw() {
  drawStaticContent();
  
}