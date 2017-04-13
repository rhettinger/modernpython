% rebase('base')

<section class="userlist">
    <h2> {{who_does_what}} </h2>
      % for user in users:
      %     include('single_user', user=user, comb=comb)
      % end
</section>
