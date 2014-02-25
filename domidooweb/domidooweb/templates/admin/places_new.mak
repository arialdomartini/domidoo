<%namespace name="master" file="../master.mak"/>
<%master:layout>
    <%def name="pagetitle()">Register a new place</%def>
        <div class="row">
          <div class="col-lg-16">
            <div class="well">
              <form class="bs-example form-horizontal" method="POST" accept-charset="utf-8" enctype="multipart/form-data">
                <fieldset>
                  <legend>New place</legend>
                  <div class="form-group">
                    <label for="title" class="col-lg-12 control-label">Name</label>
                    <div class="col-lg-12">
                      <textarea class="form-control" name="name" type="text" placeholder="Name">${name}</textarea>
                    </div>
                  </div>
                  <div class="form-group">
                     <label for="image" class="col-lg-12 control-label">Image</label>
                    <div class="col-lg-12">
                      <input name="image" class="form-control" type="file" value="" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="city" class="col-lg-12 control-label">City</label>
                    <div class="col-lg-12">
                      <textarea class="form-control" name="city" type="text" placeholder="The city">${city}</textarea>
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="col-lg-10 col-lg-offset-2">
                      <button type="submit" class="btn btn-primary">Save</button>
                    </div>
                  </div>
                </fieldset>
              </form>
            </div>
          </div>
</%master:layout>
