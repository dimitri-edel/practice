from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData, URL
)

url_object = URL.create(
    "postgresql+psycopg2",
    username="workoutapp",
    password="w2r4k2t3!",  # plain (unescaped) text
    host="8e837af.online-server.cloud",
    database="chinook",
)
db = create_engine(url_object)

meta = MetaData()

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)

)
with db.connect() as connection:
    # Qeury 1 - select all from the artist_table
    # select_query = artist_table.select()

    # Qeury 2 - select only name column from the artista_table
    # select_query = artist_table.select().with_only_columns(artist_table.c.Name)

    # Qeury 3 - select only 'Queen' from the artist_table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Qeury 4 -  select only by 'AritstId' #51 from the artist_table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the 'Album' table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all titles by 'Queen' from track_table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")


    results = connection.execute(select_query)
    for result in results:
        print(result)