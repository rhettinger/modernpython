<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title> PubSub Demo </title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
    <link rel="icon" href="/static/ps_favicon.ico" type="image/x-icon">
    <style>
      body {
          background-color: LightSteelBlue;
          margin-right: 50px;
          margin-left:  50px;
      }
      section   { padding: 20px; }
      .userlist { background-color: PapayaWhip; }
      .postlist { background-color: MistyRose; }
      .newpost  { width: 100%; }
      .search   { width: 30em; }
    </style>
  </head>
  <body>
    <header class="pure-g">
      <h1 class="pure-u-1-2"> Messenger </h1>

      <form class="pure-u-1-2 pure-form" method="get" action="/search">
        <input type="text" class="pure-input-rounded search" name="phrase">
        <button type="submit" class="pure-button"> Search </button>
      </form>
    </header>

    {{!base}}
</body>
</html>
