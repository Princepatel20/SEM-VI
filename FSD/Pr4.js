const http = require("http");
const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("This is the http server!!");
});
const PORT = 8085;
server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}/`);
});
