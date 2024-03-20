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
