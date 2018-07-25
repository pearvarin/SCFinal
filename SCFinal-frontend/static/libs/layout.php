<?php
	include getcwd()."\dbconn.php";
	include getcwd()."\library_new.php";
	include getcwd()."\library.php";
	
	if($_GET["logout"] == "true")
		session_destroy();
		
	function gen_head($title = null){
?>
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="x-ua-compatible" content="IE=9">
		<title><?php echo $title ? $title : "Interactive Supply Chain Game (Ver. 2.0 Beta)"; ?></title>
		<link rel="stylesheet" type="text/css" href="css/main.css" />
		<script type="text/javascript" src="resources/js/jquery-1.4.2.js"></script>
		<script type="text/javascript" src="resources/js/jquery-ui.js"></script>
		<script type="text/javascript" src="resources/js/jquery.layout-1.3.0.rc28.js"></script>

	</head>

	<body>
	<div id="main-container">
<?php
	if($_GET["logout"] == "true")
	{
		?>
		<div class="alert alert-block alert-success">
			<p>You have successfully logged out!</p>
		</div>
		<?php
	}
}

function gen_foot(){
?>
		</div>
	</body>
</html>
<?php
}
?>