function toggleClass(){
  header = document.querySelector('header');
  if (header.classList == "green") {
    header.classList = "red";
  } else {
    header.classList = "green";
  }
}
let toggle_header = document.querySelector("#toggle_header");
toggle_header.addEventListener("click", toggleClass);
