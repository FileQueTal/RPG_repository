const lengthdice = 6
const diceboard = document.getElementById("diceboard")
const botao = document.getElementById("rolar");
const resultado = document.getElementById("resultado");

let rotacaoX = -20;
let rotacaoY = -25;



//creacion de datos
function createDice(diceLength, parentElem){
    let newDiceWrapper = "";
    let newDice = "";

    if (!parentElem) {
        console.error("Parent element not found!");
        return;
    }

    for(i = 1; i <= diceLength; i++){
        console.log("Hello-LOOP, I'm here!");
        newDiceWrapper = document.createElement("div");
        newDiceWrapper.classList.add("scene");

        newDice = document.createElement("div");
        newDice.setAttribute("id", "dado");
        newDice.classList.add("dado");

        for (j = 1; j <= lengthdice; j++){
            let newFace = document.createElement("div");
            newFace.classList.add("face", `face-${j}`);
            newFace.textContent = j;

            newDice.appendChild(newFace);
        };
        
    };

    parentElem.appendChild(newDiceWrapper);
    newDiceWrapper.appendChild(newDice);
};

//agregando datos al tablero
createDice(1, diceboard);
const dado = document.getElementById("dado");

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

    dado.style.transform =`rotateX(${rotacaoX}deg) rotateY(${rotacaoY}deg)`;

    //resultado.textContent = numero;
});