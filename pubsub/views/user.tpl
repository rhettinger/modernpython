% rebase('base')
<div class="pure-g">
  <div class="pure-u-7-24 userlist">
    <section>
    % include('single_user', user=user, comb=comb)
    </section>
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
        <td> {{post_user.displayname}} </td>
        <td> @{{post.user}} </td>
        <td> {{comb.age(post)}} </td>
        <td> {{post.text}} </td>
      </tr>
      % end
    </table>
    </section>
  </div>
</div>
