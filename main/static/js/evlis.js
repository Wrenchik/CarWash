document.addEventListener('DOMContentLoaded', function () {
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('overlay');
    const toggleBtn = document.getElementById('toggleDrawer');

    toggleBtn.addEventListener('click', () => {
    const isOpen = drawer.classList.toggle('open');
    overlay.classList.toggle('visible', isOpen);
    });

    overlay.addEventListener('click', () => {
    drawer.classList.remove('open');
    overlay.classList.remove('visible');
    });

    const bookingDrawer = document.getElementById('booking-drawer');
    const bookingOverlay = document.getElementById('booking-overlay');
    const bookingToggleBtn = document.getElementById('booking-toggleDrawer');

    bookingToggleBtn.addEventListener('click', () => {
    const bookingIsOpen = bookingDrawer.classList.toggle('open');
    bookingOverlay.classList.toggle('visible', bookingIsOpen);
    });

    bookingOverlay.addEventListener('click', () => {
    bookingDrawer.classList.remove('open');
    bookingOverlay.classList.remove('visible');
    });
});