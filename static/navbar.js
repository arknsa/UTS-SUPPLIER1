document.addEventListener('DOMContentLoaded', function () {
    // Notification Functions
    function showNotification() {
        const notification = document.getElementById('notification');
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000); // Hide after 3 seconds
    }

    function closeNotification() {
        const notification = document.getElementById('notification');
        notification.classList.remove('show');
    }

    // Sidebar Toggle Function
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');

    sidebarToggle.onclick = function() {
        sidebar.classList.toggle('open');
    };
});
