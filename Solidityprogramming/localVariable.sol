pragma solidity ^0.8.20; 

contract LocalVariables{

    uint256 public myNumber;

    function local() public pure returns(uint256){
        uint256 i = 345;
        return i;
    }

    function update() public returns(uint256){
        uint256 i = 345;
        myNumber = i;
        return myNumber;
    }

    function updatewadd() public returns(address,uint256,uint256){
        uint256 i = 345;
        myNumber = i;
        
        i += 45;
        address myAddress = address(1);
        return (myAddress, myNumber, i);
    }

}