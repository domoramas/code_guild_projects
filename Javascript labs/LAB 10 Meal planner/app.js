let results = document.getElementById("results");
let searchTerm = document.getElementById('search-term');
let searchBtn = document.getElementById("search-btn");
let mealTypes = document.getElementById("checkboxes");

searchBtn.addEventListener("click", function(e){
  let req = new XMLHttpRequest();
  let searchText = ((searchTerm.value).split(' ').join("+"));

  console.log(searchText)
  
  req.addEventListener("progress", function(e) {
    console.log(`Request ${e.loaded/e.total * 100}% complete`)
  });

  req.addEventListener("error", function (e){
    results.innerText =`oh no error ${e.status}`;
  });

  req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    var recipes = response.matches;
    console.log(recipes)
    for (let i=0; i< recipes.length; i++) {
      let resultDiv= document.createElement("div");
      resultDiv.innerHTML = `
      <p>${recipes[i].recipeName}</p>
      <button>+</button>`;
      resultDiv.setAttribute("class", "resultframes");
      resultDiv.setAttribute("style",`background-image:url('${recipes[i].imageUrlsBySize[90]}'); background-repeat: no-repeat; background-size: cover`);
      results.appendChild(resultDiv);
    }
});

  req.open("GET", `http://api.yummly.com/v1/api/recipes?_app_id=${appId}&_app_key=${apiKey}&q=${searchText}&requirePictures=true&nutrition.ENERC_KCAL.{300|600}`);
  console.log( `http://api.yummly.com/v1/api/recipes?_app_id=${appId}&_app_key=${apiKey}&q=${searchText}`)
  req.send();
})

var vue = new Vue({
  el: "#results",
  prop: ["recipes"],
  data: {
  },
  methods: {
  }

})