from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    games = get_game_options()
    #print(games)
    return render_template('index.html', game_options=games)

@app.route("/page2")
def render_page2():
    games = get_game_options()
    #print(games)
    return render_template('gameFacts.html', game_options=games)

@app.route("/page3")
def render_page3():
    with open('video_games.json') as videoGames_data:
        videoGames = json.load(videoGames_data)
    consoles = get_console_options()
    #print(games)
    if "console" in request.args:
            game_list=[]
            console = request.args.get('console')
            for games in videoGames:
                if games["Release"]["Console"]==console:
                    game_list.append(games["Title"])
            return render_template('consolGames.html', console_options=consoles, consoleFacts=game_list)
    return render_template('consolGames.html', console_options=consoles)

@app.route("/page4")
def render_page4():
    with open('video_games.json') as videoGames_data:
        videoGames = json.load(videoGames_data) 
    publishers = get_publisher_options()
    #print(games)
    if "publisher" in request.args:
            game_list=[]
            publisher = request.args.get('publisher')
            for games in videoGames:
                if games["Metadata"]["Publishers"]==publisher:
                    game_list.append(games["Title"])
            return render_template('gamePublisher.html', publisher_options=publishers, publisherFacts=game_list)
    return render_template('gamePublisher.html', publisher_options=publishers)
    
@app.route('/showGameFact')
def render_fact():
     with open('video_games.json') as videoGames_data:
        videoGames = json.load(videoGames_data)
        games2 = get_game_options()
        if "game" in request.args:
        
            game = request.args.get('game')
            for games in videoGames:
                if games["Title"] == game:
                    ishandheld = games["Features"]["Handheld?"]
                    maxPlayers = games["Features"]["Max Players"]
                    Multiplat = games["Features"]["Multiplatform?"]
                    online = games["Features"]["Online?"]
                    genre = games["Metadata"]["Genres"]
                    licen = games["Metadata"]["Licensed?"]
                    publish = games["Metadata"]["Publishers"]
                    sequel = games["Metadata"]["Sequel?"]
                    review = games["Metrics"]["Review Score"]
                    sale = games["Metrics"]["Sales"]
                    used = games["Metrics"]["Used Price"]
                    console = games["Release"]["Console"]
                    rating = games["Release"]["Rating"]
                    re_release = games["Release"]["Re-release?"]
                    year = games["Release"]["Year"]
                    average = games["Length"]["All PlayStyles"]["Average"]
                    leisure = games["Length"]["All PlayStyles"]["Leisure"]
                    median = games["Length"]["All PlayStyles"]["Median"]
                    polled = games["Length"]["All PlayStyles"]["Polled"]
                    rushed = games["Length"]["All PlayStyles"]["Rushed"]
                    average2 = games["Length"]["Completionists"]["Average"]
                    leisure2 = games["Length"]["Completionists"]["Leisure"]
                    median2 = games["Length"]["Completionists"]["Median"]
                    polled2 = games["Length"]["Completionists"]["Polled"]
                    rushed2 = games["Length"]["Completionists"]["Rushed"]
                    average3 = games["Length"]["Main + Extras"]["Average"]
                    leisure3 = games["Length"]["Main + Extras"]["Leisure"]
                    median3 = games["Length"]["Main + Extras"]["Median"]
                    polled3 = games["Length"]["Main + Extras"]["Polled"]
                    rushed3 = games["Length"]["Main + Extras"]["Rushed"]
                    average4 = games["Length"]["Main Story"]["Average"]
                    leisure4 = games["Length"]["Main Story"]["Leisure"]
                    median4 = games["Length"]["Main Story"]["Median"]
                    polled4 = games["Length"]["Main Story"]["Polled"]
                    rushed4 = games["Length"]["Main Story"]["Rushed"]
            return render_template('gameFactextanded.html', ishandheld=ishandheld, maxPlayers=maxPlayers, Multiplat=Multiplat, online=online, genre=genre, licen=licen, publish=publish, sequel=sequel, review=review, sale=sale, used=used, console=console, rating=rating, re_release=re_release, year=year, average=average, leisure=leisure, median=median, polled=polled, rushed=rushed, average2=average2, leisure2=leisure2, median2=median2, polled2=polled2, rushed2=rushed2, average3=average3, leisure3=leisure3, median3=median3, polled3=polled3, rushed3=rushed3, average4=average4, leisure4=leisure4, median4=median4, polled4=polled4, rushed4=rushed4, game_options=games2)
        return render_template('gameFacts.html', ishandheld=ishandheld, maxPlayers=maxPlayers, Multiplat=Multiplat, online=online, genre=genre, licen=licen, publish=publish, sequel=sequel, review=review, sale=sale, used=used, console=console, rating=rating, re_release=re_release, year=year, average=average, leisure=leisure, median=median, polled=polled, rushed=rushed, average2=average2, leisure2=leisure2, median2=median2, polled2=polled2, rushed2=rushed2, average3=average3, leisure3=leisure3, median3=median3, polled3=polled3, rushed3=rushed3, average4=average4, leisure4=leisure4, median4=median4, polled4=polled4, rushed4=rushed4, game_options=games2)
#the Json file has some misinformation (espely with call of duty 2) I don't know how to fix it and with games with multipel enterys, one versoin will over write another version

                

def get_game_options():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('video_games.json') as video_games_data:
        VidGa = json.load(video_games_data)
    games=[]
    for v in VidGa:
            games.append(v["Title"])
    options=""
    for g in games:
        options += Markup("<option value=\"" + g + "\">" + g + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
    
def get_console_options():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('video_games.json') as video_console_data:
        VidCon = json.load(video_console_data)
    consoles=[]
    for v in VidCon:
        if v["Release"]["Console"] not in consoles:
            consoles.append(v["Release"]["Console"])
    options=""
    for g in consoles:
        options += Markup("<option value=\"" + g + "\">" + g + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
    
def get_publisher_options():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('video_games.json') as video_publisher_data:
        VidPub = json.load(video_publisher_data)
    publishers=[]
    for v in VidPub:
        if v["Metadata"]["Publishers"] not in publishers:
            publishers.append(v["Metadata"]["Publishers"])
    options=""
    for g in publishers:
        options += Markup("<option value=\"" + g + "\">" + g + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

    
if __name__ == '__main__':
    app.run(debug=True)