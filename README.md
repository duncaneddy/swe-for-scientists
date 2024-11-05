# Software Engineering for Scientists

Repository of example code and demonstrations from my "Software Engineering for Scientists" Talk

To run the examples, you will need to have Python 3 installed on your machine. The recommended way to install Python 3
is through [Pyenv](https://github.com/pyenv/pyenv) and [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

The examples are divided by number each with their own `requirements.txt` file. To install the dependencies for each example,
`cd` into the example directory and run:

```bash
pip install -r requirements.txt
```

There are slightly different ways to execute each example.

## Example 1

```bash
streamlit run app.py
```

## Example 2

In one terminal run:

```bash
fastapi dev fastapi_server.py
```

In another terminal run:

```bash
python fastapi_client.py
```

## Example 3

```bash
pytest
```

## Example 4

In one terminal run:

```bash
fastapi dev server.py
```

In another terminal run:

```bash
pytest
```

