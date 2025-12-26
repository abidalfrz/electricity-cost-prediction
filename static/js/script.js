document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Result Counter Animation
    const counter = document.getElementById('cost-counter');
    
    if (counter) {
        const target = +counter.getAttribute('data-target'); // Ambil nilai cost
        const duration = 2000; // Durasi animasi dalam ms
        const increment = target / (duration / 16); // 60fps

        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                // Format angka dengan koma (misal: 1,200.00)
                counter.innerText = Math.ceil(current).toLocaleString('en-US');
                requestAnimationFrame(updateCounter);
            } else {
                counter.innerText = target.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            }
        };

        updateCounter();
    }

    // 2. Auto-hide Flash Messages after 5 seconds
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