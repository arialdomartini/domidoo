<%namespace name="master" file="master.mak"/>
<%master:layout>
<%def name="pagetitle()">Domidoo</%def>

% for place in places:
  ${master.show_place(place)}
%endfor

</%master:layout>
