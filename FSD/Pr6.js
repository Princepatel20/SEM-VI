const checkNumber = (num) => {
  const result = num > 0 ? "positive" : num < 0 ? "negative" : "zero";
  console.log(`${num} is ${result}.`);
};
const getDayOfWeek = (day) => {
  let dayName;
  switch (day) {
    case 0:
      dayName = "Sunday";
      break;
    case 1:
      dayName = "Monday";
      break;
    case 2:
      dayName = "Tuesday";
      break;
    case 3:
      dayName = "Wednesday";
      break;
    case 4:
      dayName = "Thursday";
      break;
    case 5:
      dayName = "Friday";
      break;
    case 6:
      dayName = "Saturday";
      break;
    default:
      dayName = "Invalid day";
  }
  console.log(`The day is ${dayName}.`);
};
const main = () => {
  console.log("If-else statements:");
  checkNumber(10);
  checkNumber(-5);
  checkNumber(0);
  console.log("\nSwitch statement:");
  getDayOfWeek(3);
  getDayOfWeek(7);
  console.log("\nTernary operator:");
  const num = 15;
  const result = num > 10 ? "greater than 10" : "not greater than 10";
  console.log(`The number ${num} is ${result}.`);
  console.log("\nShort-circuit evaluation (and operation):");
  const x = true;
  const y = 5;
  const resultAnd = x && y;
  console.log(`The result of 'x && y' operation is: ${resultAnd}`);
};
main();
