all: activate install run

activate:
	@echo "Activating virtual environment..."
	@source venv/bin/activate

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

run:
	@echo "Running the application with streamlit..."
	@streamlit run app.py
	