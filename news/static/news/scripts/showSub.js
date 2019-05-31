var eL = document.getElementsByClassName("menu-item");
for (var i = 0; i < eL.length; i++) {
    eL.addEventListener('mouseenter', showSub(true), false)
    eL.addEventListener('mouseleave', showSub(false), false)
}

function showSub(isVisible) {
    if (this.children.length > 1) {
        if (isVisible) {
            this.children[1].style.height = "auto";
            this.children[1].style.opacity = '1';
            this.children[1].style.overflow = 'visible';
        } else {
            this.children[1].style.height = "0";
            this.children[1].style.opacity = '0';
            this.children[1].style.overflow = '0';
        }

    } else {
        return false;
    }

}