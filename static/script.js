document.addEventListener('DOMContentLoaded', function () {
    const expandableItems = document.querySelectorAll('.expandable');
    expandableItems.forEach(item => {
        item.addEventListener('click', function () {
            const details = this.querySelector('.details');
            details.classList.toggle('visible');
        });
    });

    const ctx = document.getElementById('resultChart').getContext('2d');
    const chartData = {
        labels: ['Malicious', 'Suspicious', 'Undetected'],
        datasets: [{
            label: 'Scan Results',
            data: [{{ results['data']['attributes']['last_analysis_stats']['malicious'] }}, {{ results['data']['attributes']['last_analysis_stats']['suspicious'] }}, {{ results['data']['attributes']['last_analysis_stats']['undetected'] }}],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    };

    const resultChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
