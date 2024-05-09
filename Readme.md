- [API](#api)


# API
https://opentdb.com/api_config.php

När jag tryckte på "generate api url"
skickades en postrequest som jag såg i devtools.


Där kunde jag se payload vilket blir mina keys jag behöver använda för att hämta data.
Det kommer också med en token vars syfte är att man inte får samma frågor nästa gång man kör en sökning.
Detta är inget viktigt i nuläget så jag kommer inte ta med det.

trivia_amount: 10
trivia_category: any
trivia_difficulty: any
trivia_type: any
trivia_encode: default

För att skicka payloaden behöver jag skapa en klass som kan skicka en post request samt genom
user input ändra i payloaden

<option value="9">General Knowledge</option>
<option value="10">Entertainment: Books</option>
<option value="11">Entertainment: Film</option>
<option value="12">Entertainment: Music</option>
<option value="13">Entertainment: Musicals &amp; Theatres</option>
<option value="14">Entertainment: Television</option>
<option value="15">Entertainment: Video Games</option>
<option value="16">Entertainment: Board Games</option>
<option value="17">Science &amp; Nature</option>
<option value="18">Science: Computers</option>
<option value="19">Science: Mathematics</option>
<option value="20">Mythology</option>
<option value="21">Sports</option>
<option value="22">Geography</option>
<option value="23">History</option>
<option value="24">Politics</option>
<option value="25">Art</option>
<option value="26">Celebrities</option>
<option value="27">Animals</option>
<option value="28">Vehicles</option>
<option value="29">Entertainment: Comics</option>
<option value="30">Science: Gadgets</option>
<option value="31">Entertainment: Japanese Anime &amp; Manga</option>
<option value="32">Entertainment: Cartoon &amp; Animations</option>	






Any categori -> self.category ska inte existera i api call

Mer komplext spel -> funktion som kollar av diverse spelalternativ

Enkelt -> 20 frågor alltid, random kategori
Koppla ihopp två spelare på lokalhost
