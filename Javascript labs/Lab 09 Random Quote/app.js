let target = document.getElementById("target");
let Btn = document.getElementById("button");
let sTarget = document.getElementById("s-results");
let searchBtn = document.getElementById("search-btn");
let search = document.getElementById("search");
let previous = document.getElementById("previous");
let next = document.getElementById("next");
let pageNum = document.getElementById("page-num");
let searchBy = document.getElementById("searchby");

Btn.addEventListener("click", function(e){
    let req = new XMLHttpRequest();

req.addEventListener("progress", function(e) {
    target.innerText =`Request ${e.loaded/e.total *100}% complete`
});

req.addEventListener("error", function (e){
    target.innerText =`oh no error ${e.status}`;
});

req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    let resultHTML = `
        <h2>${response.quote.body}</h2>
        <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
        `
    target.innerHTML = resultHTML;
});

req.open("GET", "https://favqs.com/api/qotd");
req.send();
})




searchBtn.addEventListener("click", function(e){
    let req = new XMLHttpRequest();
    let searchVal = document.querySelector('input[name=searchby]:checked').value
    
    let searchText = ((search.value).split(' ').join("+"));

    console.log(searchText, searchVal);
    let pageId = 1;
    
    let quotes = document.getElementsByTagName("li");
    for (let i=(quotes.length -1); i >= 0; i--){
        sTarget.removeChild(quotes[i]);      // removes old list when new search is initiated
    }
req.addEventListener("progress", function(e) {
    console.log(`Request ${e.loaded/e.total * 100}% complete`)
});

req.addEventListener("error", function (e){
    sTarget.innerText =`oh no error ${e.status}`;
});

req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    pageNum.innerText = `pg. ${pageId}`;
    for (let i=0; i< response.quotes.length; i++){
        let li = document.createElement("li");
        li.innerHTML = `<p>${response.quotes[i].body}<i><a href="${response.quotes[i].url}"> ~${response.quotes[i].author}</a></i></p>`;
        sTarget.appendChild(li);
    }
});
next.addEventListener("click", function(){
    let response = JSON.parse(req.responseText);
    if (response.last_page === false){
        pageId += 1;
    for (let i=(quotes.length -1); i >= 0; i--){
        sTarget.removeChild(quotes[i]);};   
    req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}${searchVal}`);
    req.setRequestHeader("Authorization", `Token token="${apiKey}"`);
    req.send();
    }  
});
previous.addEventListener("click", function(){
    if (pageId >1 ){
    pageId -=1;
    for (let i=(quotes.length -1); i >= 0; i--){
        sTarget.removeChild(quotes[i]);}; 
    req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}${searchVal}`);
    req.setRequestHeader("Authorization", `Token token="${apiKey}"`);
    req.send();}
});

req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}${searchVal}`);
console.log( `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}${searchVal}`)
req.setRequestHeader("Authorization", `Token token="${apiKey}"`);
req.send();
})


