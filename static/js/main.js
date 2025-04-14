// Script pour la validation de formulaire et interactions utilisateur
document.addEventListener('DOMContentLoaded', function() {
    // Validation du formulaire de réservation
    const bookingForm = document.querySelector('#booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            const checkIn = document.querySelector('#check_in').value;
            const checkOut = document.querySelector('#check_out').value;

            // Validation simple des dates
            if (new Date(checkIn) >= new Date(checkOut)) {
                e.preventDefault();
                alert('La date de départ doit être postérieure à la date d'arrivée.');
            }

            // Empêcher la sélection de dates passées
            const today = new Date().toISOString().split('T')[0];
            if (checkIn < today) {
                e.preventDefault();
                alert('Vous ne pouvez pas sélectionner une date passée.');
            }
        });
    }

    // Mise à jour dynamique du prix total
    const updateTotalPrice = function() {
        const checkIn = document.querySelector('#check_in');
        const checkOut = document.querySelector('#check_out');
        const pricePerNight = document.querySelector('#price-per-night');
        const totalPrice = document.querySelector('#total-price');

        if (checkIn && checkOut && pricePerNight && totalPrice) {
            const checkInDate = new Date(checkIn.value);
            const checkOutDate = new Date(checkOut.value);

            if (checkInDate && checkOutDate && checkInDate < checkOutDate) {
                const nights = Math.floor((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24));
                const price = parseFloat(pricePerNight.dataset.price);
                const total = nights * price;
                totalPrice.textContent = total.toFixed(2) + ' €';
            }
        }
    };

    // Écouter les changements de date
    const dateInputs = document.querySelectorAll('#check_in, #check_out');
    dateInputs.forEach(input => {
        input.addEventListener('change', updateTotalPrice);
    });

    // Initialiser Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Filtrer les dates indisponibles dans le datepicker
    // Ce code est commenté car il nécessite une bibliothèque datepicker plus avancée
    /*
    if (typeof bookedDates !== 'undefined') {
        $('.datepicker').datepicker({
            format: 'yyyy-mm-dd',
            startDate: new Date(),
            datesDisabled: bookedDates
        });
    }
    */
});
