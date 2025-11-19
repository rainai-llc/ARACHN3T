// map.mjs
const hub = document.getElementById("hubId");
const vectorLayer = document.getElementById("vector-layer");

let dotCount = 0;
let isConnecting = false;
const dotElements = {}; // Store dot elements here

hub.addEventListener('click', async function(event) {
    if (isConnecting) {
        console.log("Already connecting dots. Please wait.");
        return;
    }

    // Reset dotCount and other state for a new click
    dotCount = 0;
    isConnecting = true;
    console.log("Click was triggered. Creating and connecting dots one by one.");

    // Clear existing dots and lines from previous clicks
    // Optional, but recommended for clean updates
    document.querySelectorAll('.dot').forEach(dot => dot.remove());
    document.querySelectorAll('.vector-line').forEach(line => line.remove());
    Object.keys(dotElements).forEach(key => delete dotElements[key]);

    function createAndConnectNextDot() {
        if (dotCount > 28) {
            console.log("All dots have been created and connected.");
            isConnecting = false;
            fetchDotDataAndUpdate(); // All dots are created. Now, fetch the data.
            return;
        }
        const newDot = document.createElement('div');
        newDot.className = `dot dot${dotCount}`;
        document.body.appendChild(newDot);

        // Store a reference to the new dot element
        dotElements[dotCount] = newDot;

        // Use 'newDot' to add a placeholder until data arrives
        const newText = document.createElement('p');
        newText.textContent = "Loading...";
        newDot.appendChild(newText);

        const hubRect = hub.getBoundingClientRect();
        const hubX = hubRect.left + hubRect.width / 2;
        const hubY = hubRect.top + hubRect.height / 2;
        const hubRadius = hubRect.width / 2;

        const dotRect = newDot.getBoundingClientRect();
        const dotX = dotRect.left + dotRect.width / 2;
        const dotY = dotRect.top + dotRect.height / 2;

        const dx = dotX - hubX;
        const dy = dotY - hubY;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance > 0) {
            const lineStartX = hubX + (dx / distance) * hubRadius;
            const lineStartY = hubY + (dy / distance) * hubRadius;

            const newLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
            newLine.setAttribute("class", "vector-line");
            newLine.setAttribute("x1", lineStartX);
            newLine.setAttribute("y1", lineStartY);
            newLine.setAttribute("x2", dotX);
            newLine.setAttribute("y2", dotY);

            vectorLayer.appendChild(newLine);
        }

        dotCount++;
        setTimeout(createAndConnectNextDot, 1);
    }

    async function fetchDotDataAndUpdate() {
        try {
            const response = await fetch('http://localhost:3001/api/get-dot-data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // if (Array.isArray(data)) {
            //     // Find the first object in the array that has a 'Total' property.
            //     const itemWithTotal = data.find(item => 'Total' in item);
            //
            //     // If an item with 'Total' was found...
            //     if (itemWithTotal) {
            //         const dbTotal = itemWithTotal.Total;
            //         const tmpHeader = document.getElementById('hubId');
            //         if (tmpHeader) {
            //             const dbSize = document.createElement('h3');
            //             dbSize.textContent = `Total: ${dbTotal}`;
            //             tmpHeader.appendChild(dbSize);
            //         }
            //     }
            // }

            if (Array.isArray(data) && data.length <= 29) {
                console.log('Received new dot data from server:', data);

                data.forEach(item => {
                    const dotId = item.id;
                    const dotText = item.text;
                    const dotUrl = item.url;
                    const targetDot = dotElements[dotId];

                    if (targetDot) {
                        targetDot.innerHTML = '';

                        const linkElement = document.createElement('a');
                        linkElement.href = dotUrl;
                        linkElement.textContent = dotUrl;
                        linkElement.target = "_blank"; // Open link in a new tab

                        // Append a paragraph wrapper if you want to keep the centering CSS
                        const pWrapper = document.createElement('p');
                        pWrapper.appendChild(linkElement);
                        targetDot.appendChild(pWrapper);

                        console.log(`Updated dot ${dotId} with link: ${dotText}`);
                    } else {
                        console.warn(`Dot element with ID ${dotId} not found, cannot update.`);
                    }
                });
            } else {
                console.error('Received malformed data for dot updates:', data);
            }
        } catch (error) {
            console.error('Error fetching dot data:', error);
        }
    }

    // Start the dot creation process
    createAndConnectNextDot();
});
