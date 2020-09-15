const items = Array.from(document.querySelectorAll(".item"));

let siblings = me => Array.from(me.closest(".item").children).filter(e => e != me);

function handleMouseEnter(event) {
    const target = event.target;
    const wrapper = target.querySelector(".preview-wrapper"),
        img = wrapper.querySelector("img");
    img.classList.add("dark");
    siblings(img).forEach((e, index) => {
        if(index === 0 || index === 2) {
            e.classList.remove("hidden");
        }
    });
}

function handleMouseLeave(event) {
    const target = event.target;
    const wrapper = target.querySelector(".preview-wrapper"),
        img = wrapper.querySelector("img");
    img.classList.remove("dark");
    siblings(img).forEach((e, index) => {
        if(index === 0 || index === 2) {
            e.classList.add("hidden");
        }
    });
}

items.forEach(item => {
    item.addEventListener("mouseenter", handleMouseEnter);
    item.addEventListener("mouseleave", handleMouseLeave);
});
