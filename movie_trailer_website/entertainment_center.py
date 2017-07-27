import media
import fresh_tomatoes


# store the movie info in dict
movie_data = {
    "inception": {
        "title": "Inception",
        "story_line": "we don't use this item yet",
        "poster_image_url": "https://b-ssl.duitang.com/uploads/item/201201"
                            "/16/20120116230816_cskMu.thumb.700_0.jpg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=YoHD9XEInc0",
    },

    "titanic": {
        "title": "Titanic",
        "story_line": "we don't use this item yet",
        "poster_image_url": "http://i0.hexunimg.cn/2012-04-03/140031914.jpg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
    },

    "life_of_pi": {
        "title": "Life of Pi",
        "story_line": "we don't use this item yet",
        "poster_image_url": "http://img170.poco.cn/mypoco/myphoto/20121121"
                            "/14/66523397201211211357423112115279365_006.jpg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=5GbXVo9DdZo",
    },

    "up": {
        "title": "Up",
        "story_line": "we don't use this item yet",
        "poster_image_url": "http://mt4.haibao.cn/img/600_0_100_1/1246622594"
                            ".0283/bigfiles/200926/1246622594.0283.jpg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=ORFWdXl_zJ4"
    },

    "zootopia": {
        "title": "Zootopia",
        "story_line": "we don't use this item yet",
        "poster_image_url": "http://zjimg.5054399.com/allimg"
                            "/160310/16_160310105944_9.jpg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=jWM0ct-OLsM",
    },

    "wall": {
        "title": "WALL-E",
        "story_line": "we don't use this item yet",
        "poster_image_url": "http://img3.duitang.com/uploads/item"
                            "/201506/05/20150605215538_kLjG2.jpeg",
        "trailer_youtube_url": "https://www.youtube.com/watch?v=alIq_wG9FNk",
    },
}

# store the instance of Movie
movies = []

# Looping through movie_data to crearte their instance and saving them in array
for movie_name, movie_detail in movie_data.items():
    movies.append(media.Movie(movie_detail["title"],
                              movie_detail["story_line"],
                              movie_detail["poster_image_url"],
                              movie_detail["trailer_youtube_url"],))

fresh_tomatoes.open_movies_page(movies)
