<%def name="layout()">
<html xmlns="http://www.w3.org/1999/xhtml">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
  <head>	
     <title>
         ${caller.title()}
     </title>
  </head>
  <body>
    <ul>	
      <li>
    	<a href="${request.route_url("home")}">Home</a>    
      </li>
    </ul>
    <div class="mainlayout">
        <div class="content">
            ${caller.body()}
        </div>
	<div>
  </body>
</%def>
