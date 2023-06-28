function checkfill(id) {
  var inputVal = document.getElementById(id);
  if (inputVal.value == "") {
    inputVal.style.background = "#e4e4e4";
  } else {
    inputVal.style.background = "rgb(232, 240, 254)";
  }
}
