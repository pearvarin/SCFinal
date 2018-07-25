<template>
	<div class= "container">
	<h1>Welcome! The record shows us that you are a General Manager.</h1>
	<h2>What would you like to do today></h2>

		<!-- Title of Patient Webpage===================================================== -->
		<!-- <title>Game Management Page</title>  -->
		<!-- ===================================================== -->
		<!-- <link type="text/css" href="resources/css/cupertino/jquery-ui-1.8.custom.css" rel="stylesheet" id="pageStyle"/> -->
		<!-- <link type="text/css" href="resources/css/jquery-ui-layout.css" rel="stylesheet" />
		<link type="text/css" href="resources/css/controls/ui.accordion.css" rel="stylesheet" />
		<link type="text/css" href="resources/css/tableshow/muffin.css" rel="stylesheet" />
		<link type="text/css" href="resources/css/ccd.css" rel="stylesheet" /> -->
		<!-- ===================================================== -->
		<!-- <link type="text/css" rel="stylesheet" href="resources/css/stylechat.css" /> -->
<!-- 
	<body bgcolor="#cccccc"> -->
		<table align="center" cellspacing="0" cellpadding="0" border="1" bgcolor="#FFFFFF">
			<tr>
				<!-- Title -->
				<td>					
					<h2>Game Management Page</h2>				
				</td>
			</tr>
			<tr>
				<!-- Display the current player's information (ID, playing type, and Email) -->
				<td>
				<table>
						<tr>
							<td align="right">ID: </td>
							<td name="id">ID <!--{{user_id}}-->
							</td>
							<td align="right">Playing Type: </td><td align="left">Game Master</td>
						</tr>
						<tr>
							<td align="right">Email: </td>
							<td>
								<!-- {{email}} -->
							</td>
							<td align="right">Privileges: </td>
							<td>
								Unrestricted
							</td>
						</tr>
					</table>
				</td>
				
				</tr>			
				<tr>
					<td><p><b>Please Choose an Active Game or Create a New One: </b></p></td>
				</tr>
				<tr>
				<td>
 
<!-- 				//let's create a select for each game that the game master is currently managing 
				//we need 1. the game_id, 
				//2. the emails of every participating player (you know, so the GM knows which game it is) -->
<!-- 				if($numgames!=0)
				{ -->
				<form name='select_game' method='post' action='gm_game.php'>
					<select name='Game_id'>
			  	<option value='0'>Create New Game</option>
				<!-- for ($a=0; $a < $numgames ; $a++) 
					{
						$emailsql = "SELECT u.email, ul.game_id FROM Users_Link ul, Users2 u 
						WHERE u.user_id = ul.user_id AND ul.game_id = ".($gamelist[$a])."";
						$emailresult =  odbc_exec($connection, $emailsql);
						while($row =  odbc_fetch_array($emailresult))
							$emails[$a][] = $row['email'];
						
						$emailstring = "Active Users: ";
						for ($i=0; $i < count($emails[$a]) ; $i++) 
						{ 
							$emailstring = $emailstring.$emails[$a][$i]." ";
						} -->
					<option value ="1">Pick other games</option>
				<!-- <option value=".$gamelist[$a].".{{emailstring}}>.</option> -->
				</select>
				<button type='submit' style='height: 30px; width: 111px'><b>Advance</b></button>
				</form>
<!-- 				}
				else if($numgames==0)
				{
					$_SESSION['game_id']=NULL;
					header("Location: ./gm_game.php");	
				}
				?>		 -->
				</td>
				</tr>	
		</table>
	</div>

</template>

<script>
	</script>

<style>
</style>