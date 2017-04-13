% rebase('base')
<div class="pure-g">
  <div class="pure-u-7-24 userlist">
    % if user:
    <section>
    % include('single_user', user=user, comb=comb)

    <hr>
    <h2> Post a new message </h2>
    <form class="pure-form" method="post" action="/postmessage">
      <input class="newpost" name="text" type="text">
      <button type="submit" class="pure-button pure-button-primary"> Post </button>
    </form>
    </section>
    % end
  </div>

  <div class="pure-u-1-24"> </div>

  <div class="pure-u-2-3 postlist">
    <section>
    <hr>
    <h2> {{heading}} </h2>
    <table class="pure-table pure-table-horizontal">
      % for post in posts:
      %     post_user = comb.user_info[post.user]
      <tr>
        <td> <img src="/static/{{post_user.photo}}" height="75" alt="Photo of {{post.user}}"> </td>
        <td> <a href="/{{post.user}}"> <strong> {{post_user.displayname}} </strong> </a> </td>
        <td> <a href="/{{post.user}}"> @{{post.user}} </a> </td>
        <td> {{comb.age(post)}} </td>
        <td> {{post.text}} </td>
      </tr>
      % end
    </table>
    </section>
  </div>
</div>
