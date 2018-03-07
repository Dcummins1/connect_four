var board;
var cols;
var rows;
var w = 60;
var player = 1;


function playerTurn(){
    if (player == 1){
        document.getElementById("playerturn").innerHTML = "<h2 style='color:blue';>Player 1's turn</h2>"
    }
    else {
        document.getElementById("playerturn").innerHTML = "<h2 style='color:blue';>Player 2's turn</h2>"
    }
}


function twoDArray(cols, rows) {
    var arr = new Array(cols);
    for (var i = 0; i < arr.length; i++) {
        arr[i] = new Array(rows);
    }
    return arr;
}

function setup() {
    createCanvas(421, 361);
    cols = 7;
    rows = 6;
    board = twoDArray(cols, rows);
    for (var i = 0; i < cols; i++) {
        for (var j = 0; j < rows; j++) {
            board[i][j] = new Square(i, j, w);
        }
    }
}

function mousePressed() {
    var j = 0;
    for (var i = 0; i < cols; i++) {
        if (board[i][0].contains(mouseX, mouseY)) {
            makeMove(i);

        }
    }
}

function makeMove(move) {
    var i = 0;
    if (board[move][0].empty) {
        while (i < 6) {
            if (board[move][i].empty) {
                i++;
            } else {
                break;
            }

        }
    }

        board[move][i - 1].player = player;
        board[move][i - 1].empty = false;
        board[move][i - 1].show();
        checkSurrounds(move, i - 1);
        player = player * -1;
        playerTurn();
    }




function checkSquare(x, y) {
    try {
        if (board[x][y].player == player) {
            return true;
        }

    } catch (err) {
        return false;
    }

}



function checkSurrounds(x, y) {
    var check_win = [[0, -1, 0, +1], [+1, 0, -1, 0], [+1, +1, -1, -1], [+1, -1, -1, +1]];
    for (var i in check_win) {
        var initial_x = x;
        var initial_y = y;
        var initial_x1 = x;
        var initial_y1 = y;
        var up_right = true;
        var down_left = true;
        var count_up_right = 0;
        var count_down_left = 0;
        var total = 1;
        while (up_right == true) {

            if (checkSquare(initial_x + check_win[i][0], initial_y + check_win[i][1])) {


                count_up_right += 1;
                initial_x = initial_x + check_win[i][0];
                initial_y = initial_y + check_win[i][1];

            } else {

                up_right = false;
            }
        }
        while (down_left == true) {
            if (checkSquare(initial_x1 + check_win[i][2], initial_y1 + check_win[i][3])) {
                count_down_left += 1;
                initial_x1 = initial_x1 + check_win[i][2];
                initial_y1 = initial_y1 + check_win[i][3];

            } else {
                down_left = false;
            }
        }

            total += count_up_right + count_down_left;
            if (total == 4) {
                if (player == 1){
                    alert("Player "+player+" wins!!!!!!!!!!");
                    }
                else {
                    alert("Player 2 wins!!!!!!!!!!");
                    }
                location.reload();
                return;
            }
        }

    }




function draw() {
    background(255);
    for (var i = 0; i < cols; i++) {
        for (var j = 0; j < rows; j++) {
            board[i][j].show();
        }
    }
}

function Square(i, j, w) {
    this.i = i;
    this.j = j;
    this.x = i * w;
    this.y = j * w;
    this.w = w;
    this.empty = true;

    this.player = 0;



}

Square.prototype.contains = function (x, y) {
    return (x > this.x && x < this.x + this.w && y > this.y && y < this.y + this.w);
}

Square.prototype.show = function () {
    stroke(0);
    fill('blue');
    rect(this.x, this.y, this.w, this.w);
    if (this.player == 1) {
        fill("red");
        ellipse(this.x + this.w * 0.5, this.y + this.w * 0.5, this.w * 0.5);
    } else if (this.player == -1) {
        fill("yellow");
        ellipse(this.x + this.w * 0.5, this.y + this.w * 0.5, this.w * 0.5);

    }


}