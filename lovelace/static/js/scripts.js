const menuHamburguer = document.querySelector('.menu-haburguer');
const divMenuHamburguer = document.querySelector('.div-menu-hamburguer');

const atualizarMenu = function (){
    menuHamburguer.classList.toggle('ativo');
    footerMenuHamburguer.classList.toggle('visivel');
}

menuHamburguer.onclick = atualizarMenu;