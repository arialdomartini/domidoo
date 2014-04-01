<%namespace name="master" file="master.mak"/>
<%namespace name="def_place" file="def_place.mak"/>

<%master:layout>
  <%def name="pagetitle()">Domidoo</%def>

  % for place in places:
    ${def_place.show(place)}
  %endfor

</%master:layout>
