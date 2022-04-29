import mal_scraper as mal

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    animeVillard = getAnime('Villard_')
    animeMexbot = getAnime('Maxib')

    return render_template('./index.html', animeVillard=animeVillard, animeMexbot=animeMexbot)


def getAnime(user):
    animeList = mal.get_user_anime_list(user)

    for anime in animeList:
        if anime['name'] == 'One Piece':
            return anime


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)