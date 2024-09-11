const form = document.getElementById("student-form");

function setupFormValidation() {
    form.addEventListener("submit", event => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add("was-validated");

    })
}

setupFormValidation();
