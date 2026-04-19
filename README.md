# Factorial App

A simple web application for calculating the factorial of a natural number, built with **Python** and **Streamlit**.

---

## Description

This app allows users to enter a natural number and instantly compute its factorial directly in the browser. The interface is clean and straightforward, making it great for learning and practicing Python.

---

## Project Structure

```
factorial-app/
├── app.py            # Main file — runs the Streamlit UI
├── factorial.py      # Factorial module (recursive function)
└── requirements.txt  # Required dependencies
```

---

## Requirements

- Python 3.7+
- pip

---

## Installation & Usage

**1. Clone the repository:**
```bash
git clone https://github.com/vietanh1802/factorial-app.git
cd factorial-app
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the app:**
```bash
streamlit run app.py
```

**4. Open your browser** and go to `http://localhost:8501`

---

## How to Use

1. Enter a natural number between **0 and 900** in the input field.
2. Click the **Calculate** button.
3. The factorial result will be displayed below.

---

## Algorithm

The factorial function uses recursion:

```python
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

---

## Tech Stack

| Technology | Role |
|------------|------|
| Python | Core programming language |
| Streamlit | Web UI framework |

---

## License

This project was developed for educational purposes.

