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

document.getElementById('load-slots').addEventListener('click', function () {
    const selectedServices = Array.from(document.querySelectorAll('input[name="services"]:checked')).map(el => el.value);
    const date = document.getElementById('date').value;

    if (!selectedServices.length || !date) {
        alert('Выберите дату и хотя бы одну услугу.');
        return;
    }

    const params = new URLSearchParams();
    selectedServices.forEach(id => params.append('services', id));
    params.append('date', date);

    fetch(`/available-slots/?${params.toString()}`)
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById('slots-container');
            container.innerHTML = '';

            if (data.available_slots && data.available_slots.length) {
                data.available_slots.forEach((slot, index) => {
                    const id = `slot_${index}`;
                    container.innerHTML += `
                        <label for="${id}">
                            <input type="radio" name="start_time" value="${slot}" id="${id}" required>
                            ${slot}
                        </label><br>
                    `;
                });
            } else {
                container.innerHTML = '<p>Нет доступных слотов на выбранную дату и услуги.</p>';
            }
        })
        .catch(error => {
            console.error('Ошибка при загрузке слотов:', error);
        });
});