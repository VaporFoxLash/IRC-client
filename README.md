# IRC-client
Internet Relay Chat (IRC) is an application layer protocol that facilitates communication in the form of text. 
The chat process works on a client/server networking model. 
IRC clients are computer programs that users can install on their system or web based applications 
-running either locally in the browser or on a 3rd party server. 
These clients communicate with chat servers to transfer messages to other clients.
[1] IRC is mainly designed for group communication in discussion forums, called channels,
[2] but also allows one-on-one communication via private messages
[3] as well as chat and data transfer,
[4] including file sharing.

## Index
* [Installation](#Install)
* * [Usage](#Usage)
* [Screen Shots](#Shots)

## <a name="Install">Installation</a>
* To clone the repo
```shell
$ git clone git@github.com:VaporFoxLash/IRC-client.git
$ cd IRC-client
 ```

## Prerequisites
```shell
$ pip install tkinter
```

## Ussage:
```shell
$ python irc_client.py
```

Enter your username and channel you want to join in freenode server.
When the second window pops up enter the message and hit enter to send, click leave channel to exit the channel.

# Running the tests
```shell
$ python -m test_irc_client.py
```
