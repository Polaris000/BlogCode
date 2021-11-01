## Contact Information Chatbot v2

This is the example bot used I used in a recent workshop on Rasa.

The presentation discussed the basics of Rasa, starting from what a chatbot is, all the way to building one with Rasa.

This example builds on our v1 chatbot, the code for which you can find [here](../RasaChatbot).

### Improvements over Chatbot v1
- handles the sad path where the user may not want to provide information
- handles the case where the user may provide on partial information, like only their name or only their email
- provides the user with further actions once a valid name and email are supplied
    - the user can choose to end the conversation by choosing the "That's all" option
    - the user can provide another set of name and email by choosing the "Add More Information" option.
- makes use of custom actions
- makes use of rules
- has mutliple stories to handle different scenarios

### Contents
This project follows the format of a standard Rasa project. There's a directory called `data` for training data like nlu, stories, and rules.

There's a directory called `actions`, which contains all your custom actions.

You'll also find the `domain.yml` file, which mentions all your intents, entities, slots, responses and actions.

Finally, there's the `config.yml` file, which specifies the components your bot is comprised of.

### Usage
1. Clone this repo
2. Navigate to the RasaChatbot directory
3. Install rasa>=2.6.2 in an env.

Modify the files in `data/` or the `domain.yml` file to play around.

### Training the bot
#### Validating the data
Before training the bot, a good practice is to check for any inconsistencies in the stories and rules, though in a project this simple, it's unlikely to occur.
```
$ rasa data validate
```

#### Training
To train the bot, we simply use the rasa train command. We'll provide a name to the model for better organization, but it's not necessary.
```
$ rasa train --fixed-model-name contact_bot_v2
```

### Chatting with the bot
To test your bot, open a new terminal window and start a rasa shell session.
```
$ rasa shell
```
This will let you chat with your bot in your terminal. If you want a more interactive UI and a little more debugging information like what intents were identified and what entities were extracted, you can use Rasa X.

---

You can find me on medium [here](https://polaris000.medium.com).
