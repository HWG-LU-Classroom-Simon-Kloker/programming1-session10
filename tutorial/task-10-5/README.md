---
title: "BWI160 Programming 1 - 10 Testing Your Code"
author: "Prof. Dr. Simon Kloker"
---

{{< include ../fragments/_housekeeping.qmd >}}

## ⛰️ This lecture's context: Henry Dunant and Florence Nightingale


### Henry Dunant

![Henry Dunant](img/henri-dunant.jpg)

Henry Dunant was a Swiss businessman and social activist who, after witnessing the horrific aftermath of the Battle of Solferino, founded the International Committee of the Red Cross. His lifelong commitment to humanitarianism earned him the distinction of receiving the first-ever Nobel Peace Prize in 1901.

{{< slides-break >}}

### Florence Nightingale

![Florence Nightingale](img/florence.jpg)

Florence Nightingale was a pioneering reformer who transformed nursing into a respected profession by using rigorous statistics and sanitation practices to drastically reduce hospital death rates. Driven by what she described as a divine calling, she became a global icon known as "The Lady with the Lamp" for her tireless care of soldiers during the Crimean War.

# Learning Objectives

![](/shared/images/learning_objectives.png){width=80}

In this lecture...

- ... you'll learn why testing is essential for professional programming and how it builds confidence in your code.
- ... you'll learn to write automated tests using `pytest`, the most popular Python testing framework.
- ... you'll learn to test both functions and classes, including how to use fixtures to reduce code duplication.
- ... you'll learn advanced testing techniques like parametrization and exception testing.
- ... you'll learn about the `if __name__ == "__main__":` pattern and why it's critical for writing testable, professional Python code.

# Repetition: What we have already covered (starting from Session 05)

- Dictionaries
    - Creating Dictionaries with Curly Braces: `{}`
    - `dict()` Constructor
    - Accessing, Adding, Modifying, and Removing Key-Value Pairs: `my_dict[key]`, `my_dict[key] = value`, `del my_dict[key]`
    - `get()` Method for Safe Access with Default Values
    - Looping through Dictionaries with `.items()`, `.keys()`, `.values()`
    - Nesting: Lists inside Dictionaries, Dictionaries inside Lists, Dictionaries inside Dictionaries
- User Input and While Loops
    - `input()` Function and Processing Text and Numerical Input
    - `str.format()` Method for String Formatting
    - `while` Loops and Loop Conditions
    - Loop Control: Flags, `break`, and `continue`
    - Using `while` Loops to Move Items between Lists
    - Using `while` Loops with Dictionaries and User Input

{{< slides-break >}}

- Functions
    - Defining Functions with `def` and Calling Functions
    - Positional Arguments, Keyword Arguments, and Default Values
    - Making Arguments Optional
    - Return Values: Returning Simple Values and Dictionaries
    - Using Functions with `while` Loops
    - Passing Lists to Functions: Modifying vs. Preventing Modification
    - Arbitrary Arguments: `*args` and `**kwargs`
    - Storing Functions in Modules: `import`, `from ... import`, Aliases
- Classes
    - Defining Classes with `class`, `__init__()`, and `self`
    - Creating Instances and Accessing Attributes
    - Defining and Calling Methods
    - Default Attribute Values and Modifying Attributes (directly, via methods)
    - Setter and Getter Methods
    - Inheritance: Child Classes, `super()`, Overriding Methods
    - Storing Classes in Modules and Importing Classes

{{< slides-break >}}

- Files and Exceptions
    - Reading Files with `pathlib`: `read_text()`, `splitlines()`
    - Relative and Absolute File Paths
    - Method Chaining
    - Writing Files: `write_text()`, Writing Single and Multiple Lines
    - Handling Exceptions with `try`/`except`/`else`/`finally`
    - Common Exceptions: `ZeroDivisionError`, `FileNotFoundError`, `ValueError`
    - Handling Multiple Exceptions and Failing Silently with `pass`
    - Storing Data with JSON: `json.dumps()`, `json.loads()`

