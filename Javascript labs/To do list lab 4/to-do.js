// To do list

let addItem = document.getElementById("add-item")
let addBtn = document.getElementById("add-btn")
let items = document.getElementById("items")

function newItem() {
    let newEntry = addItem.value;
    let listItem = document.createElement("li");
    let checkbox = document.createElement("input");
    let deletebtn = document.createElement("button");
    deletebtn.setAttribute("type", "button");
    deletebtn.setAttribute("class","btn btn-danger btn-sm");
    checkbox.setAttribute("type", "checkbox");
    listItem.setAttribute("class", "list-group-item")
    deletebtn.innerText = "Delete";
    listItem.appendChild(checkbox);
    listItem.appendChild(document.createTextNode(newEntry));
    listItem.appendChild(deletebtn);
    items.appendChild(listItem);
    addItem.value = "";
    checkbox.addEventListener("change",function(){
        if (this.checked) { 
            listItem.style.textDecoration="line-through"; 
        }else {
            listItem.style.textDecoration= "none";
        }
    });
    deletebtn.addEventListener("click", function(){
        items.removeChild(listItem)
    })
}

addBtn.addEventListener("click", newItem);