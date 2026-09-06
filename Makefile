install: # синхронизация зависимостей
	uv sync

brain-games: # запуск brain-games
	uv run brain-games

build: # сборка пакета
	uv build

package-install: # установка пакета
	uv tool install dist/*.whl

lint: # проверка качества кода
	uv run ruff check brain_games

brain-even: # запуск brain-even
	uv run brain-even

brain-calc: # запуск brain-calc
	uv run brain-calc

brain-gcd: # запуск brain-gcd
	uv run brain-gcd

brain-progression: # запуск brain-progression
	uv run brain-progression