# Why Testing Matters

**Testing is Essential**

- Verify that your code works correctly
- Catch bugs before users find them
- Make refactoring safer
- Document expected behavior
- Build confidence in your code


::: {.fragment}

**Testing Benefits**

- ✅ Easier bug fixing (tests identify the problem)
- ✅ Freedom to improve code
- ✅ Other programmers respect your work
- ✅ Required for professional projects

:::

# pytest

**What is pytest?**

- Simple, powerful testing framework for Python
- Automatically discovers and runs tests
- Clear, concise syntax

## Installing pytest

Before you can use pytest, it must be installed in your Python environment. The installation process depends on how you manage your Python packages (e.g., using pip or conda).


{{< slides-break >}}

### Step 1: Check if pytest is already installed

Here's how to check if it's already installed and install it if needed:

Open your terminal and run:

```bash
pytest --version
```

If pytest is installed, you'll see the version number. If not, you'll see an error message.

{{< slides-break >}}

### Step 2a: Installing pytest (using pip)

First, make sure pip is installed:
```bash
python -m pip --version
# or
python3 -m pip --version
```

{{< slides-break >}}

If pip is not installed, you need to install it first:

```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-pip

# On macOS (using Homebrew)
brew install python3

# On Windows, pip comes with Python installer
# Download from python.org
```

{{< slides-break >}}

Once pip is available, install pytest:

```bash
python -m pip install pytest
# or
python3 -m pip install pytest
```

{{< slides-break >}}

### Step 2b: Installing pytest (using conda)

If you're using **Anaconda** or **Miniconda**, the process is slightly different:

1. **Check if pytest is installed in your conda environment:**
   ```bash
   conda list pytest
   ```

2. **Install pytest using conda (recommended for conda users):**
   ```bash
   conda install pytest
   ```
   
   Or using conda-forge channel:
   ```bash
   conda install -c conda-forge pytest
   ```

{{< slides-break >}}

**Key differences with conda:**

- Conda manages both Python packages AND system libraries
- Better dependency resolution for scientific packages
- Creates isolated environments more easily
- You should prefer `conda install` over `pip install` when using conda environments to avoid conflicts
- If a package isn't available in conda, you can still use pip: `pip install pytest` (but conda is preferred)

{{< slides-break >}}

### Step 3: Verify pytest installation

```bash
pytest --version
```

## Using Github Codespaces

Alternatively, I have prepared a Github Codespace for this lecture with pytest already installed. You can use it to follow along without worrying about installation.

