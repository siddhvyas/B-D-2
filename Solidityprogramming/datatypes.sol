pragma solidity ^0.8.20; 

contract DataTypes{
    bool public hey;
    bool public no = true;

    //uintx range: 0 to 2^x-1
    //positive integer
    uint8 public u8 = 1;
    uint  public u256 = 456;
    uint public u = 123;
    //integer 
    int8 public i8 = -1;
    int public i256 = 456;
    int i = -123;

    int public minInt = type(int).min;
    int public maxInt = type(int).max;

    //bytes less gas usage
    bytes1 public a = 0xb5;
    bytes1 public b = 0xb5;

    //Array
    uint256[] muNumber;

    //Address
    address public addr = 0xc0ffee254729296a45a3885639AC7E10F9d54979;

    // Default values for datatypes 
    bool public  defaultBool;
    uint public number;
    int public defaultInt;
    address public defaultaddr;
}