document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".expandable-textarea").forEach(function (textarea) {
        textarea.style.height = "auto";
        textarea.style.height = textarea.scrollHeight + "px";
    });
    
});
setTimeout(function() {
        const messages = document.querySelector('.message-container');
        console.log(messages);  
        if (messages) {
            messages.classList.add('hidden'); 
        }
    }, 5000); 