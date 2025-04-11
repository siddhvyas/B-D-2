pragma solidity ^0.8.20;
contract WhileLoop{
//while (condition)
uint256[]data;
uint8 k = 0;
function loop()public returns (uint256[] memory){
while(k < 5){
k++;
data.push(k);
}
return data;
}
}
contract DoWhile{
uint256[]data;
uint8 j = 0;
function loop()public returns(uint256[] memory){
do{
j++;
data.push(j);
}while(j < 5);
return data;
}
}