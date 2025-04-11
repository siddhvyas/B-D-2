pragma solidity ^0.8.20; 

//Global Variable

contract GlobalVariable{

    address public owner;
    address public Myblockhash;
    uint256 public difficult;
    uint256 public gasLimit;
    uint256 public number;
    uint256 public timestamp;
    uint256 public value;
    uint256 public nowOn;
    address public origin;
    uint256 public gasprice;
    bytes public callData;
    bytes4 public Firstfour;

    constructor(){
        owner = msg.sender;
    }

    Myblockhash = block.coinbase;
    difficult = block.difficulty;
    gasLimit = block.gasLimit;
    number = block.number;
    timestamp = block.timestamp;
    gasprice = tx.gasprice;
    origin = tx.origin;
    callData = msg.data;
    Firstfour = msg.sig;
}