const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

let jobs = [{
    "id": "1",
    "title": "Job A",
    "location": "N/A",
},
{
    "id": "2",
    "title": "Job B",
    "location": "N/A",
},
{
    "id": "3",
    "title": "Job C",
    "location": "N/A",
},
{
    "id": "4",
    "title": "Job D",
    "location": "N/A",
},
{
    "id": "5",
    "title": "Job E",
    "location": "N/A",
}];

// Configuring body parser middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('Hello World, from express');
});

app.post('/jobs', (req, res) => {
    const job = req.body;

    // Output the book to the console for debugging
    console.log(job);
    jobs.push(job);

    res.send('Job is added');
});

app.get('/jobs/:id', (req, res) => {
    // Reading id from the URL
    const id = req.params.id;

    // Searching books for the isbn
    for (let job of jobs) {
        if (job.id === id) {
            res.json(job);
            return;
        }
    }

    // Sending 404 when not found
    res.status(404).send('Job not found');
});

app.get('/jobs', (req, res) => {
    res.json(jobs);
});

// start up the server
app.listen(PORT, () => console.log(`Listening on ${PORT}`));