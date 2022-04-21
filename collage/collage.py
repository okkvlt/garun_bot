import io
from typing import List

import requests
from PIL import Image

from .types import Album, AlbumImage, Artist, Track


class LastFM:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _get_top_tracks(self, user: str, period: str = '1month', limit: int = 50) -> List[Track]:
        response = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={user}&limit={limit}&period={period}&api_key={self.api_key}&format=json')
        response_json = response.json()

        if 'error' in response_json.keys():
            raise Exception(response_json['message'])

        tracks = []

        for track in response_json['toptracks']['track']:
            artist = Artist(**track['artist'])

            track.pop('artist')
            track.pop('image')
            track.pop('@attr')
            track.pop('streamable')
            track.pop('duration')
            track.pop('playcount')

            tracks.append(Track(artist=artist, **track))

        return tracks

    def _get_top_artists(self, user: str, period: str = '1month', limit: int = 150) -> List[Artist]:
        """Busca lista de artistas mais escutados no período selecionado.

        Args:
            user (str): Usuário a ser buscado.
            period (str, optional): Período a ser buscado. Defaults to '1month'.
            limit (int, optional): Limite de resultados. Defaults to 150.

        Raises:
            Exception: Erro retornado pela API.

        Returns:
            List[Artist]: Lista de artistas retornados.
        """

        response = requests.get(f'https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={user}&limit={limit}&period={period}&api_key={self.api_key}&format=json')
        response_json = response.json()

        if 'error' in response_json.keys():
            raise Exception(response_json['message'])

        artists = []

        for artist in response_json['topartists']['artist']:
            artists.append(Artist(url=artist['url'], name=artist['name'], mbid=artist['mbid']))

        return artists

    def _get_top_albums(self, user: str, period: str = '1month', limit: int = 150) -> List[Album]:
        """Busca lista de álbuns mais escutados no períodos selecionado.

        Args:
            user (str): Usuário a ser buscado.
            period (str, optional): Período de tempo a ser buscado. Defaults to '1month'.
            limit (int, optional): Limite de resultados. Defaults to 150.

        Raises:
            Exception: Erro retornado pela API.

        Returns:
            List[Album]: Lista de álbuns retornados.
        """

        response = requests.get(f"https://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user={user}&limit={limit}&period={period}&api_key={self.api_key}&format=json")
        response_json = response.json()

        if 'error' in response_json.keys():
            raise Exception(response_json['message'])

        albums = []

        for album in response_json['topalbums']['album']:
            artist = Artist(**album['artist'])

            images = []

            for image in album['image']:
                image['url'] = image.pop("#text")
                images.append(AlbumImage(**image))

            album.pop('artist')
            album.pop('image')
            album.pop('@attr')

            albums.append(Album(artist=artist, images=images, **album))

        return albums

    def _gen_collage(self, images: List[Image.Image], art_width: int = 200, art_height: int = 200, collage_width: int = 1000, collage_height: int = 1000) -> Image.Image:
        """Gera colagem

        Args:
            images: (List[Image.Image]): Lista de imagens que irão compor o colagem.
            art_width (int, optional): Largura das imagens que irão compor o colagem. Defaults to 200.
            art_height (int, optional): Altura das imagens que irão compor o colagem. Defaults to 200.
            collage_width (int, optional): Largura da imagem final. Defaults to 1000.
            collage_height (int, optional): Altura da imagem final. Defaults to 1000.

        Returns:
            Image: Colagem montada.
        """

        collage = Image.new('RGB', (collage_width, collage_height), 'white')

        for i, img in enumerate(images):
            if img.size != (art_width, art_height):
                img = img.resize((art_width, art_height))

            line = int(i // (collage_height / art_width))

            x = (i * art_width) % collage_width
            y = line * art_height

            collage.paste(img, (x, y))

        return collage

    def gen_top_albums_collage(self, user: str, period: str = '1month', limit: int = 50, **kwargs) -> Image.Image:
        """Gera colagem dos álbuns mais escutados.

        Args:
            user (str): Usuário do last.fm
            period (str, optional): Período a ser buscado. eg. overall | 7day | 1month | 12month. Defaults to 1month.
            limit (int, optional): Limite de álbuns. Defaults to 50.

        Returns:
            Image.Image: Colagem montada.
        """

        albums = self._get_top_albums(user, period)

        imgs = []

        for album in albums:
            if len(imgs) == limit:
                break

            img_url = album.images[-1].url

            # Pula álbuns que não têm imagem.
            if not img_url:
                continue

            img = Image.open(io.BytesIO(requests.get(img_url).content))

            imgs.append(img)

        return self._gen_collage(imgs, **kwargs)

    def gen_top_artists_collage(self, user: str, period: str = '1month', limit: int = 50, **kwargs) -> Image.Image:
        """Gera colagem dos artistas mais escutados.

        Args:
            user (str): Usuário do last.fm
            period (str, optional): Período a ser buscado. eg. overall | 7day | 1month | 12month. Defaults to 1month.
            limit (int, optional): Limite de álbuns. Defaults to 50.

        Returns:
            Image.Image: Colagem montada.
        """

        artists = self._get_top_artists(user, period)

        imgs = []

        for artist in artists:
            if len(imgs) == limit:
                break

            if image := artist.image:
                imgs.append(image)

        return self._gen_collage(imgs, **kwargs)

    def gen_top_tracks_collage(self, user: str, period: str = '1month', limit: int = 50, **kwargs) -> Image.Image:
        """Gera colagem das músicas mais escutados.

        Args:
            user (str): Usuário do last.fm
            period (str, optional): Período a ser buscado. eg. overall | 7day | 1month | 12month. Defaults to 1month.
            limit (int, optional): Limite de músicas. Defaults to 50.

        Returns:
            Image.Image: Colagem montada.
        """

        tracks = self._get_top_tracks(user, period)

        imgs = []

        for track in tracks:
            if len(imgs) == limit:
                break

            imgs.append(track.image)

        return self._gen_collage(imgs, **kwargs)
