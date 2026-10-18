# Анализ изображений: от данных к модели — практикумы

Ноутбуки Colab к блоку Наталии Тылевич (© 2026, все права защищены). По одному на часть блока. Программировать не нужно: откройте ноутбук, нажмите
**«Среда выполнения → Выполнить все»** и меняйте параметры в полях справа от ячеек. Данные ноутбук скачивает сам.

Ноутбуки и ссылки на них работают на время курса. Если ссылка не активна — обратитесь к автору.

| Часть | Ноутбук | Открыть |
|---|---|---|
| Введение · Данные — основа всего | `00_intro_data.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BigDataQueen/cv-practicum/blob/main/00_intro_data.ipynb) |
| 1 · Алгоритмическая база | `01_algorithms.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BigDataQueen/cv-practicum/blob/main/01_algorithms.ipynb) |
| 2 · Графы в машинном обучении | `02_graphs.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BigDataQueen/cv-practicum/blob/main/02_graphs.ipynb) |
| 3 · Сбор и разметка данных | `03_data_collection_labeling.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BigDataQueen/cv-practicum/blob/main/03_data_collection_labeling.ipynb) |
| 4 · Компьютерное зрение | `04_computer_vision.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BigDataQueen/cv-practicum/blob/main/04_computer_vision.ipynb) |

## Как начать

1. Нужен аккаунт Google — Colab работает от него, бесплатно.
2. Откройте ноутбук по кнопке выше или по QR из презентации.
3. «Среда выполнения → Выполнить все» и читайте сверху вниз.
4. Меняйте значения в полях и запускайте ячейку заново (▶ или Ctrl+Enter).
5. Чтобы сохранить свою версию: «Файл → Сохранить копию на Диске». Исходный ноутбук общий и не меняется.

В части «Компьютерное зрение» есть нейросети: включите видеокарту — «Среда выполнения → Сменить среду → GPU». На процессоре тоже работает,
но медленнее.

## Данные

- Снимки листьев — открытый набор PlantVillage (Mohanty, Hughes, Salathé, 2016), лицензия CC BY-SA 3.0,
  [spMohanty/PlantVillage-Dataset](https://github.com/spMohanty/PlantVillage-Dataset).
- Рукописные цифры — scikit-learn; графы «Отверженных» и карате-клуба — NetworkX.
- Учебная страница новостей в части «Сбор и разметка» — выдуманная, встроена в ноутбук.

Ноутбуки собираются скриптом из материалов курса; правки сюда приходят новой версией, а не правкой файлов вручную.

## Авторские права

© 2026 Наталия Тылевич. Все права защищены. Открывать, выполнять и хранить личную копию для заданий
курса — можно; распространять, использовать в других курсах и коммерчески — только с письменного согласия автора.
Подробно — [`LICENSE.md`](LICENSE.md).
