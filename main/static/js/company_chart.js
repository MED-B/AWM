document.addEventListener('DOMContentLoaded', function () {
  // Make an AJAX request to get company information
  $.ajax({
    url: url_company_info, // Replace with the actual URL pattern name
    type: "GET",
    dataType: "json",
    success: function (data) {
        const companies = document.getElementById('companies');
        companies.textContent = data.total_companies;
      // Create a pie chart with the retrieved data
      createPieChart(data);
    },
    error: function (error) {
      console.error("Error fetching company information:", error);
    },
  });

  // Function to create the pie chart
  function createPieChart(data) {
    var ctx = document.getElementById("companyPieChart").getContext("2d");
    var pieChart = new Chart(ctx, {
      type: "pie",
      data: {
        labels: ["Certified Companies", "Uncertified Companies"],
        datasets: [
          {
            data: [data.certified_companies, data.uncertified_companies],
            backgroundColor: ["#36a2eb", "#ff6384"],
          },
        ],
      },
    });
  }
});



//company bars charts code 

document.addEventListener('DOMContentLoaded', async function () {

    // Function to fetch company information from the server
    async function fetchCompanyInfo() {
        const response = await fetch(url_company_info, { method: 'GET', headers: { 'Accept': 'application/json' } });
        return await response.json();
    }

    // Fetch company information
    const companyInfo = await fetchCompanyInfo();

    // Extract data for the bar chart
    const companyTypeLabels = companyInfo.company_type_distribution.map(item => item.company_type);
    const companyTypeCounts = companyInfo.company_type_distribution.map(item => item.count);

    // Create a bar chart
    const ctx = document.getElementById('companyTypeBarChart').getContext('2d');
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: companyTypeLabels,
            datasets: [{
                label: 'Company Type Distribution',
                data: companyTypeCounts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Bar color
                borderColor: 'rgba(75, 192, 192, 1)', // Border color
                borderWidth: 1,
            }],
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Company Type',
                    },
                },
                x: {
                    title: {
                        display: true,
                        text: 'Count',
                    },
                    ticks: {
                        stepSize: 1, // Specify the step size for X-axis
                        precision: 0, // Display integers only
                    },
                },
            },
        },
    });

});