const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
const sub = require('child_process');
const port = 3000;

// In-memory storage (replace with database in production)
let items = [];


const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        res.writeHead(200); // OK status for preflight
        res.end();
        return;
    }

    if (req.method === 'POST' && req.url === '/api/mya') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { Message } = data; // Destructuring only Message since that's what's sent

                if (!Message) {
                    res.writeHead(400, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ error: 'Message is required' }));
                    return;
                }

                const newItem = {
                    id: items.length + 1,
                    Message,
                    createdAt: new Date()
                };

                items.push(newItem);
                const cleanMessage = Message.toLowerCase();
                if (cleanMessage.includes('yes')){
                    troubleShoot = true;

                }
                // Start the Python process
                const pythonProcess = sub.spawn('python3', ['netKernel.py', newItem.Message]);

                let pythonOutput = '';

                // Listen for data from the Python script's stdout
                pythonProcess.stdout.on('data', (data) => {
                    pythonOutput += data.toString();
                    console.log(`Received data from Python: ${data}`);
                });

                // Listen for the Python script to close
                pythonProcess.on('close', (code) => {
                    console.log(`Python process exited with code ${code}`);

                    // When the process is done, send the accumulated output back to the client
                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({
                        message: pythonOutput.trim() || 'No message received from agent.',
                                           item: newItem
                    }));
                });

                // Handle errors from the Python script
                pythonProcess.stderr.on('data', (data) => {
                    console.error(`Python stderr: ${data}`);
                    // Optionally send an error message to the client
                    // res.writeHead(500, { 'Content-Type': 'application/json' });
                    // res.end(JSON.stringify({ error: `Python script error: ${data}` }));
                });
            } catch (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({
                    error: 'Server error',
                    details: error.message
                }));
            }
        });
    } else if (req.method === 'GET' && req.url === '/api/mya') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(items));
    } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Route not found' }));
    }
});

server.on('error', (error) => {
    console.error('Server error:', error);
});

server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
