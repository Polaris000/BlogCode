## Rasa Chatbot

This is the example package used in my blogpost Building a Chatbot.

The post discusses:
* what chatbots are
* what Rasa is at a high level
* Terminology like intents, entities, slots and stories
* training and testing a chatbot with Rasa.


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
$ rasa train --fixed-model-name contact_bot
```

### Chatting with the bot
To test your bot, pen a new terminal window and start a rasa shell session.
```
$ rasa shell
```
This will let you chat with your bot in your terminal. But if you want to cleaner UI and a little more info like what intents were identified and what entities were extracted, you can use Rasa X.

---

You can find me on medium [here](https://polaris000.medium.com).
