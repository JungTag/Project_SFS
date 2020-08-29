const btn = document.querySelector("button");

function handleClick(event) {
    // 실제 장고에서 쓰일 것
    // location.href="{% url 'main' %}"
    window.location = "main.html"
}

btn.addEventListener("click", handleClick);