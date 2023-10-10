// desitribution of companies per sectors
document.addEventListener('DOMContentLoaded', async function () {

    // Function to fetch sector distribution information from the server
    async function fetchSectorDistribution() {
        const response = await fetch(url_sector_distribution, { method: 'GET', headers: { 'Accept': 'application/json' } });
        return await response.json();
    }

    // Fetch sector distribution information
    const sectorDistribution = await fetchSectorDistribution();

    // Extract data for the bar chart
    const sectorNames = sectorDistribution.company_distribution.map(item => item.sectorid__name);
    const companyCounts = sectorDistribution.company_distribution.map(item => item.company_count);

    // Create a bar chart
    const ctx = document.getElementById('companySectorBarChart').getContext('2d');
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sectorNames,
            datasets: [{
                label: 'Companies Count per Sector',
                data: companyCounts,
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
                        text: 'Sector',
                    },
                    ticks: {
                        stepSize: 1, // Specify the step size for Y-axis
                        precision: 0, // Display integers only
                    },
                },
                x: {
                    title: {
                        display: true,
                        text: 'Companies Count',
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
document.addEventListener('DOMContentLoaded', async function () {
    // Function to fetch sector distribution information from the server
    async function fetchSectorDistribution() {
        const response = await fetch(url_sector_distribution, { method: 'GET', headers: { 'Accept': 'application/json' } });
        return await response.json();
    }

    // Fetch sector distribution information
    const sectorDistribution = await fetchSectorDistribution();

    // Extract data for the product distribution bar chart
    const productSectorLabels = sectorDistribution.product_distribution.map(item => item.sectorid__name);
    const productSectorCounts = sectorDistribution.product_distribution.map(item => item.product_count);

    // Create a product distribution bar chart
    const productCtx = document.getElementById('productSectorBarChart').getContext('2d');
    const productBarChart = new Chart(productCtx, {
        type: 'bar',
        data: {
            labels: productSectorLabels,
            datasets: [{
                label: 'Products per Sector',
                data: productSectorCounts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
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
                        text: 'Sector',
                    },
                    
                },
                x: {
                    title: {
                        display: true,
                        text: 'Product Count',
                    },
                    ticks: {
                        stepSize: 1,
                        precision: 0,
                    },
                },
            },
        },
    });

    // Extract data for the average rating distribution bar chart
    const avgRatingSectorLabels = sectorDistribution.review_distribution.map(item => item.productid__sectorid__name);
    const avgShippingRating = sectorDistribution.review_distribution.map(item => item.avg_shipping_rating);
    const avgProductQualityRating = sectorDistribution.review_distribution.map(item => item.avg_productquality_rating);
    const avgSalesServicesRating = sectorDistribution.review_distribution.map(item => item.avg_salesservices_rating);

    // Create an average rating distribution bar chart
    const avgRatingCtx = document.getElementById('avgRatingSectorBarChart').getContext('2d');
    const avgRatingBarChart = new Chart(avgRatingCtx, {
        type: 'bar',
        data: {
            labels: avgRatingSectorLabels,
            datasets: [
                {
                    label: 'Average Shipping Rating',
                    data: avgShippingRating,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                },
                {
                    label: 'Average Product Quality Rating',
                    data: avgProductQualityRating,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                },
                {
                    label: 'Average Sales Services Rating',
                    data: avgSalesServicesRating,
                    backgroundColor: 'rgba(255, 205, 86, 0.2)',
                    borderColor: 'rgba(255, 205, 86, 1)',
                    borderWidth: 1,
                },
            ],
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Sector',
                    },
                    
                },
                x: {
                    title: {
                        display: true,
                        text: 'Average Rating',
                    },
                    ticks: {
                        stepSize: 1,
                        precision: 0,
                    },
                },
            },
        },
    });
});