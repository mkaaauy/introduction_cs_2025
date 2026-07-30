// Функция для изменения цвета фона
function changeBackgroundColor() {
    const colors = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
        'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'
    ];
    
    const currentColor = document.body.style.background;
    let newColor;
    
    do {
        newColor = colors[Math.floor(Math.random() * colors.length)];
    } while (newColor === currentColor && colors.length > 1);
    
    document.body.style.background = newColor;
    showMessage('Цвет фона изменён! 🎨');
}

// Счётчик кликов
let counter = 0;

function incrementCounter() {
    counter++;
    document.getElementById('counter').textContent = counter;
    
    if (counter === 1) {
        showMessage('Первый клик! 👍');
    } else if (counter === 5) {
        showMessage('Отличная работа! Вы кликнули 5 раз! 🎉');
    } else if (counter === 10) {
        showMessage('Поздравляем! 10 кликов достигнуто! 🏆');
    } else if (counter % 10 === 0) {
        showMessage(`Невероятно! ${counter} кликов! 🚀`);
    }
}

// Показ сообщения
function showMessage(text) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = text;
    messageDiv.classList.add('show');
    
    // Убираем сообщение через 3 секунды
    setTimeout(() => {
        messageDiv.classList.remove('show');
        setTimeout(() => {
            messageDiv.textContent = '';
        }, 300);
    }, 3000);
}

// Приветственное сообщение при загрузке страницы
function init() {
    console.log('Страница загружена!');
    console.log('JavaScript работает корректно ✓');
    
    // Добавление анимации при загрузке
    const sections = document.querySelectorAll('section');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            section.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 100 * index);
    });
    
    showMessage('Добро пожаловать! Изучайте web-разработку! 🌟');
}

// Добавление обработчиков событий
document.addEventListener('DOMContentLoaded', function() {
    // Инициализация
    init();
    
    // Кнопка изменения цвета
    const colorButton = document.getElementById('colorButton');
    if (colorButton) {
        colorButton.addEventListener('click', changeBackgroundColor);
    }
    
    // Кнопка счётчика
    const counterButton = document.getElementById('counterButton');
    if (counterButton) {
        counterButton.addEventListener('click', incrementCounter);
    }
    
    // Добавление эффекта при наведении на карточки
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Вывод информации в консоль
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('  Добро пожаловать в Introduction CS 2025!');
console.log('  HTML + CSS + JavaScript = ❤️');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
