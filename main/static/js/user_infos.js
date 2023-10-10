
document.addEventListener('DOMContentLoaded', function () {
// Get the element where you want to display the number of projects
const total_users = document.getElementById('total_users');
const buyers = document.getElementById('buyers');
const vendors = document.getElementById('vendors');
const both = document.getElementById('both');

// Fetch the data using AJAX
fetch(url_user_info)
  .then(response => response.json())
  .then(data => {
    // Update the text of the project count element with the number of projects
    total_users.textContent = data.total_users;
    buyers.textContent = data.buyers;
    vendors.textContent = data.vendors;
    both.textContent = data.both;
  })
  .catch(error => {
    console.error('Error fetching project count:', error);
  });


});