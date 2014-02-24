<%def name="layout()">
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>${caller.pagetitle()}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/static/css/bootstrap.css" media="screen">
    <link rel="stylesheet" href="/static/css/bootswatch.min.css">
    <link rel="stylesheet" href="/static/css/sticky-footer.css">
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/static/js/html5shiv.js"></script>
      <script src="/static/js/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="${request.route_url('home')}" class="navbar-brand">Domidoo</a>
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="navbar-collapse collapse" id="navbar-main">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#" id="tags">Tags <span class="caret"></span></a>
              <ul class="dropdown-menu" aria-labelledby="themes">
                <li><a href="#">All</a></li>
                <li class="divider"></li>
                <li><a href="#">Foo</a></li>
                <li><a href="#">Bar</a></li>
                <li><a href="#">Barbaz</a></li>
              </ul>
            </li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li><a href="${request.route_url('about')}" target="_blank">About</a></li>
          </ul>

        </div>
      </div>
    </div>


    <div class="container">
      ${caller.body()}
    </div>
    
    <div id="footer">
      <div class="footer">
        <p class="text-muted">Copyright 2014 <a href="/">Domidoo</a></p>
      </div>
    </div>

</div>
<script src="/static/js/jquery-1.10.2.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<script src="/static/js/bootswatch.js"></script>
  % if hasattr(caller, 'scripts'):
      ${caller.scripts()}
  % endif
</body>
</html>
</%def>
