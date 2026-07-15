function addredclass(){
  document.querySelector('header').classList += "red";
}
let red_header  = document.querySelector("#red_header");
red_header.addEventListener("click", addredclass);
