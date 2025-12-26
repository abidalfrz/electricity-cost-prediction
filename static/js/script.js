particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 80, 
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#ffffff" 
        },
        "shape": {
            "type": "circle",
            "stroke": {
                "width": 0,
                "color": "#000000"
            }
        },
        "opacity": {
            "value": 0.3, 
            "random": false,
            "anim": {
                "enable": false
            }
        },
        "size": {
            "value": 3, 
            "random": true,
            "anim": {
                "enable": false
            }
        },
        "line_linked": {
            "enable": true, 
            "distance": 150, 
            "color": "#ffffff", 
            "opacity": 0.2, 
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 2, 
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 1200
            }
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": true, 
                "mode": "grab" 
            },
            "onclick": {
                "enable": true,
                "mode": "push" 
            },
            "resize": true
        },
        "modes": {
            "grab": {
                "distance": 180, 
                "line_linked": {
                    "opacity": 0.5
                }
            },
            "repulse": {
                "distance": 100,
                "duration": 0.4
            }
        }
    },
    "retina_detect": true
});

document.addEventListener('DOMContentLoaded', () => {
    
    const counter = document.getElementById('cost-counter');
    
    if (counter) {
        const target = +counter.getAttribute('data-target'); 
        const duration = 2000; 
        const increment = target / (duration / 16); 

        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.innerText = Math.ceil(current).toLocaleString('en-US');
                requestAnimationFrame(updateCounter);
            } else {
                counter.innerText = target.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            }
        };

        updateCounter();
    }

    const alerts = document.querySelectorAll('.alert');
    if (alerts) {
        setTimeout(() => {
            alerts.forEach(alert => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            });
        }, 10000);
    }
});