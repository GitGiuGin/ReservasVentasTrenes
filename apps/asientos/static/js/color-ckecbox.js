document.addEventListener('DOMContentLoaded', function() {
    // Obtiene todos los checkboxes con clase btn-check
    document.querySelectorAll('.btn-check').forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            console.log("Checkbox clicked: ", this.checked);
            var id = this.id; // Obtén el ID del checkbox
            var label = document.getElementById('label-' + id.split('-').pop()); // Obtén el label correspondiente

            if (this.checked) {
                label.classList.remove('btn-success');
                label.classList.add('btn-warning');
            } else {
                label.classList.remove('btn-warning');
                label.classList.add('btn-success');
            }
        });
    });
});