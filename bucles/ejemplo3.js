condition = false;

while (condition == false) {
  let user = "user";
  let pasw = 123;
  if (user == "user" && pasw ===1234) {
    console.log("inicio");
    //condition = true;
    break; // break statement stops the loop immediately
  } else {
    console.log("acceso denegado");
    break;
  }
}
