// #ATM
// class for ATM functions//
class ATM{
    constructor(balance=0, intRate= .01, trans= []) {
        this.balance = balance;
        this.intRate = intRate;
        this.trans = trans;
    }
    checkBalance() {
        return this.balance
    }
    deposit(amount) {
        this.trans.push(`Deposit $${amount}`);
       return (this.balance += amount);(t)
    }
    withdrawl(amount) {
        this.trans.push(`Withdrawl $${amount}`);
        return (this.balance -= amount);
    }

    calcIntrest(){
        return (this.balance * this.intRate);
    }
    printTrans() {
        return(this.trans)
    }
}

// initates deposit //
let atm= new ATM()
let deposit = document.getElementById("deposit-start");
let depositField = document.getElementById("deposit-amount");
let depositInput = document.getElementById("deposit")
let depositEnter = document.getElementById("enter-deposit");
let output = document.getElementById("output")
// function for opening input field
function startdep() {
    withdrawlInput.style.display = "none";
    let depositInput = document.getElementById("deposit")
    depositInput.style.display = "flex";
}
function makedep(){
    let depositAmount = depositField.value;
    let amount = parseFloat(depositAmount);
    if (isNaN(amount)) {
        output.innerText= "invalid entry";
    }else {
    atm.deposit(amount);
    depositField.value= "";
    depositInput.style.display = "none";
    output.innerText = `Deposit $ ${amount}`
    }
}
// event to open the deposit field
deposit.addEventListener("click", startdep);
// event to make the deposit and close the field
depositEnter.addEventListener("click", makedep);

let withdrawl = document.getElementById("withdrawl-start");
let withdrawlField = document.getElementById("withdrawl-amount");
let withdrawlInput = document.getElementById("withdrawl")
let withdrawlEnter = document.getElementById("enter-withdrawl");

// function for opening input field
function startwith() {
    depositInput.style.display = "none";
    let withdrawlInput = document.getElementById("withdrawl")
    withdrawlInput.style.display = "flex";}

function makewith(){
    let withdrawlAmount = withdrawlField.value;
    let amount = parseFloat(withdrawlAmount);
    if (isNaN(amount)) {
        output.innerText= "invalid entry";
    }else {
        if ((atm.balance - amount)>=0) {
            atm.withdrawl(amount);
            withdrawlField.value = "";
            withdrawlInput.style.display = "none";
            output.innerText = `Withdrawl $ ${amount}`
        }else if ((atm.balance- amount)<0) {
            withdrawlField.value = "";
            withdrawlInput.style.display = "none";
            output.innerText = "Insufficient Funds"
        } 
    }
}
// event to open the withdrawl field
withdrawl.addEventListener("click", startwith);
// event to make the withdrawl and close the field
withdrawlEnter.addEventListener("click", makewith);


let balance = document.getElementById("balance");
let history = document.getElementById("history");
let transPrint = document.getElementById("trans-list");


balance.addEventListener("click", function(){
    withdrawlInput.style.display = "none";
    depositInput.style.display = "none";
    output.innerText = `Your balance is $ ${atm.checkBalance()}`
})

history.addEventListener("click", function(){
    withdrawlInput.style.display = "none";
    depositInput.style.display = "none";
    output.innerText = "";
    (atm.printTrans()).forEach(function(trans){
        let itm = document.createElement("li");
        itm.innerText = `${trans}`;
        transPrint.appendChild(itm);
    })
})
