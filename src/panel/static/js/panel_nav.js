const navbar = document.querySelector('.navbar');
const expandIcon = document.getElementById('expand-icon');
const expandImage = document.getElementById('expand-image');

expandIcon.addEventListener('click', () => {
  if (navbar.style.left === '-200px') {
    navbar.style.left = '0';
    navbar.style.overflowY = 'auto';
    expandImage.style.transform = 'rotate(0deg)';
  } else {
    navbar.style.overflowY = 'hidden';
    navbar.style.left = '-200px';
    expandImage.style.transform = 'rotate(180deg)';
  }
});