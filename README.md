## ReadMe

## [Chapter 01 Domain Model Exercise](https://github.com/cosmicpython/code/tree/chapter_01_domain_model_exercise)

## Bash Code

```bash
python -m venv venv

venv\scripts\activate

venv\scripts\deactivate
```

```bash
pytest unit_tests_batches.py

## use this when running in nested folders
python -m pytest tests\unit\test_services.py
```

### TDD

* When creating tests you may be identifying methods and classes first without them existing. Don't panic, this is good as you will create them to make sure the tests fully test the intended behaviour when you implement it.

### Terms

* ABC - Abstract Base Class
* Port is the interface between out application and whatever we wish to abstract away from (AbstractRepository)
* Adapter is the implementation behind that abstraction (SqlAlchemyRepository, FakeRepository)
* To create an abstraction of a file system and file moves, you can just print what will happen to the filesystem (e.g COPY, RENAME etc), that you can then test.