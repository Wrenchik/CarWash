document.addEventListener('DOMContentLoaded', function () {
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('overlay');
    const toggleBtn = document.getElementById('toggleDrawer');

    toggleBtn.addEventListener('click', () => {
    const isOpen = drawer.classList.toggle('open');
    overlay.classList.toggle('visible', isOpen);
    document.body.classList.add('no-scroll');
    });

    overlay.addEventListener('click', () => {
    drawer.classList.remove('open');
    overlay.classList.remove('visible');
    document.body.classList.remove('no-scroll');
    });

    const bookingDrawer = document.getElementById('booking-drawer');
    const bookingOverlay = document.getElementById('booking-overlay');
    const bookingToggleBtn = document.getElementById('booking-toggleDrawer');

    bookingToggleBtn.addEventListener('click', () => {
    const bookingIsOpen = bookingDrawer.classList.toggle('open');
    bookingOverlay.classList.toggle('visible', bookingIsOpen);
    document.body.classList.add('no-scroll');
    });

    bookingOverlay.addEventListener('click', () => {
    bookingDrawer.classList.remove('open');
    bookingOverlay.classList.remove('visible');
    document.body.classList.remove('no-scroll');
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

document.addEventListener('DOMContentLoaded', function() {
    const nextReviewsBtn = document.querySelector('#next-reviews');

    if (nextReviewsBtn) {
        nextReviewsBtn.closest('.arrow-right').addEventListener('click', function(e) {
            e.preventDefault();
            const currentPage = parseInt(this.getAttribute('data-page')) || 1;
            const nextPage = currentPage + 1;

            fetch(`/load_reviews/?page=${nextPage}`)
                .then(response => response.json())
                .then(data => {
                    if (data.html) {
                        document.getElementById('reviews-container').insertAdjacentHTML('beforeend', data.html);
                        this.setAttribute('data-page', nextPage);

                        if (!data.has_next) {
                            this.style.display = 'none';
                        }
                    }
                })
                .catch(error => console.error('Error loading reviews:', error));
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
  const btnGuest = document.getElementById('open-booking-guest');
  const modal   = document.getElementById('guest-modal');
  const close   = modal?.querySelector('.guest-modal-close');

  btnGuest?.addEventListener('click', () => {
    modal.classList.remove('hidden');
  });
  close?.addEventListener('click', () => {
    modal.classList.add('hidden');
  });
  // клик по фону
  modal?.addEventListener('click', e => {
    if (e.target === modal) modal.classList.add('hidden');
  });
});


document.addEventListener('DOMContentLoaded', () => {
  const guestBtn = document.getElementById('open-booking-guest');
  const warning = document.getElementById('auth-warning');

  guestBtn?.addEventListener('click', () => {
    // Сначала сделаем элемент видимым
    warning.classList.remove('hidden');
    warning.classList.add('visible');

    // Спустя 3 секунды уберём видимость
    setTimeout(() => {
      warning.classList.remove('visible');
      // Ещё через полсекунды полностью прячем
      setTimeout(() => warning.classList.add('hidden'), 500);
    }, 3000);
  });
});
