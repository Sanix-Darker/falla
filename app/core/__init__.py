from app.core.Aol import Aol
from app.core.Ask import Ask
from app.core.Bing import Bing
from app.core.DogPile import DogPile
from app.core.DuckDuckGo import DuckDuckGo
from app.core.Gibiru import Gibiru
from app.core.Mojeek import Mojeek
from app.core.Google import Google
from app.core.Qwant import Qwant
from app.core.SearchEncrypt import SearchEncrypt
from app.core.StartPage import StartPage
from app.core.Yahoo import Yahoo
from app.core.Yandex import Yandex

ENGINES = {
    'aol': Aol,
    'ask': Ask,
    'bing': Bing,
    'dogpile': DogPile,
    'duckduckgo': DuckDuckGo,
    'gibiru': Gibiru,
    'mojeek': Mojeek,
    'qwant': Qwant,
    'searchencrypt': SearchEncrypt,
    'startpage': StartPage,
    'yahoo': Yahoo,
    'yandex': Yandex,
    'google': Google,
}
