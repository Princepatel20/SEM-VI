const express = require("express");
const session = require("express-session");
const app = express();
app.use(
session({
secret: "ThisIsMySecretKeyVaidu11",
resave: false,
saveUninitialized: true,
cookie: { secure: false },
})
);
app.get("/", (req, res) => {
let visits = req.session.visits || 0;
visits++;
req.session.visits = visits;
res.send(`You have visited this page ${visits} times.`);
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
console.log(`Server is running on http://localhost:${PORT}`);
});
