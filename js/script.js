document.addEventListener('DOMContentLoaded', function() {
    const noButton = document.getElementById('noButton');
    const yesButton = document.getElementById('yesButton');
    const question = document.getElementById('question');
    const gif = document.getElementById('gif');
    const buttons = document.getElementById('buttons');
    const message = document.getElementById('message');

    noButton.addEventListener('mouseover', function() {
        const x = Math.random() * (window.innerWidth - noButton.offsetWidth);
        const y = Math.random() * (window.innerHeight - noButton.offsetHeight);
        noButton.style.position = 'absolute';
        noButton.style.left = `${x}px`;
        noButton.style.top = `${y}px`;
    });

    yesButton.addEventListener('click', function() {
        question.style.display = 'none';
        buttons.style.display = 'none';
        gif.src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZ4aWdoeXh2aGpvZ3hsbzZtZzZhOXV6bWc0b296bW5tZzV3a2V6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/UMon0fuimoANUNhp5g/giphy.gif'; // Replace with your desired GIF
        message.style.display = 'block';
    });
});
