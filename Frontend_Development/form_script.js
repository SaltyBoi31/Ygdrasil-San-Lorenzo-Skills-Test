const form = document.getElementById('feedback_form');
const form_container = document.querySelector('.form_container');
const form_message = document.getElementById('form_message');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    let errors = [];

    if (!name){ //if message is empty
        errors.push("Please enter a name.")
    }
    if (!email || !/\S+@\S+\.\S+/.test(email)) { //if email is empty or if the email has the correct format
        errors.push("Please enter a valid email.");
    }
    if (!message){ //if message is empty
        errors.push("Please enter a message.")
    }

    if (errors.length > 0) {
        form_message.style.color = "red";
        form_message.innerText = errors.join(" ");
        form_message.style.fontWeight = "bold";
        form_container.style.paddingBottom = "80px";
    } 
    else {
        form_message.style.color = "lime";
        form_message.style.fontWeight = "bold";
        form_message.innerText = "Form submitted successfully!";
        form_container.style.paddingBottom = "80px";
        form.reset();
    }
});