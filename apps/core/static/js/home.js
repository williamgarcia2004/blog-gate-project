const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach(item => {
    const btn = item.querySelector(".faq-question");
    const answer = item.querySelector(".faq-answer");
    const icon = item.querySelector(".faq-icon");

    btn.addEventListener("click", () => {
        // Cierra otros elementos si quieres un solo abierto
        faqItems.forEach(other => {
            if(other !== item) {
                other.querySelector(".faq-answer").style.maxHeight = null;
                other.querySelector(".faq-icon").style.transform = 'rotate(0deg)';
            }
        });

        // Alterna el actual
        if(answer.style.maxHeight){
            answer.style.maxHeight = null;
            icon.style.transform = 'rotate(0deg)';
        } else {
            answer.style.maxHeight = answer.scrollHeight + "px";
            icon.style.transform = 'rotate(180deg)';
        }
    });
});