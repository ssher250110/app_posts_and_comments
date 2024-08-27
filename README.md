## MVP приложения, в котором пользователи могут писать посты и комментировать их.

### Задание:

- Создайте модели и соответствующие точки API для взаимодействия с ними.

### Технические требования:

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

### Критерии приемки:

- Все три модели описаны.
- Все эндпоинты реализованы.
- Все описанные валидации настроены.
- Админка настроена.
- Описанные права доступа заложены в проект.
- Решение выложено на github.com.

### Структура приложения:

<details>
<summary>Задача 1</summary>

**МОДЕЛИ**

**Модель пользователя**

- логин
- пароль
- номер
- дата рождения
- дата создания
- дата редактирования

**Модель поста**

- заголовок
- текст
- изображение (если есть)
- автор
- комментарии
- дата создания
- дата редактирования

**Модель комментария**

- автор
- текст
- дата создания
- дата редактирования

**Примечание**: связи между моделями определите самостоятельно.
</details>

<details>
<summary>Задача 2</summary>

**ЭНДПОИНТЫ**

Реализуйте CRUD для каждой модели.

**Пользователь**:

- CREATE: все пользователи (регистрация).
- READ: администратор/авторизованные пользователи.
- UPDATE: администратор/пользователь может редактировать только себя./
- DELETE: администратор.

**Пост**:

- CREATE: авторизованные пользователи.
- READ: все пользователи.
- UPDATE: администратор/пользователь может редактировать только себя.
- DELETE: администратор/пользователь может удалять свои посты.

**Комментарий**:

- CREATE: авторизованные пользователи.
- READ: все пользователи.
- UPDATE: администратор/пользователь может редактировать только себя.
- DELETE: администратор/пользователь может удалять свои комментарии.

</details>

<details>
<summary>Задача 3</summary>

**ВАЛИДАТОРЫ**

**Модель пользователя**

Реализуйте валидатор для пароля (должен быть не менее 8 символов, должен включать цифры).  
Реализуйте валидатор для почты (разрешены домены: mail.ru, yandex.ru).

**Модель поста**

Реализуйте проверку того, что автор поста достиг возраста 18 лет.  
Реализуйте проверку, что автор в заголовок не вписал запрещенные слова: ерунда, глупость, чепуха.
</details>

<details>

<summary>Задача 4</summary>

**АДМИН. ПАНЕЛЬ**

Добавьте в объекте поста ссылку на автора.  
Добавьте фильтр по дате создания поста.
</details>

### Инструкция для запуска проекта

<details>
<summary>Инструкция</summary>

1. Клонируйте данный репозиторий к себе на локальную машину:

```bash
    git clone https://github.com/ssher250110/app_posts_and_comments.git
```

2. В файле .env_example подставьте свои переменные окружения и переименуйте файл в .env
3. Запустите Docker
4. Введите команду в терминале(выполнение команды осуществляется из папки проекта):
    * Для Compose V1:
    ```bash
    docker-compose up -d --build 
    ```
    * Для Compose V2:
    ```bash
    docker compose up -d --build 
    ```

- Команда для создания суперпользователя

```bash
docker ps
```

```bash
docker exec -it <id_container_trading_network> bash
```

```bash
python3 manage.py createsuperuser
```

- Пути документации

```bash
http://127.0.0.1:8000/swagger/
```

```bash
http://127.0.0.1:8000/redoc/
```

</details>

### Автор проекта:

https://github.com/ssher250110