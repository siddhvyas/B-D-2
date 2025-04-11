pragma solidity ^0.8.20;
contract Require{
function checkInput(uint256 _input) public view returns (string memory ){
require(_input >=0, "invalid uint8");
require(_input <= 255, "invalid uint8");
return "Input is Uint8";
}
function odd(uint256 _input) public view returns (bool){
require (_input % 2 !=0);
return true;
}
}