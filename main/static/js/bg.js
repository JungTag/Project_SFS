const SHOWING_CN = "showing",
    firstBg = document.querySelector(".background:first-child");
    
function slide() {
    const currentBg = document.querySelector(`.${SHOWING_CN}`);
    if (currentBg) {
        currentBg.classList.remove(SHOWING_CN);
        const nextBg = currentBg.nextElementSibling;
        if (nextBg) {
            nextBg.classList.add(SHOWING_CN);
        }
        else {
            firstBg.classList.add(SHOWING_CN);
        }
    }
    else {
        firstBg.classList.add(SHOWING_CN);
    }
}
slide();
setInterval(slide, 5000);