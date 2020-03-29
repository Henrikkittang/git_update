const express = require('express');
const schedule = require('node-schedule'); 

const app = express();
app.listen(8050, () => {console.log(`listening at port 8050`)});
app.use(express.static('public'));
app.use(express.json({limit: '2mb'}));


const jobb = schedule.scheduleJob('* */15 * * * *', () => {        
    const { spawn } = require('child_process');
    const pyProg = spawn('python', ['update.py']);
});

