pragma solidity ^0.8.20; 

contract StateVariables{


    string public myState;
    uint public myNum;

    string public defaultText = "hey Default Text";
    uint256 public defaultNum = 5;


    bytes public defaultbyte = "hey default";
    bytes public defaultbyteno;

    uint256[] public myNumber;

    constructor( string memory _text, uint _no){
        myState = _text;
        myNum = _no;
    }

    function update (string memory _text, uint _no) public {
        myState = _text;
        myNum = _no;
    }
    
}