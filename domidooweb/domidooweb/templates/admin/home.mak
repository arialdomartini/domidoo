<%namespace name="master" file="../master.mak"/>
<%master:layout>
<%def name="pagetitle()">Admin</%def>
<h1>Admin area</h1>
<h2>Places</h2>
<ul>
  <li>
    <a href="${request.route_url('admin.places')}">List all the places</a>
  </li>
  <li>
    <a href="${request.route_url('admin.places.new')}">Add a new place</a>
  </li>
  <li>
    JSON POST: Add a new place ${request.route_url('admin.places.new.json')}
  </li>
</ul>
<h2>Tags</h2>
<ul>
  <li>
    <a href="${request.route_url('admin.tags')}">List all the tags</a>
  </li>
  <li>
    <a href="${request.route_url('admin.tags.new')}">Add a new tag</a>
  </li>
</ul>
</%master:layout>
