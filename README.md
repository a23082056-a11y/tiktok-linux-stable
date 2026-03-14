# TikTok Desktop for Linux (PyQt6)

Простое и легкое приложение для просмотра TikTok на Linux Mint, Ubuntu и других дистрибутивах. 

## Особенности
*   **Навигация**: Кнопки "Назад", "Главная" и "Обновить".
*   **Изоляция**: Работает через Flatpak (безопасно и надежно).
*   **Авторизация**: Поддерживает вход через QR-код и другие методы.

## Как установить (для разработчиков)
1. Установите зависимости:
   ```bash
   sudo apt install python3-pyqt6 python3-pyqt6.qtwebengine
   ```
2. Запустите скрипт:
   ```bash
   python3 tiktok_app.py
   ```

## Сборка Flatpak
Если вы хотите собрать пакет самостоятельно:
```bash
flatpak-builder --user --install --force-clean build-dir com.Arsen.TikTokDesktop.json
```
