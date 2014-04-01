<%def name="show_place(place)">

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
</%def>
