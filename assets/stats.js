// Get the user's IP address using a third-party API
fetch('https://api.ipify.org?format=json')
  .then(response => response.json())
  .then(data => {
    const ipAddress = data.ip;

    // Get the user's country using a third-party API
    fetch(`https://ipapi.co/${ipAddress}/country_name/`)
      .then(response => response.text())
      .then(country => {
        // Get the current visit count from Local Storage and increment it
        let visitCount = parseInt(localStorage.getItem('visitCount')) || 0;
        visitCount++;

        // Store the new visit count and country in Local Storage
        localStorage.setItem('visitCount', visitCount);
        localStorage.setItem('country', country);

        // Display the visit count and country on the HTML page
        const visitCountSpan = document.getElementById('visitCount');
        const countrySpan = document.getElementById('country');
        visitCountSpan.textContent = visitCount;
        countrySpan.textContent = country;

        // Create a log message with IP address, country, and visit count
        const logMessage = `IP Address: ${ipAddress}\nCountry: ${country}\nVisit Count: ${visitCount}\n\n`;

        // Create a Blob with the log message
        const blob = new Blob([logMessage], { type: 'text/plain' });

        // Create a link to download the Blob as a text file
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'log.txt';

        // Append the link to the document and trigger a click event to start the download
        document.body.appendChild(link);
        link.click();

        // Remove the link from the document
        document.body.removeChild(link);
      })
      .catch(error => console.error(error));
  })
  .catch(error => console.error(error));
