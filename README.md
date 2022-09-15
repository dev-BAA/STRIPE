# STRIPE
Инструкция для установки на сервер Ubuntu 20.04
<br />
Предварительно на сервере должны быть установлены Git, Docker, docker-compose, python3.9

1. скачайте проект
```diff
git clone https://github.com/dev-BAA/STRIPE.git
```
2. перейдите в каталог проекта
```diff
cd STRIPE
```
3. соберите контэйнер
```diff
docker-compose up -d --no-deps --build
```

