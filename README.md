# speakers


##Bootstraping for MAC OS X

We are going to use [Python](http://wiki.python.org.br/) as a mainly language in this project and [pip](https://pypi.python.org/pypi/pip) for installing Python packages. 


####Install virtualenv

The [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool that will provide us a isolated Python environment to run our application. Beyond control dependencies and versions. To install it open the terminal and run the follow line:

```
sudo pip install virtualenv
```

####Install virtualenvwrapper

[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) is a set of extension for virtualenv tool. To install it open the terminal and run the follow line:
```
sudo pip install virtualenvwrapper
```
Run the follow lines to create a space in HOME for virtual enviroments. 

```
cd $HOME
mkdir .virtualenvs
```

Open the .bash_login add the follow line to set the location where the virtual environments should live.

```
source /usr/local/bin/virtualenvwrapper.sh
```

Here you can see the documentation for [virtualenvwrapper](with http://virtualenvwrapper.readthedocs.org/en/latest/) that can help.


##Run speakers

python app.py

go to http://127.0.0.1:5000