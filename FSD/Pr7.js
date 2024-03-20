const path = require('path');
const os = require('os');
const util = require('util');
console.log('--- Path Module ---');
const filePath = '/path/to/example.txt';
console.log('File name:', path.basename(filePath));
console.log('Directory name:', path.dirname(filePath));
console.log('File extension:', path.extname(filePath));
console.log('\n--- OS Module ---');
console.log('OS type:', os.type()); //
console.log('OS platform:', os.platform());
console.log('Total memory (GB):', os.totalmem() / (1024 * 1024 * 1024));
console.log('\n--- Util Module ---');
const promisify = util.promisify;
const delay = promisify(setTimeout);
const asyncFunction = async () => {
await delay(2000);
return 'Async function completed';
  };
asyncFunction().then(result => console.log('Result:', result));
