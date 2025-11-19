// server.js
const express = require('express');
const http = require('http');
const { spawn } = require('child_process');
const path = require('path');
const cors = require('cors');

const app = express();
const server = http.createServer(app);

const port = 3001;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// --- NEW: Endpoint to get data for dots on demand ---
app.post('/api/get-dot-data', (req, res) => {
    console.log('User click received. Spawning agent.py to get new dot data...');

    const pythonScriptPath = path.join(__dirname, 'arachnet.py');
    const pythonProcess = spawn('python3', [pythonScriptPath]);

    let pythonOutput = '';
    let pythonError = '';

    // Capture stdout data from the Python process
    pythonProcess.stdout.on('data', (data) => {
        pythonOutput += data.toString();
    });

    // Capture stderr data from the Python process
    pythonProcess.stderr.on('data', (data) => {
        pythonError += data.toString();
    });

    // When the Python process exits, handle the captured output
    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.error(`Python script exited with code ${code}. Error: ${pythonError}`);
            return res.status(500).json({ error: 'Failed to run Python script', details: pythonError });
        }

        try {
            // Attempt to parse the JSON output from the Python script
            const dotData = JSON.parse(pythonOutput);
            console.log('Successfully received data from Python script.');
            // Send the JSON data back to the client
            res.status(200).json(dotData);
        } catch (jsonError) {
            console.error('Failed to parse Python output as JSON:', pythonOutput);
            res.status(500).json({ error: 'Invalid data format from Python script', details: pythonOutput });
        }
    });

    // Handle errors in spawning the Python script itself
    pythonProcess.on('error', (err) => {
        console.error(`Failed to start Python process: ${err.message}`);
        res.status(500).json({ error: 'Failed to start Python process', details: err.message });
    });
});

// GET all items (for initial load if needed)
app.get('/api/loop', (req, res) => {
    // This endpoint remains if you have other uses for it
    res.status(200).json([]); // Or your existing data
});

// Handle routes not found
app.use((req, res) => {
    res.status(404).json({ error: 'Route not found' });
});

// Listen on the HTTP server
server.listen(port, () => {
    console.log(`Express server running at http://localhost:${port}`);
    console.log(`POST to http://localhost:${port}/api/get-dot-data to fetch new dot data.`);
});
