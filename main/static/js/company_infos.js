
document.addEventListener('DOMContentLoaded', function () {
    // Get the element where you want to display the number of projects
    const factories = document.getElementById('factories');
    const expositions = document.getElementById('expositions');
    const certificates = document.getElementById('certificates');
    
    // Fetch the data using AJAX
    fetch(url_general_infos)
      .then(response => response.json())
      .then(data => {
        // Update the text of the project count element with the number of projects
        
        factories.textContent = data.factory_count;
        expositions.textContent = data.exposition_count;
        certificates.textContent = data.certificate_count;
      })
      .catch(error => {
        console.error('Error fetching project count:', error);
      });
    
    
    });