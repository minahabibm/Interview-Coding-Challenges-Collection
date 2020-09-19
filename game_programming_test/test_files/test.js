//==================//
// 		Part 1	 	//
//==================//

var userBalance = 0;
var userBalanceBefore = 0;
var val = 0;
var x = 0;
var y = 0;
var z = 0;

// Gets called whenever the money finished tweening to the bottom.
function addFromCatch(value)
{	
	userBalance += value;
	val = value;
	x += 1;
}

// Gets called every frame.
// Time elapsed since the last update is passed into the function(milliseconds)
function onUpdate({delta})
{	

	if (val === 1000){
		y += delta
		z += 8 * y;
		setInterval(function(){
			increment();
		},  z/x );
	}else if (val === 2000){
		y += delta
		z += 4 * y;
		setInterval(function(){
			increment();
		},  z/x );
	}else if (val === 4000){
		y += delta
		z += 2 * y;
		setInterval(function(){
			increment();
		},  z/x );
	}

}

function increment(){
	if ( userBalanceBefore < userBalance ){
		userBalanceBefore += 100;
		updateBalance(userBalanceBefore.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,'));
	}
}

// You have access to a function updateBalance which
// takes in a string and sets the ui to that value
// updateBalance("1");




//==================//
// 		Part 2	 	//
//==================//

function processSlots(input)
{	
	x = 0;
	y = 0;
	var one = {
		3: 5,
		4: 10,
		5: 20
	};
	var two = {
		3: 10,
		4: 25,
		5: 50
	};
	var three = {
		3: 25,
		4: 50,
		5: 100
	};
	arr = [1,2,3];
	win = { 1: one, 2: two, 3: three };
	wins = [];
	check = [];
	
	//Checks for rows
	for (i =0; i < input.length; i ++){ 			
		if(arr.includes(input[i][0])){				
			for (q =1; q < input[i].length; q ++){ 	 
				if(input[i][q] === input[i][0] ){	 //Checks for repeated
					x++;
				}else{
					if (x >= 2){					  //Append scores
						x++;
						wins.push(win[input[i][0]][x]);
					}
					x = 0;
					break;
				}
			}
		}
	}

	//Checks for vs
	if(arr.includes(input[0][0])){
		a = input[0][0];
		var q = 0;
		for (i = 0 ; i <input.length ; i++){
			var w = input[i].length -1 ;
			if( input[i][q] == input[i][w - q] &&  input[i][q] == a){
				check.push(input[i][q])
				check.push(input[i][w - q])
			}
			q ++;
		}
		if (check.length > 1 && check.length % input.length == 0){
			wins.push( win[a][check.length-1]);
			check = [];
		}
	} 

	if(arr.includes(input[input.length-1][0])){
		a = input[input.length-1][0];
		var q = 0;
		for  (i = input.length-1 ; i >= 0 ; i--){
			var w = input[i].length -1 ;
			if( input[i][q] == input[i][w - q] &&  input[i][q] == a){
				check.push(input[i][q])
				check.push(input[i][w - q])
			}
			q ++;
		}
		if (check.length > 1 && check.length % input.length == 0){
			wins.push( win[a][check.length-1]);
			check = [];
		}
	}
	
	if (wins.length > 1 ){
		var arrSum =0;
		for(i=0;i<wins.length;i++){arrSum += wins[i]}
		str = `'${wins.length} winning lines, scoring a total ${arrSum} points.'`
	}else if (wins.length == 1 ) {
		var arrSum =0;
		for(i=0;i<wins.length;i++){arrSum += wins[i]}
		str = `'${wins.length} winning line, scoring ${arrSum} points.'`
	}
	console.log("Output: " + str);
};

// examples input
var array = [
	[1,0,0,0,1],
	[0,1,0,1,0],
	[0,0,1,0,0]
];
//Output: '1 winning line, scoring 20 points.'

var array2 = [
	[2,4,2,2,3],
	[1,1,1,4,1],
	[3,3,3,4,2]
];
//Output: '2 winning lines, scoring a total 30 points.'

var array3 = [
	[0,0,3,0,0],
	[0,3,0,3,0],
	[3,0,0,0,3]
];
var array4 = [
	[2,0,2,0,2],
	[2,2,2,2,0],
	[2,0,2,0,2]
];

processSlots(array)