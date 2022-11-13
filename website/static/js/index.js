function toggleNav() {
    let nav_list = document.querySelector('.navbar-list');
    console.log(nav_list);
    nav_list.className == 'navbar-list' ? nav_list.className = 'navbar-list active' : nav_list.className = 'navbar-list';
    let nav_toggler = document.querySelector('.line');
    nav_toggler.className == 'line' ? nav_toggler.className = 'line active' : nav_toggler.className = 'line';
}