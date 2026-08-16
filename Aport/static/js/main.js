// Typewriter effect for profession
document.addEventListener('DOMContentLoaded', function() {
    const professionElement = document.querySelector('.profession');
    if (!professionElement) return;
    
    const profession = professionElement.textContent;
    professionElement.textContent = '';
    
    let i = 0;
    const typeWriter = () => {
        if (i < profession.length) {
            professionElement.textContent += profession.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    };
    
    setTimeout(typeWriter, 1000);
});
