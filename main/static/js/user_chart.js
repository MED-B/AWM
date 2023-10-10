// user_chart.js

// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function () {
    // Make an AJAX request to get user distribution data
    $.ajax({
        url: url_user_info,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // Call a function to create the pie chart
            createPieChart(data);
        },
        error: function (error) {
            console.error('Error fetching user distribution data:', error);
        }
    });
});

// Function to create the pie chart
function createPieChart(data) {
    // Get the pie chart container
    var pieChartCanvas = document.getElementById('userPieChart');

    // Create a new Chart instance
    var pieChart = new Chart(pieChartCanvas, {
        type: 'pie',
        data: {
            labels: ['Buyers', 'Vendors', 'Both'],
            datasets: [{
                data: [data.buyers, data.vendors, data.both],
                backgroundColor: ['red', 'green', 'blue'],
            }],
        },
    });

    
}
