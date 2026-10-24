
const dado = document.getElementById("dado");
const botao = document.getElementById("rolar");
const resultado = document.getElementById("resultado");

let rotacaoX = -20;
let rotacaoY = -25;

// rotação gay do dado
const faces = {
    1: [0, 0],
    2: [0, -90],
    3: [-90, 0],
    4: [90, 0],
    5: [0, 90],
    6: [0, 180]
};

botao.addEventListener("click", () => {
    const numero = Math.floor(Math.random() * 6) + 1;

    const [x, y] = faces[numero];

    // rolagem do dado visualmente
    rotacaoX += 720 + x - rotacaoX % 360;
    rotacaoY += 720 + y - rotacaoY % 360;

    dado.style.transform =
        `rotateX(${rotacaoX}deg) rotateY(${rotacaoY}deg)`;

    resultado.textContent = numero;
});
