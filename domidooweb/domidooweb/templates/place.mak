<%namespace name="master" file="master.mak"/>
<%master:layout>
<%def name="pagetitle()">Domidoo</%def>

<div class="col-md-12">
  ${place.name}
</div>
<div class="col-md-12">
  % for image in place.images:
     <image src="/images/${image.filename}" width="350px" />
  % endfor
</div>

% for tag in place.tags:
  ${tag.name}
% endfor


</%master:layout>
