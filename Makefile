install: # синхронизация зависимостей
	uv sync

brain-games: # запуск программы
	uv run brain-games

build: # сборка пакета
	uv build

package-install: # установка пакета
	uv tool install dist/*.whl

lint: # проверка качества кода
	uv run ruff check brain_games

brain-even:
	uv run brain-even
