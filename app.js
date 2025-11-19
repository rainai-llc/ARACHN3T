const express = require('express');
const path = require('path');
const sub = require('child_process');
const { writeHeapSnapshot } = require('v8'); // This seems unused, consider removing
const app = express();
const port = 80;
const session = require('express-session');

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));
// Serve static files (CSS, images, etc.) - Make sure 'public' is correct
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

// Set up session middleware
app.use(session({
    secret: '5e3b1a82e45eba6ec95cc2a9f455c473e0665d1666081bdae284012d7a2f36719a773932000322d7e04707975a6aa967d1923954582734fad0078ce3f17fc957',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'demo.html'));
    }
);


app.get('/home', (req, res) => {
    res.sendFile(path.join(__dirname, 'home.html'));
});


app.get('/mya', (req, res) => {
    res.sendFile(path.join(__dirname, 'mya.html'));
});

app.get('/demo', (req, res) => {
    res.sendFile(path.join(__dirname, 'demo.html'));
});

app.get('/database', (req, res) => {
    res.sendFile(path.join(__dirname, 'database.html'));
});

app.get('/forms/:formName', (req, res) => {
    const formName = req.params.formName;
    const formPath = path.join(__dirname, 'forms', `${formName}.html`);
    res.sendFile(formPath, (err) => {
        if (err) {
            res.status(404).send('Just a void :/')
        }
    });
});


// Route to serve dynamic profile.html pages
app.get('/:team/profile.html', (req, res) => {
    const { team } = req.params;
    const profilePath = path.join(__dirname, team, 'profile.html');
    res.sendFile(profilePath, (err) => {
        if (err) {
            console.error(`Error serving profile.html for ${team}:`, err);
            // If the profile.html doesn't exist, redirect to maintenance
            res.redirect('/maintenance');
        }
    });
});

app.post('/test', (req, res) => {
    const userPosition = req.body.position; // This is not used but kept from original
    const { rainaiTarget } = req.body;

    if (!rainaiTarget) {
        return res.status(400).send('Target URL is required.');
    }
    const statsDat = `[SCAN]: ${rainaiTarget}`;
    console.log(`Calling: ${statsDat}`);

    let pythonOutput = '';
    const pythonError = [];

    const dashBuildProcess = sub.spawn('python3', [path.join(__dirname, 'scripts', 'build', 'dashbuild.py'), statsDat]);

    dashBuildProcess.stdout.on('data', (data) => {
        pythonOutput += data.toString();
        console.log(`Python stdout: ${data.toString()}`);
    });

    dashBuildProcess.stderr.on('data', (data) => {
        pythonError.push(data.toString());
        console.error(`Python stderr: ${data.toString()}`);
    });

    dashBuildProcess.on('close', (code) => {
        const formattedTarget = rainaiTarget.replace(/^(https?:\/\/)+|\s+/g, '');

        if (code === 0) {
            if (pythonOutput.includes(`PROFILE_GENERATED:${formattedTarget}/profile.html`)) {
                const redirectUrl = `/${formattedTarget}/profile.html`;
                console.log(`Python script succeeded. Redirecting to: ${redirectUrl}`);
                res.redirect(redirectUrl);
            } else {
                console.error("Python script succeeded but didn't output expected success message. Redirecting to maintenance.");
                res.redirect('/mya');
            }
        } else {
            console.error(`Python script exited with code ${code}. Errors: ${pythonError.join('')}. Redirecting to maintenance.`);
            res.redirect('/mya');
        }
    });

    dashBuildProcess.on('error', (err) => {
        console.error('Failed to start dashbuild.py child process:', err);
        res.status(500).send('Internal server error: Could not start processing script.');
    });
});
// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
