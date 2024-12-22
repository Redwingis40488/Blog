document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn.delete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmDelete = confirm('Are you sure you want to delete this blog post?');
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});
