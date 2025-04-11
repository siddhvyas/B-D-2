pragma solidity ^0.8.20; 

contract View{

    uint256 num1 = 2;
    uint256 num2 = 7;


    function getResults() public view returns(uint256, uint256){
        return (num1, num2);
    }

    function getResults2 () public view returns (uint256 product,uint256 total){
        uint256 num3 = 20;
        uint256 num4 = 30;

        product = num3 * num4;
        total = num3 + num4;

        num3 += 5;
        num4 += 7;

    } 
    function getResults3 () public view returns (uint256 ,uint256 ){
        uint256 num5 = 20;
        uint256 num6 = 30;

        uint256 product1 = num5 * num6;
        uint256 total1 = num5 + num6;

        num5 += 5;
        num6 += 7;

        return (product1, total1);

    } 
}