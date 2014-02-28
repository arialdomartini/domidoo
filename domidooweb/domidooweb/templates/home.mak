<%namespace name="master" file="master.mak"/>
<%master:layout>
<%def name="pagetitle()">Domidoo</%def>

<div class="col-md-12">
  ${place.name}
</div>
<div class="col-md-12">
  <image src="/images/${place.image}" width="350px" />
</div>

</%master:layout>
