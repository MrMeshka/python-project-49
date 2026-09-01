install: # синхронизация зависимостей
	uv sync

brain-games: # запуск программы
	uv run brain-games

build: # сборка пакета
	uv build

package-install: # установка пакета
	uv tool install dist/*.whl
