pragma solidity >=0.4.22 <0.9.0;  
/// @title A contract for demonstrate payable functions and addresses
/// @author Jitendra Kumar
/// @notice For now, this contract just show how payable functions and addresses can receive ether into the contract
contract Reentrancy {
    mapping(address => uint) public balance;
 
    function deposit() public payable {
        balance[msg.sender] += msg.value;
    }
 
    function withdraw() public payable {
        require(balance[msg.sender] >= msg.value);
        payable(msg.sender).transfer(msg.value);
        balance[msg.sender] -= msg.value;
    }
}
