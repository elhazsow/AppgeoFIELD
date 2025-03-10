const canvas = document.getElementById('line_chart');
ctx = canvas.getContext('2d');
const mychart = new Chart(ctx, {
    type: 'line',
    data : {
        labels: [],
        datasets: [{
        label: "#Graph NDVI",
        data: [],
        fill: false,
        borderColor: 'rgb(10, 245, 20)',
        tension: 0.1
        }]
    },
    options: {
        animation: {
        duration: 500,
        easing: "linear",
        },

        maintainAspectRatio: false,
        scales: {
        y:{
            beginAtZero:true
        },
        x: {
            type: 'timeseries',
            /*time: {
                displayFormats: {
                    unit: 'month',
                    unitStepSize: 6,
                },
                ticks: {
                    font: {
                        //size: 20,
                        weight: "bold",
                        color: 'rgb(10, 245, 20)',
                    },
            
                    minRotation: 45,
                    //count: 3,
                    stepSize: 20,
                    // autoSkip: false
                    },
            }*/
        }
        }
    }
    });
