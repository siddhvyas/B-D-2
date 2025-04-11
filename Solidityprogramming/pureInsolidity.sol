pragma solidity ^0.8.20; 


contract Pure{

    uint256 num1 = 4;
    uint256 num2 = 10;

    function getData() public pure returns(uint256, uint256){

        uint256 muNum1 = 30;
        uint256 muNum2 = 30;

        uint256 product = muNum1 * num1;
        uint256 total = muNum2 * num2;
        return (product, total);
    }
}