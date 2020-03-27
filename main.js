const express = require('express');

const app = express();
app.listen(8030, () => {console.log(`listening at port 8030`)});
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}));

console.log('yes yes yes');
