<%namespace name="master" file="master.mak"/>
<%master:layout>
<%def name="pagetitle()">Domidoo</%def>

% for place in places:
  <div class="col-md-12">
    ${place.name}
  </div>
  <div class="col-md-12">
    <image src="/images/${place.image}" width="350px" />
  </div>
  % for tag in place.tags:
    ${tag.name}
  % endfor
%endfor

</%master:layout>
