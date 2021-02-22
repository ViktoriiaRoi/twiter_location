<a href="https://twitter.com"><img src="https://img.icons8.com/color/48/000000/twitter--v1.png"/></a>
# Twitter Location
This application give an opportunity to see a location of user's friends on Twitter

## How to use the application
1. Download all files
2. Start application.py
3. Enter a username in the input field
4. Enter your bearer token in the input field
5. Tap on "Build a map"

## Modules
* application.py - creates site by flask and catches requests
* location.py - find location of user's friends by Twitter API
* build_map.py - build map with friend's locations by folium

## Templates
* index.html - main screen, where user should enter name of account
* empty.html - screen with error, when user doesn't input name
* failure.html - screen with error, when user with this name isn't exist or hasn't friends with location
* layout.html - template for these 3 screens
* Friends_map.html - are generated and shown when user tap a button (if there aren't any errors)

## Example of working program
![map1](https://user-images.githubusercontent.com/44781809/108779682-ea709b00-756f-11eb-8055-1e1020d24953.jpg)
![map2](https://user-images.githubusercontent.com/44781809/108752342-02cebe80-754c-11eb-8086-262bb716e26c.jpg)
