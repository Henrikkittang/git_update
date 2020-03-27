const express = require('express');
const schedule = require('node-schedule'); 

const app = express();
app.listen(8030, () => {console.log(`listening at port 8030`)});
app.use(express.static('public'));
app.use(express.json({limit: '1mb'}));



let j = schedule.scheduleJob('*/5 * * * * *', () => {        
    const { spawn } = require('child_process');
    const pyProg = spawn('python', ['update.py']);

});

