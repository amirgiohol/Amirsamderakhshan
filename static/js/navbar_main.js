document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.progress-nav li');

    // هایلایت آیتم منو بر اساس اسکرول
    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (item.querySelector('a').getAttribute('href') === `#${current}`) {
                item.classList.add('active');
            }
        });
    });

    // اسکرول نرم برای کلیک روی منو
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.querySelector('a').getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        });
    });
});