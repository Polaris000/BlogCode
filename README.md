# Code Samples from my blog posts
![Untitled 51](https://user-images.githubusercontent.com/31214064/157730857-85924761-96fe-4314-b667-aead3222f369.png)

This is a repository of code samples from my blogposts. I'm writing on Medium at the moment. You can find me [here](https://polaris000.medium.com).

---
### Articles

| Link to the article on Medium  | Sample Code | Publish Date | Topics |
| ------------- | ------------- | ------------ | ------------ |
| ![](https://img.shields.io/badge/NEW-success/?style=flat-square) [Dissecting the Birthday Paradox](https://towardsdatascience.com/dissecting-the-birthday-paradox-c26754aff6b5) | [Code](./BirthdayParadox)| April, 2022| jupyter-notebook, statistics, pandas, matplotlib|
| [How do Chatbots Understand?](https://towardsdatascience.com/how-do-chatbots-understand-87227f9f96a7) | [Code](./CustomIntentClassifier) | February, 2022| rasa, python, chatbot, nlu |
|[Handling Chatbot Failure Gracefully](https://towardsdatascience.com/handling-chatbot-failure-gracefully-466f0fb1dcc5) | [Code](./FallbackExample) | December, 2021| rasa, python, chatbot, nlu |
| [Evaluating Multi-label Classifiers](https://towardsdatascience.com/evaluating-multi-label-classifiers-a31be83da6ea) | [Code](./MetricsMultilabel) | November, 2021| classification, sklearn, ml, metrics |
| [Rasa Chatbot v2 (not a post)](https://github.com/Polaris000/ContactBot)| [Code](https://github.com/Polaris000/ContactBot) | October, 2021| rasa, python, chatbot, nlu |
| [Building a Chatbot with Rasa](https://towardsdatascience.com/building-a-chatbot-with-rasa-3f03ecc5b324)  | [Code](./RasaChatbot) | September, 2021| rasa, python, chatbot, nlu |
| [How Imports Work in Python](https://betterprogramming.pub/how-imports-work-in-python-59c2943d87dc?sk=9034d9c99e6b83d93a3c1a37f000f4a7)  | [Code](./PythonImportExample)  | June, 2021| python, imports |
| [Python: Decorators in OOP](https://towardsdatascience.com/python-decorators-in-oop-3189c526ead6)  | [Code](./PythonDecorators) | January, 2021| python, oop, decorators |
| [How Neural Networks Solve the XOR Problem](https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7)  | [Code](./XOR_Perceptron) | November, 2020| python, jupyter-notebook, matplotlib |
| [Understanding Dynamic Programming](https://towardsdatascience.com/understanding-dynamic-programming-75238de0db0d)  | [Code](./DynamicProgramming) | October, 2020| python, algorithms, dynamic programming |
| [Understanding Maximum Likelihood Estimation](https://polaris000.medium.com/understanding-maximum-likelihood-estimation-e63dff65e5b1)  | TBA | August, 2020| statistics |
| [Visualizing the Defective Chessboard Problem](https://polaris000.medium.com/visualizing-the-defective-chessboard-problem-aa5fc38b6e5e)  | [Code](./DefectiveChessBoard/) | Jan, 2020| algorithms |

---
### Star History Chart

[![Star History Chart](https://api.star-history.com/svg?repos=Polaris000/BlogCode&type=Date)](https://star-history.com/#Polaris000/BlogCode&Date)

Checkout [star-history.com](https://star-history.com) to get a star plot like the one above.

Also, if you found this repository useful, please do leave a star!

---
### Usage
-  Fork this repo
-  Clone it
  ```
  https://github.com/Polaris000/BlogCode.git
  ```
- Create an environment with the required packages installed. (**More info below**)
- Navigate to a project
- Check the README inside each project for information specific to it.

---
### Managing environments and dependencies
- Creating an environment is straightforward. Though there are a few ways to do it, `conda` is a reliable way to go about it. Install conda from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
- To create an environment run:
  ```
  $ conda create --name <env_name> python=3.8.10
  ```
- After the setup is complete, activate the env.
  ```
  $ conda activate <env_name>
  ```

- The packages required to run these code samples are mainly of two kinds:
  - Rasa dependencies
  - Python data visualization and machine learning libraries

- If you want to install both, use `requirements/requirements.txt` in your env
  ```
  (env)$ pip install -r requirements/requirements.txt
  ```
- If you want to install rasa dependencies, use `requirements/rasa_requirements.txt` in your env
  ```
  (env)$ pip install -r requirements/rasa_requirements.txt
  ```
- If you want to install python machine learning dependencies only, use `requirements/non_rasa_requirements.txt` in your env
  ```
  (env)$ pip install -r requirements/non_rasa_requirements.txt
  ```

#### Notes
- If you're interested in using [Rasa X](https://rasa.com/docs/rasa-x/) for a more visual experience while improving and conversing with your bot, you'll require these additional steps:
  - Downgrade pip to fix a circular dependency issue
    ```
    $ pip install pip==20.2
    ```
  - Install rasa x
    ```
    $ pip install install rasa-x==0.38.1 --extra-index-url https://pypi.rasa.com/simple
    ```

---
