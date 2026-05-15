CREATE DATABASE synergy_education;
USE synergy_education;

-- 1. Справочник направлений подготовки
CREATE TABLE Directions (
    direction_id INT PRIMARY KEY AUTO_INCREMENT,
    direction_code VARCHAR(20) NOT NULL,        -- например: 09.03.03
    direction_name VARCHAR(150) NOT NULL,       -- Прикладная информатика
    profile VARCHAR(100)                        -- Искусственный интеллект и большие данные
);

-- 2. Справочник преподавателей
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(150) NOT NULL,
    position VARCHAR(100),                      -- Доцент, Преподаватель и т.д.
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- 3. Справочник курсов / дисциплин
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_code VARCHAR(30) NOT NULL,
    course_name VARCHAR(200) NOT NULL,
    direction_id INT,
    hours INT,
    semester INT,
    FOREIGN KEY (direction_id) REFERENCES Directions(direction_id)
);

-- 4. Справочник групп
CREATE TABLE Groups (
    group_id INT PRIMARY KEY AUTO_INCREMENT,
    group_name VARCHAR(50) NOT NULL,            -- ОБП-123312МОиибд
    direction_id INT,
    start_year YEAR,
    FOREIGN KEY (direction_id) REFERENCES Directions(direction_id)
);

-- 5. Основная таблица (переменная информация) — Записи о прохождении курсов
CREATE TABLE Student_Course_Registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    student_full_name VARCHAR(150) NOT NULL,
    group_id INT,
    course_id INT,
    teacher_id INT,
    registration_date DATE,
    status ENUM('Зарегистрирован', 'В процессе', 'Завершен', 'Отчислен') DEFAULT 'Зарегистрирован',
    grade INT,                                  -- Оценка (если есть)
    FOREIGN KEY (group_id) REFERENCES Groups(group_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
