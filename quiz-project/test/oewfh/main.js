let questions = [
    {
        question: "Что означает HTML?",
        answers: ["Язык разметки", "Язык программирования", "База данных", "Операционная система"],
        correct: 0
    },
    {
        question: "Что используется для оформления сайта?",
        answers: ["HTML", "CSS", "JavaScript", "Python"],
        correct: 1
    },
    {
        question: "Что делает JavaScript?",
        answers: ["Добавляет интерактивность", "Создаёт таблицы", "Рисует картинки", "Удаляет сайт"],
        correct: 0
    },
    {
        question: "Какой тег используется для заголовка?",
        answers: ["p", "div", "h1", "button"],
        correct: 2
    },
    {
        question: "Какой тег создаёт кнопку?",
        answers: ["button", "input", "a", "span"],
        correct: 0
    },
    {
        question: "Как подключить CSS?",
        answers: ["script", "link", "style-js", "css"],
        correct: 1
    },
    {
        question: "Где обычно хранится JavaScript?",
        answers: ["В файле .js", "В файле .css", "В файле .txt", "В файле .png"],
        correct: 0
    },
    {
        question: "Что такое div?",
        answers: ["Контейнер", "Картинка", "Кнопка", "Ссылка"],
        correct: 0
    },
    {
        question: "Какой символ используется для id в CSS?",
        answers: [".", "#", "*", "/"],
        correct: 1
    },
    {
        question: "Какой символ используется для class в CSS?",
        answers: [".", "#", "!", "?"],
        correct: 0
    }
];

let currentQuestion = 0;
let score = 0;
let answered = false;

let questionText = document.getElementById("question");
let answersBox = document.getElementById("answers");
let nextBtn = document.getElementById("nextBtn");
let resultBox = document.getElementById("resultBox");
let resultText = document.getElementById("resultText");

showQuestion();

function showQuestion() {
    answered = false;
    nextBtn.style.display = "none";
    answersBox.innerHTML = "";

    questionText.textContent = questions[currentQuestion].question;

    for (let i = 0; i < questions[currentQuestion].answers.length; i++) {
        let button = document.createElement("button");
        button.textContent = questions[currentQuestion].answers[i];
        button.className = "answer";

        button.onclick = function () {
            checkAnswer(i, button);
        };

        answersBox.appendChild(button);
    }

//    let progress = ((currentQuestion + 1) / questions.length) * 100;
//    progressBar.style.width = progress + "%";
}

function checkAnswer(index, button) {
    if (answered == true) {
        return;
    }

    answered = true;

    let correctIndex = questions[currentQuestion].correct;
    let allButtons = document.getElementsByClassName("answer");

    if (index == correctIndex) {
        button.classList.add("correct");
        score++;
    } else {
        button.classList.add("wrong");
        allButtons[correctIndex].classList.add("correct");
    }

    nextBtn.style.display = "inline-block";
}

function nextQuestion() {
    currentQuestion++;

    if (currentQuestion < questions.length) {
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    questionText.style.display = "none";
    answersBox.style.display = "none";
    nextBtn.style.display = "none";
    resultBox.style.display = "block";

    resultText.textContent = "Результат: " + score + " из " + questions.length;
}

function restartQuiz() {
    currentQuestion = 0;
    score = 0;

    questionText.style.display = "block";
    answersBox.style.display = "block";
    resultBox.style.display = "none";

    showQuestion();
}
