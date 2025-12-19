// افکت دکمه MORE ABOUT ME
document.querySelector('.cta-button').addEventListener('click', () => {
    window.scrollTo({
        top: document.querySelector('#about').offsetTop,
        behavior: 'smooth'
    });
});

// تغییر رنگ هدر هنگام اسکرول
window.addEventListener('scroll', () => {
    const header = document.querySelector('.personal-header');
    header.style.opacity = 1 - window.scrollY / 500;
});



  window.addEventListener('load', () => {
    const skillLevels = document.querySelectorAll('.skill-level');
    skillLevels.forEach(skill => {
      const level = skill.getAttribute('data-level');
      setTimeout(() => {
        skill.style.width = level;
      }, 300); // انیمیشن کمی تأخیر داره
    });
  });


