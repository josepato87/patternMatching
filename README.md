# Pattern Matching
## How to run the program

Before running the program, run the following command to install the dependencies:
`pip install -r requirements.txt`


For running the program execute the patternMatching.sh file

`sh patternMatching.sh`

This will run the program with two given inputs.

For running with different input files, just run the following command in the root folder of the project:

`cat input/file/path | python3 app.py > input/file/path`

## Running tests
For running the test, you will need to install **pytest**. Then just execute the following command in the root folder of the project:

`pytest tests`

## Extra Credit Answers
**What's the algorithmic complexity of your program? In other words, how does its running time change as the number of patterns or number of paths increases?**

The complexity of this program is O(n^2), since it´s iterating for each path, then for each pattern. This means that if the ammount of patterns and paths increases, its performance will decrease.

**Would your program complete quickly even when given hundreds of thousands of patterns and paths? Is there a faster solution?**

With large ammounts of patterns and paths, the program will run slow.

Using **regex** would be another solution, however the code readability will decrease, and large ammount of data will affect the program too.

To mitigate this problem, an upgrade to the code would be to group the patterns by their length, and then by wildcard quantity. 

Using a "Trie" tree can increase the performance of the program with lots of paths and patterns data.

