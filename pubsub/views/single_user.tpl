
    <hr>
    <p> <strong> {{comb.user_info[user].displayname}} </strong> @{{user}} </p>
    <p> <img src="/static/{{comb.user_info[user].photo}}" alt="Photo of {{user}}" width="250"> </p>
    <p> {{comb.user_info[user].bio}} </p>
    <a class="pure-button" href="/{{user}}"> {{len(comb.user_posts[user])}} Posts </a>
    <a class="pure-button" href="/{{user}}/following"> {{len(comb.following[user])}} Following </a>
    <a class="pure-button" href="/{{user}}/followers"> {{len(comb.followers[user])}} Followers </a>

