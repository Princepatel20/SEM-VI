Program:

User.jsx

const mongoose = require('mongoose');
const userSchema = new mongoose.Schema({
name: String,
email: String,
age: Number,
});
module.exports = userSchema;
db.jsx
const mongoose = require("mongoose");
mongoose
.connect("mongodb://localhost:27017/?directConnection=true", {
useNewUrlParser: true,
useUnifiedTopology: true,
})
.then(() => console.log("Connected to MongoDB"))
.catch((err) => console.error("Error connecting to MongoDB:", err));
module.exports = mongoose;

crud.jsx

const mongoose = require("./db.jsx");
const userSchema = require("./models/user");
const User = mongoose.model("User", userSchema);
const main = async () => {
try {
const newUser = await User.create({
name: "Vaidik Ghelani",
email: "Vaid@example.com",
age: 22,
});
console.log("New user created:", newUser);
const allUsers = await User.find();
console.log("All users:", allUsers);
const updatedUser = await User.findOneAndUpdate(
{ name: "Vaidik Ghelani" },
{ age: 20 },
{ new: true }
);
console.log("Updated user:", updatedUser);
const deletedUser = await User.findOneAndDelete({ name: "Vaidik Ghelani" });
console.log("Deleted user:", deletedUser);
const remainingUsers = await User.find();
console.log("Remaining users:", remainingUsers);
} catch (error) {
console.error("Error:", error);
} finally {
mongoose.disconnect();
  }
};
main();
