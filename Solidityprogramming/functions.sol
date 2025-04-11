//types of functions declaring function and non declaring function 
pragma solidity ^0.8.20; 

contract LearnFunction{

    uint256 public hey;
    uint256 public hello;

    function getinfo() public view returns(uint){

            return hey;
    }

    function updatedata( uint256 _hey) public {

            hey = _hey;
    }

    function getadd( uint256 _a, uint256 _b) public view returns (uint){
        
            uint256 newnumber = _a + _b;
            return newnumber;
    }

    function get( uint256 _a, uint256 _b) public{
        
            uint256 newnumber2 = _a + _b;
            hello = newnumber2;

            
    }
    
}