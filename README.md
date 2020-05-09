# IRC-client
#### Technologies: Python, Tkinter

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
* [Prerequisites](#Prerequisites)
* [Usage](#Usage)
* [Unit Tests](#Testing)
* [Screen Shots](#Shots)
* [References](#References)

## <a name="Install">Installation</a>
* To clone the repo
```shell
$ git clone git@github.com:VaporFoxLash/IRC-client.git
$ cd IRC-client
 ```

## <a name="Prerequisites">Prerequisites<a/>
```shell
$ pip install tkinter
```

## <a name="Usage">Usage</a>
```shell
$ python irc_client.py
```

Enter your username and channel you want to join in freenode server.
When the second window pops up enter the message and hit enter to send, click leave channel to exit the channel.

## <a name="Testing">Running the tests</a>
```shell
$ python test_irc_client.py

```

## <a name="Shots">Screen Shots</a>
![](https://raw.githubusercontent.com/VaporFoxLash/IRC-client/master/img/Screenshot0.png)


## <a name="References">References</a>
* Wikipedia
https://en.wikipedia.org/wiki/Internet_Relay_Chat

* RFC 1459 (Internet Relay Chat Protocol)                                             
https://tools.ietf.org/html/rfc1459
