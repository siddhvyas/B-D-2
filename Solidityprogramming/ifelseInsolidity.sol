pragma solidity ^0.8.20;


contract ifelse{

    uint256 public myNum = 5;
    string public myString;

    function get(uint256 _num) public returns(string memory){

        if (_num == 5){
            myString = "Hey the value of muNum is 5";
        }
        else{
            myString = "Not 5";
        }
    }
}