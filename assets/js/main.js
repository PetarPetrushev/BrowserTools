document.addEventListener('DOMContentLoaded', () => {
    // Theme Switcher Logic
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const currentTheme = localStorage.getItem('theme') || (prefersDark ? 'dark' : 'light');

    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        if (themeToggle) {
            themeToggle.innerHTML = theme === 'dark'
                ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></svg>'
                : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>';
        }
    };

    setTheme(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            setTheme(current === 'dark' ? 'light' : 'dark');
        });
    }

    // Sidebar Mobile Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });

        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                if (sidebar.classList.contains('open') &&
                    !sidebar.contains(e.target) &&
                    e.target !== menuToggle &&
                    !menuToggle.contains(e.target)) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }

    // Copy Utility
    window.copyToClipboard = async function(text, btnElement) {
        if (!text) return;

        const originalText = btnElement ? btnElement.innerText : '';
        try {
            await navigator.clipboard.writeText(text);
            if (btnElement) {
                btnElement.innerText = "Copied!";
                btnElement.classList.add('text-success');
                setTimeout(() => {
                    btnElement.innerText = originalText;
                    btnElement.classList.remove('text-success');
                }, 2000);
            }
        } catch (err) {
            console.error('Failed to copy', err);
            if (btnElement) {
                btnElement.innerText = "Error";
                setTimeout(() => btnElement.innerText = originalText, 2000);
            }
        }
    };
});
