# Resurrect the Evolution

## RU

Мы провели мысленный эксперимент, который продлился двое суток.
Можно сказать, мы придумали метаигру.

Каким, по-вашему, будет конец человечества? Мы представили один из вариантов.
На эти двое суток мы оказались в мире, подобном мирам Оруэлла или Хаксли.

Колония людей пытается выжить на новой планете вдали от Земли.
Биологическое разнообразие обеспечивается заранее заготовленным генетическим материалом.
Воспроизводимое потомство вполне здорово физически и готово к дальнейшему размножению.

Однако тесная культурная среда, ограниченный круг общения и однообразие в обучении
и мировосприятии между людьми приводят к серьёзным социальным проблемам.
Люди не видят стимула для развития, растёт уровень преступности, психических расстройств.
Люди попали в культурный тупик. Значительная часть механизмов эволюции остановилась.

Метаигра предлагает погрузиться в проблемы нового мира и сохранить человечество,
перезапустив эволюцию.

Наше решеие предлагает воссоздать базовые механизмы культурного разнообразия.
Предлагается применить жёсткие меры для расселения разных групп населения на разные
территории, ограничив возможности общения между группами на значительное время.

Мы сфокусировались на одном из инструментов, который помог бы восстановить разнообразие
человеческих языков. Мы создали генератор самодостаточных человеческих языков.
Расселяемые на разные территории группы людей должны разговаривать на разных языках.

Демонстрация инструмента: генерация языка, орфографический словарь, грамматические правила,
азбука, толковый словарь.


## EN

We conducted thought experiment that lasted for two days.
We some kind of invented a metagame.

How do you think, what would be the end of humanity? We thought of one of possibilities.
For the last two days we dove into the world similar to Aldous Huxley' or George Orwell's worlds.

A colony of people tries to survive on foreign planet far far away from the Earth.
Biological diversity guaranteed by genetic material brought from homeplanet.
The offspring is healthy and ready to bring new generations.

But. Very narrow cultural environment, limited circles of communication and uniformity
of education and opinions of the people around entail to serious social problems.
People don't want to develop themselves. Crime is rising. Psychological problems appear.
Culture does not progress. A lot of evolution mechanisms stopped.

Metagame offers to dive to the problems of brave new world and to save humanity.
All you need to do -- is to resurrect the evolution.

Our solution to the problem is to recreate basic mechanisms of cultural diversity.
We propose to take strong measures to resettle different groups of people
to different areas for a long-long time. It is necessary to restrict communication
between those groups.

We focused on one of the tools which can help to restore diversity in human
languages. To achieve this, we created a generator of self-sufficient languages.
Resettled groups of people should speak different languages.

Tool demonstration: language generation, orphographic dictionary, grammar,
abc, explanatory dictionary.

## Features

using part of speech: noun, verb, adjectives, preposition, articles

- Language basement generation:
    - Grammar (using part of speech: noun, verb, adjectives, preposition, articles)
    - ABC from custom word list
    - Dictionary for all made up words during text translations
- Text translation any number of text at a time (see Makefile)
- Repetition of generation depends on name of new language


# How to use

- Come up a new language name
- Put togather texts for translation in English
- Use resurrection tool (see examples in Makefile)


## How to install dependencies

    $ pip3 install nltk
    python3
    >>> nltk
    >>> nltk.download('wordnet')
    >>> nltk.download('averaged_perceptron_tagger')
    >>> nltk.download('tagsets')
    >>> nltk.download('punkt')
