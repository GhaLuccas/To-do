document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.toggle-status');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const taskId = this.getAttribute('data-id');
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(`/tasks/toggle-status/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Atualize o botão com base no novo status
                    this.classList.toggle('btn-success');
                    this.classList.toggle('btn-warning');
                    this.textContent = data.done ? 'Completed' : 'Pending';
                } else {
                    alert('Failed to update task status.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
