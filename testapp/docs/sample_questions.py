from datetime import date

questions = [
[Question(
    summary='Factorial',
    points=2,
    type="python",
    description='''
Write a function called <code>fact</code> which takes a single integer argument
(say <code>n</code>) and returns the factorial of the number. 
For example:<br/>
<code>fact(3) -> 6</code>
''',
    test='''
assert fact(0) == 1
assert fact(5) == 120
'''),
#Add tags here as a list of string.
['Python','function','factorial'],
],

[Question(
    summary='Simple function',
    points=1,
    type="python",
    description='''Create a simple function called <code>sqr</code> which takes a single 
argument and returns the square of the argument. For example: <br/>
<code>sqr(3) -> 9</code>.''',
    test='''
import math
assert sqr(3) == 9
assert abs(sqr(math.sqrt(2)) - 2.0) < 1e-14 
    '''),
#Add tags here as a list of string.
['Python','function'],
],

[Question(
    summary='Bash addition',
    points=2,
    type="bash",
    description='''Write a shell script which takes two arguments on the
    command line and prints the sum of the two on the output.''',
    test='''\
docs/sample.sh
docs/sample.args
'''),
#Add tags here as a list of string.
[''],
],

[Question(
    summary='Size of integer in Python',
    points=0.5,
    type="mcq",
    description='''What is the largest integer value that can be represented
in Python?''',
    options='''No Limit
2**32
2**32 - 1
None of the above
''',
    test = "No Limit"
    ),
#Add tags here as a list of string.
['mcq'],
],

] #list of questions ends here

quiz = Quiz(start_date=date.today(),
            duration=10,
            description='Basic Python Quiz 1'
            )