## Failing Gracefuuly

This is the example bot to demonstrate the fallback scenarios provided by Rasa. Its sample code from the post on Fallback Strategies, which can be found on [Medium.com](https://towardsdatascience.com/handling-chatbot-failure-gracefully-466f0fb1dcc5).

It builds upon our existing example, which can be found [here](../RasaChatbot_v2).



### Improvements over Chatbot v2
- addition of fallback mechanisms
- addition of simple, single stage and two stage fallback mechanisms
- support for asking the user to rephrase themselves
- support for asking the user to select from some suggestions

A few examples:

**Simple Fallback**
```
👨 : !@#?*& (something the bot doesn't understand)

🤖 : Sorry! Let me connect you to a human...

```

**Single-Stage Fallback**
```
👨 : !@#?*& (something the bot doesn't understand)

🤖 : Sorry! What do you want to do?
    (a) Supply Contact information
    (b) Agree
    (c) Disagree
    (d) End the converation
    (e) None of these

👨 : (e) None of these (button click)

🤖 : Sorry! Let me connect you to a human...
```
**Two-stage fallback**
```
👨 : !@#?*& (something the bot doesn't understand)

🤖 : Sorry! What do you want to do?
    (a) Supply Contact information
    (b) Agree
    (c) Disagree
    (d) End the converation
    (e) None of these

👨 : (e) None of these (button click)

🤖 : I'm sorry, I didn't quite understand that. Could you rephrase?

👨 : !@#?*& (again, something the bot doesn't understand)

🤖 : Sorry! What do you want to do?
    (a) Supply Contact information
    (b) Agree
    (c) Disagree
    (d) End the converation
    (e) None of these

👨 : (e) None of these (button click)

🤖 : Sorry! Let me connect you to a human...
```


### Contents
This project follows the format of a standard Rasa project. There's a directory called `data` for training data like nlu, stories, and rules.

There's a directory called `actions`, which contains all your custom actions.

You'll also find the `domain.yml` file, which mentions all your intents, entities, slots, responses and actions.

Finally, there's the `config.yml` file, which specifies the components your bot is comprised of.

The config file has a modification compared to the previous versions of this bot: low training epochs for the `DIETClassifier`. This is to simulate fallback behaviour. If you want to build a properly functioning bot, increase epochs to about 100.

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

### Testing the various fallback strategies
To test the different fallback strategies, simply comment out the rules for all except for the one you want to test. These rules are located along with the regular rules in `rules.yml`.

After this, retrain the bot to test the strategy. Be sure to keep the epochs for your `DIETClassifier` low (below 5), to simulate nlu_fallback reliably.

---

You can find me on medium [here](https://polaris000.medium.com).
