<%namespace name="master" file="../master.mak"/>
<%master:layout>
<%def name="pagetitle()">Admin</%def>
<h1>Admin area</h1>
<ul>
  <li>
    Add a new place [POST] ${request.route_url('admin.places.new')}
  </li>
</ul>

</%master:layout>
