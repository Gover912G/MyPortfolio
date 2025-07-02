  document.addEventListener('DOMContentLoaded', () => {
        const navToggle = document.getElementById('navToggle');
        const navLinks = document.getElementById('navLinks');

        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('show');
        });
    });

    
  const toggleBtn = document.getElementById('theme-toggle');
  const userPrefersDark = localStorage.getItem('theme') === 'dark';

  // Set initial theme on page load
  if (userPrefersDark) {
    document.body.classList.add('dark-mode');
    toggleBtn.textContent = '☀️ Light Mode';
  }

  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

    const isDark = document.body.classList.contains('dark-mode');
    toggleBtn.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';

    // Save preference
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