[https://github.com/HWG-LU-Classroom-Simon-Kloker/programming1-session10](https://github.com/HWG-LU-Classroom-Simon-Kloker/programming1-session10)

![Github Repository for Session 10](img/github_repository.png)

- log in with your GitHub account
- click "Use this template"
- click "Open in Codespaces"

{{< notice >}} If you don't use Github Codespaces, you can still download the files and run them locally. Just make sure to install pytest first!

{{< include ../fragments/_github_downlaod.qmd >}}

# Testing Functions

Let's create a function to format the names of Red Cross relief workers:

**`worker_names.py`**
```python
def get_formatted_worker_name(first, last):
    """
    Return a neatly formatted worker name.
    Example: Henry Dunant
    """
    full_name = f"{first} {last}"
    return full_name.title()
```

{{< slides-break >}}

**`main.py`**
```python
from worker_names import get_formatted_worker_name

# Test it
worker = get_formatted_worker_name('henry', 'dunant')
print(f"Worker: {worker}")
```


::: {.fragment}

**Expected output:**
```
Worker: Henry Dunant
```

:::


{{< slides-break >}}

{{< think >}} This is how we tested our code in the past: by running it and checking the output manually. 

This is fine for small scripts, but as your code grows, you need a better way to ensure everything works correctly without having to check every output by hand.

It is not possible to manually check every output in a large program - every time you make a change, you would have to re-run all your tests manually. Automated tests are essential for maintaining code quality and catching bugs early.

## Writing Your First (Automated) Test

`pytest` allows us to write automated tests that can be run with a single command.


::: {.fragment}

**How it works:**

- Write test functions that verify expected behavior
- Function names must start with `test_`
- Run `pytest` to execute all tests
- Each assertion checks a condition
- Tests pass if all assertions are true

:::

{{< slides-break >}}

**Structure of a test function:**

**`test_worker_names.py`**
```python
from worker_names import get_formatted_worker_name                          # <1>

def test_simple_worker_name():                                              # <2> 
    """
    Test that simple worker names (first and last) are formatted correctly.
    Example: Clara Barton
    """
    formatted_name = get_formatted_worker_name('clara', 'barton')          # <3>
    assert formatted_name == 'Clara Barton'                                # <4>
```
1. Import the function being tested
2. Test function name starts with `test_` 
3. Call the function being tested with specific inputs
4. Use `assert` to check that the output matches the expected result

{{< slides-break >}}

**Running the test in terminal:**

```bash
$ pytest test_worker_names.py                                           # <1>
======================== test session starts =========================
test_worker_names.py . [100%]                                           # <2>
======================== 1 passed in 0.01s =========================
```
1. Run `pytest` followed by the test file name to execute the tests (make sure you're in the correct directory or specify the path)
2. A dot (`.`) indicates a test passed; an `F` would indicate a failure


::: {.fragment}

{{< try >}}: Download the `worker_names.py`, `main.py`, and `test_worker_names.py` files from the Github repository or open them in a Github Codespace. Run `pytest test_worker_names.py` to verify that the test passes.

:::


## 🔧 Task 10.0: Florence Nightingale joins the British Red Cross

**Scenario**:

Despite Florence Nightingale's early skepticism, she eventually became a supporter of the British Red Cross.

**The Tasks:**

- Add optional `middle=''` parameter to `get_formatted_worker_name`
- Build full name based on whether middle name exists
- Test with "Florence Emma Nightingale"
- Keep backward compatibility (existing tests still pass)


*Note: She does not actually have a middle name.* 😉

{{< slides-break >}}

### Solution

**Updated `worker_names.py`**
```python
def get_formatted_worker_name(first, last, middle=''):
    """
    Return a neatly formatted worker name.
    Middle name is optional.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

{{< slides-break >}}

**Updated `main.py`**
```python
from worker_names import get_formatted_worker_name

# Test both cases
worker1 = get_formatted_worker_name('clara', 'barton')
print(f"Simple name: {worker1}")

worker2 = get_formatted_worker_name('florence', 'nightingale', 'emma')
print(f"Full name: {worker2}")
```

{{< slides-break >}}

**Testing the updated function:**

✅ Old tests still pass: Clara Barton

✅ New functionality works: Florence Emma Nightingale

## Writing Multiple Test Cases

**Why multiple tests?**

- Test different scenarios separately
- Clear test names explain what's being tested
- Easy to identify which specific behavior broke
- Build confidence in all use cases

{{< slides-break >}}

**Updated `test_worker_names.py` - Multiple tests**
```python
from worker_names import get_formatted_worker_name

def test_simple_worker_name():
    """Test simple names (first and last)."""
    formatted_name = get_formatted_worker_name('clara', 'barton')
    assert formatted_name == 'Clara Barton'

def test_worker_name_with_middle():
    """Test names with middle name."""
    formatted_name = get_formatted_worker_name('florence', 'nightingale', 'emma')
    assert formatted_name == 'Florence Emma Nightingale'
```

{{< slides-break >}}

**Running multiple tests:**
```bash
$ pytest test_worker_names.py
======================== test session starts =========================
test_worker_names.py .. [100%]
======================== 2 passed in 0.01s =========================
```

✅ Two dots indicate two tests passed!


::: {.fragment}

{{< try >}} Update the file `test_worker_names.py` to include the new test for the middle name. Run pytest to verify both tests pass.

:::

# Common Assertion Statements

**Assertion Basics:**

- Assertion = claim about what should be true
- If assertion is true → test passes
- If assertion is false → test fails


::: {.fragment}

**Most Useful Assertions:**

| Assertion | Meaning |
|-----------|----------|
| `assert a == b` | Assert that two values are equal |
| `assert a != b` | Assert that two values are NOT equal |
| `assert a` | Assert that `a` evaluates to True |
| `assert not a` | Assert that `a` evaluates to False |
| `assert element in list` | Assert element is in the list |
| `assert element not in list` | Assert element is NOT in the list |

:::

{{< slides-break >}}

```python
# Examples of assertion statements

# Equality
assert "Henry Dunant" == "Henry Dunant"
assert 1870 != 1869

# Boolean
assert True
assert not False

# Membership
workers = ['Henry', 'Clara', 'Florence']
assert 'Clara' in workers
assert 'Unknown' not in workers

print("✅ All assertions passed!")
```

# Testing Classes

**Why test classes?**

- Verify that methods work correctly
- Ensure data is stored properly
- Confidence when improving class behavior
- Catch accidental bugs during refactoring

**Testing approach:**

- Create instance of the class
- Call methods on the instance
- Assert that the instance state is correct

## Example: Red Cross Survey Class

**Scenario:** Collect survey responses from Red Cross volunteers about relief efforts

**`red_cross_survey.py`**
```python
class VolunteerSurvey:
    """Collect anonymous survey responses from Red Cross volunteers."""
    
    def __init__(self, question):
        """Store a survey question and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Display the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single volunteer response."""
        if not new_response:
            raise ValueError("Response cannot be empty.")
        self.responses.append(new_response)
    
    def show_results(self):
        """Display all responses received."""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")
```

\


::: {.fragment}

{{< note >}} Last session we talked about error handling. Here you see an example of how to raise an error when invalid input is given. We will learn how to test for this expected error later in this lecture.

:::




{{< slides-break >}}

**`main.py`**
```python
# Example: Using the VolunteerSurvey class
from red_cross_survey import VolunteerSurvey

# Create survey
question = "What humanitarian region do you work in?"
survey = VolunteerSurvey(question)

# Collect responses
survey.show_question()
survey.store_response('Southeast Asia')
survey.store_response('Middle East')
survey.store_response('Africa')

# Show results
survey.show_results()
```

## Testing Class Methods with Multiple Scenarios

It is important to test different scenarios for class methods to ensure they work correctly in all cases. For example, we want to test that the `store_response()` method correctly stores as single and multiple responses, and handles edge cases (like empty responses).


::: {.fragment}

Therefore:
- We need to *anticipate* **how the class will be used** and write tests that cover those scenarios.
- We need to *anticipate* both correct usage (storing valid responses) and **incorrect usage** (storing empty responses) to ensure our class is robust.
:::



{{< slides-break >}}

**`test_survey.py`**
```python
from red_cross_survey import VolunteerSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    
    # Store a single response
    survey.store_response('Africa')
    
    # Verify it was stored
    assert 'Africa' in survey.responses

def test_store_three_responses():
    """Test that multiple responses are stored properly."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    
    # Store multiple responses
    responses = ['Southeast Asia', 'Middle East', 'Africa']
    for response in responses:
        survey.store_response(response)
    
    # Verify all were stored
    for response in responses:
        assert response in survey.responses
```

{{< slides-break >}}

**Running the tests:**
```bash
$ pytest test_survey.py
======================== test session starts =========================
test_survey.py .. [100%]
======================== 2 passed in 0.01s =========================
```

## Testing for Expected Exceptions

Sometimes, a "successful" test is one where the code crashes correctly. 

For example, if we add validation to prevent empty responses in our survey, we want the code to raise an error when someone tries to store an empty response. 


::: {.fragment}

We use `pytest.raises` to "catch" that expected error. If the error doesn't happen, the test fails!

:::


::: {.fragment}

**Usage (Example with `ValueError`):**

```python
import pytest

with pytest.raises(ValueError):
    # Code that should raise ValueError goes here
```

:::


## 🔧 Task 10.1: Complete the survey tests

**The Tasks:**

- Use the files in `task-10-1` folder as a starting point
- Add a test to verify that storing an empty response raises a `ValueError`
- Use `pytest.raises(ValueError)` to check for the error
- Run the tests to verify the new test passes

{{< slides-break >}}

### Solution

**Updated `test_survey.py` with exception test**
```python
from red_cross_survey import VolunteerSurvey
import pytest

# Existing tests...

def test_store_empty_response():
    """Test that storing an empty response raises a ValueError."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    
    # Attempt to store an empty response
    import pytest
    with pytest.raises(ValueError):
        survey.store_response('')

```

# 🔧 Task 10.2: Red Cross Relief Worker Pay System

**The Tasks:**

- Create an `ReliefWorker` class with:
  - `__init__()` storing first_name, last_name, annual_salary
  - `give_raise()` method adding $5,000 by default (or custom amount)
- **Tests needed:**
  1. `test_give_default_raise()` - Verify $5,000 is added
  2. `test_give_custom_raise()` - Verify custom raise works

## Solution

**`relief_worker.py`**
```python
class ReliefWorker:
    """Represent a Red Cross relief worker."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the worker with name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=5000):
        """Give the worker a raise."""
        self.annual_salary += raise_amount
```

{{< slides-break >}}

**`test_relief_worker.py` - Without fixtures first**
```python
from relief_worker import ReliefWorker

def test_give_default_raise():
    """Test that default raise of $5,000 is applied."""
    worker = ReliefWorker('Clara', 'Barton', 40000)
    worker.give_raise()
    assert worker.annual_salary == 45000

def test_give_custom_raise():
    """Test that custom raise amount is applied."""
    worker = ReliefWorker('Florence', 'Nightingale', 50000)
    worker.give_raise(3000)
    assert worker.annual_salary == 53000
```

# Using Fixtures for Test Setup

**The Problem:**

- Repeating setup code in each test function
- Wasteful when tests need the same resource
- Hard to maintain as tests grow


::: {.fragment}

**The Solution: Fixtures**

- `@pytest.fixture` decorator marks a setup function
- Fixture runs before each test that needs it
- Return value passed as parameter to test
- Eliminates code duplication

:::

{{< slides-break >}}

**`test_survey_with_fixture.py`**
```python
import pytest
from red_cross_survey import VolunteerSurvey

# Define the fixture
@pytest.fixture                                                            # <1>
def volunteer_survey():                                                    # <2>         
    """Create a survey instance for all tests."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)                                     # <3>   
    return survey                                                     # <4>                       

# Use the fixture in tests
def test_store_single_response(volunteer_survey):                          # <5>
    """Test storing a single response."""
    volunteer_survey.store_response('Africa')                              # <6>
    assert 'Africa' in volunteer_survey.responses

def test_store_empty_response(volunteer_survey):
    """Test that storing an empty response raises a ValueError."""
    # Attempt to store an empty response
    import pytest
    with pytest.raises(ValueError):
        volunteer_survey.store_response('')

def test_store_three_responses(volunteer_survey):
    """Test storing multiple responses."""
    responses = ['Southeast Asia', 'Middle East', 'Africa']
    for response in responses:
        volunteer_survey.store_response(response)
    
    for response in responses:
        assert response in volunteer_survey.responses
```
1. Decorate the function with `@pytest.fixture` to mark it as a fixture
2. Define a function that sets up the resource (in this case, a `VolunteerSurvey` instance)
3. Create the resource (the survey instance)
4. Return the resource so it can be used in tests
5. Test functions receive the fixture as a parameter (pytest injects it automatically)
6. Use the fixture in the test without needing to set it up manually in each test!

{{< slides-break >}}

**How Fixtures Work:**

1. Function decorated with `@pytest.fixture`
2. Creates and returns a resource
3. Test function lists fixture name as parameter
4. pytest automatically calls fixture and passes result
5. Each test gets a fresh instance


::: {.fragment}

**Benefits:**

- No setup code in test functions
- Easier to maintain
- Clearer test focus
- DRY principle (Don't Repeat Yourself)

:::


## When to Use Fixtures

**Use fixtures when:**

- Multiple tests need the same setup
- Setup code is complex or lengthy
- You have many tests to maintain

**Don't use fixtures when:**

- Only one test uses the resource
- Setup is trivial (1-2 lines)
- You're writing your first tests


::: {.fragment}

{{< notice >}} Better to write simple tests without fixtures than to write no tests at all!

:::


## 🔧 Task 10.3: Red Cross Relief Worker Pay System II

**The Tasks:**

- Use the code you have created for Task 10.2 (otherwise, look into the folder `task-10-3` for the starting point)
- Refactor tests to use fixtures
- Verify tests still pass

{{< slides-break >}}

### Solution

**`test_relief_worker_complete.py` - With fixture**
```python
import pytest
from relief_worker import ReliefWorker

# Create fixture
@pytest.fixture
def relief_worker():
    """Create a relief worker instance for all tests."""
    worker = ReliefWorker('Clara', 'Barton', 40000)
    return worker

# Use fixture in tests
def test_give_default_raise(relief_worker):
    """Test default raise of $5,000."""
    relief_worker.give_raise()
    assert relief_worker.annual_salary == 45000

def test_give_custom_raise(relief_worker):
    """Test custom raise amount."""
    relief_worker.give_raise(3000)
    assert relief_worker.annual_salary == 43000
```

{{< slides-break >}}

**Running with pytest:**
```bash
$ pytest test_relief_worker_complete.py
======================== test session starts =========================
test_relief_worker_complete.py .. [100%]
======================== 2 passed in 0.01s =========================
```

{{< note >}} Code is now maintainable and well-tested.


::: {.fragment}

{{< note >}} If you edit the instance in one test, it will not affect the other test because pytest creates a fresh instance for each test when using fixtures.

:::

## The Scope of Fixtures

By default, fixtures have a scope of "function", meaning a new instance is created for each test function. 

However, pytest allows you to change the scope to "class", "module", or "session" if you want to share the fixture across multiple tests or even the entire test suite.

Example of changing fixture scope:
```python
@pytest.fixture(scope="module")
def relief_worker():
    """Create a relief worker instance for the entire module."""
    worker = ReliefWorker('Clara', 'Barton', 40000)
    return worker
```

::: {.fragment}

{{< note >}} This time, the second test will see the modified salary from the first test because the same instance is shared across tests in the module scope. 

{{< warning >}} Be careful when changing fixture scope, as it can lead to unintended side effects between tests if they modify the shared resource.

:::


# Testing with Multiple Inputs

Instead of writing multiple test functions for different worker names, you can use parametrization. It allows you to run the same test logic multiple times with different inputs.


::: {.fragment}

We use the **decorator `@pytest.mark.parametrize`** to specify the parameters and their values. This way, we can test multiple cases without writing separate test functions for each case.

:::



{{< slides-break >}}

**`test_worker_names.py` with various inputs**
```python
import pytest
from worker_names import get_formatted_worker_name

@pytest.mark.parametrize("first, last, expected", [             # <1>
    ("henry", "dunant", "Henry Dunant"),        
    ("CLARA", "BARTON", "Clara Barton"),
    ("florence", "nightingale", "Florence Nightingale")
])
def test_worker_name_formatting(first, last, expected):         # <2> 
    """Test that worker names are formatted correctly regardless of input case."""    

    formatted = get_formatted_worker_name(first, last)
    assert formatted == expected
```
1. `@pytest.mark.parametrize` decorator takes a string of argument names and a list of tuples with test cases
2. The test function receives the parameters for each test case and runs the assertions for all cases automatically!


# Summary: Why Testing Matters

**Testing is Professional Development**

- ✅ Catch bugs early (before users find them)
- ✅ Refactor with confidence (changes won't break things)
- ✅ Document expected behavior (tests show how to use code)
- ✅ Other programmers respect tested code


::: {.fragment}

**Best Practices:**

1. Write tests for critical functionality
2. Keep test names descriptive
3. One assertion per test (when possible)
4. Use fixtures to reduce duplication
5. Run tests frequently during development

:::

{{< slides-break >}}

**Remember:**

- Tests make you more confident
- Tests make your code better
- Tests save time in the long run
- Professional projects require tests

# 🔧 Task 10.4: The 1864 Geneva Convention Auditor 🏛️ 

**Scenario:**

It is August 1864. Henry Dunant has gathered representatives from across Europe to sign the first treaty for the protection of wounded soldiers. As the "Technical Secretary," you must build a system to manage the delegations. However, because this is the first time such an international system has been built, the logic must be bulletproof.

{{< slides-break >}}

**The Tasks:**

- You are be given a skeleton of two classes (see files in `task-10-4` folder):
  - `Delegation`: A simple data class for the country.
  - `Convention`: The manager class.
- Implement the `total_votes()` method.
  - Logic: Neutral countries (like Switzerland) get 2 votes; non-neutral countries get 1 vote.
- Create a file named `test_convention.py` and achieve 100% pass rate on the following scenarios:
  - The Normalization Test: Verify that inputting `" belgium "` or `"BELGIUM"` results in a stored name of `"Belgium"`.
  - The Exception Test: Use `pytest.raises(DuplicateCountryError)` to ensure no country can sign the treaty twice.
  - The Fixture Challenge: Create a `@pytest.fixture` that sets up a "Standard Convention" with France (non-neutral) and Switzerland (neutral) to be used across multiple tests.
  - The Logic Test: Verify that the `total_votes()` method correctly calculates the sum based on neutrality.

## Solution

See the provided `convention_manager.py` and `test_convention.py` files in the Github repository for the complete implementation and tests.

# 🚪 Self-Study: The "Front Door" of a Python Script

## Understanding `if __name__ == "__main__":`

In Python, we don't technically need a `main` function to run code. However, as your programs grow from simple scripts to complex systems (like our Geneva Convention Auditor), you need a way to **control when and how code executes**.

**The Problem:** When you import a file, Python runs all the code in it immediately.

**The Solution:** The `if __name__ == "__main__":` block ensures code only runs if the file is executed directly, **not** when it is imported by another file (like a test file).

## Why This Matters for Testing

Imagine you create `convention_manager.py` with your classes AND some test code at the bottom:

**`convention_manager.py`**
```python
class Delegation:
    def __init__(self, country):
        self.country = country

# This runs immediately when imported!
print("Creating a test delegation...")
test = Delegation("Switzerland")
print(f"Country: {test.country}")
```

{{< slides-break >}}

Now when `pytest` imports this file to test your classes, it will print those messages during testing! This is messy and unprofessional.

**`convention_manager.py` - With the guard:**
```python
class Delegation:
    def __init__(self, country):
        self.country = country

# This ONLY runs when file is executed directly
if __name__ == "__main__":
    print("Creating a test delegation...")
    test = Delegation("Switzerland")
    print(f"Country: {test.country}")
```

{{< notice >}} Now `pytest` can import `Delegation` cleanly without triggering your test code!

## Standard Professional Structure

In professional Python development, we organize our `.py` files into **three distinct zones**:

1. **Imports Zone**: Bringing in tools from other modules
   ```python
   import pytest
   from datetime import datetime
   ```


::: {.fragment}

2. **Definitions Zone**: Creating Classes and Functions (the "blueprints")
   ```python
   class Delegation:
       def __init__(self, country):
           self.country = country
   
   def validate_country_name(name):
       return name.strip().title()
   ```

:::

{{< slides-break >}}

3. **Execution Zone**: The `main()` function (the "construction site")
   ```python
   def main():
       """Entry point of the program."""
       delegation = Delegation("Switzerland")
       print(f"Welcome, {delegation.country}!")
   
   if __name__ == "__main__":
       main()
   ```

{{< slides-break >}}

**Why this structure?**

- **Clarity**: Anyone reading your code knows exactly where to look
- **Testability**: pytest can import just the classes/functions without running anything
- **Reusability**: Other programs can import your code as a library
- **Professionalism**: This is the industry standard


## 🔍 A Deeper Look: What IS `__name__`?

`__name__` is a special built-in variable that Python automatically sets in every module. Its value depends on HOW the file is being used:

| How file is used | Value of `__name__` | Example |
|-----|------|---------|
| Run directly | `"__main__"` | `python convention_manager.py` |
| Imported | The module name | `from convention_manager import Delegation` → `__name__` is `"convention_manager"` |

{{< slides-break >}}

{{< try >}} Create two files to see this in action:

**File 1: `module_demo.py`**
```python
print(f"Inside module_demo.py: __name__ = {__name__}")

def greet():
    return "Hello from module_demo!"

if __name__ == "__main__":
    print("This file was run directly!")
```


**File 2: `main_program.py`**
```python
import module_demo

print(f"Inside main_program.py: __name__ = {__name__}")
print(module_demo.greet())
```

{{< slides-break >}}

**When you run `python module_demo.py`:**
```
Inside module_demo.py: __name__ = __main__
This file was run directly!
```

**When you run `python main_program.py`:**
```
Inside module_demo.py: __name__ = module_demo
Inside main_program.py: __name__ = __main__
Hello from module_demo!
```

::: {.fragment}

{{< notice >}} The "This file was run directly!" message doesn't appear when imported!

:::


# 🔧 Task 10.5: The Guardrail Challenge

**Scenario:**

Henry Dunant needs a simple program to log when Red Cross volunteers arrive for their shifts. However, the program must be structured professionally so it can be tested and reused.

**Your Tasks:**

1. **Create a file called `shift_logger.py` with:**

   - A class `Volunteer` with attributes: `name` and `shift_time`
   - A function `log_arrival(volunteer)` that prints: `"✅ {name} arrived for {shift_time} shift"`
   - A `main()` function that:
     - Creates 2-3 volunteer instances
     - Calls `log_arrival()` for each
     - Prints a summary message
   - The proper `if __name__ == "__main__":` guard

2. **Create a test file called `test_shift_logger.py` that:**

   - Imports the `Volunteer` class and `log_arrival` function
   - Tests that a `Volunteer` instance stores name and shift_time correctly
   - Verifies that `log_arrival()` doesn't crash (basic smoke test)

3. **Verify your implementation:**

   - Run `python shift_logger.py` → Should see volunteer arrivals logged
   - Run `pytest test_shift_logger.py` → Should see tests pass WITHOUT the main() execution messages appearing


**Success criteria:**

- ✅ Running the file directly shows the volunteer logging
- ✅ Importing the file (via pytest) does NOT trigger the logging
- ✅ Tests pass cleanly
- ✅ Code follows the three-zone structure (Imports, Definitions, Execution)

**Bonus Challenge:**

Add a `pytest.fixture` for creating a test volunteer to avoid repetition in your tests!

**Reflection Questions (Self-Study):**

1. What happened when you forgot the `if __name__ == "__main__":` block?
2. Why is it important that pytest can import your classes without running main()?
3. Could another program import and reuse your `Volunteer` class? How?

## The Golden Rule: 

**If your `.py` file contains classes or functions that others might import, use the main guard. When in doubt, use it anyway—it never hurts!**

```{python}
#| file: https://github.com/HWG-LU-Classroom-Simon-Kloker/programming1-session10/blob/main/lecture/task-10-4/solution/test_convention_manager.py
```
