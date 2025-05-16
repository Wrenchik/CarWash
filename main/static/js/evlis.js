document.addEventListener('DOMContentLoaded', function () {
    const nextServicesBtn = document.getElementById('next-services');
    nextServicesBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const page = this.dataset.page;

        fetch(`/load-services/?page=${page}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('services-container').innerHTML = data.html;

                if (data.has_next) {
                    this.dataset.page = data.next_page;
                } else {
                    this.dataset.page = 1;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    const nextReviewsBtn = document.getElementById('next-reviews');
    nextReviewsBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const page = this.dataset.page;

        fetch(`/load-reviews/?page=${page}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('reviews-container').innerHTML = data.html;

                if (data.has_next) {
                    this.dataset.page = data.next_page;
                } else {
                    this.dataset.page = 1;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    const profileIcon = document.querySelector('.login-link');
    const drawer = document.getElementById('profileDrawer');
    const drawerContent = drawer.querySelector('.drawer-content');
    const closeBtn = document.getElementById('closeDrawer');

    profileIcon.addEventListener('click', function (e) {
        e.preventDefault();
        drawer.classList.add('open');
    });

    closeBtn.addEventListener('click', function () {
        drawer.classList.remove('open');
    });

    document.addEventListener('click', function (e) {
        const isClickInside = drawer.contains(e.target);
        const isButton = profileIcon.contains(e.target);
        if (!isClickInside && !isButton) {
            drawer.classList.remove('open');
        }
    });
});
