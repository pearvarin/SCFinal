	// Connect to the database
	include getcwd()."/libs/layout.php";
	
	$user_id = $_SESSION['user_id'];
	
	//get the email to display
	$sql = "SELECT u.email
		FROM Users2 u
		WHERE u.user_id = ".$user_id." ";
	$result =  odbc_exec($connection, $sql);
	$row =  odbc_fetch_array($result);
	$email = $row['email'];
	
	//get the game_id to load various pages depending on existance
	if(!is_null($_POST['Game_id']))
	{
		$_SESSION['game_id']=NULL;	
		$game_id = $_POST['Game_id'];
		if($game_id==0)
		{
			$game_id=NULL;
		}
		$_SESSION['game_id']=$game_id;	
	}
	else 
	{
		$game_id = $_SESSION['game_id'];
	}
		
	
	if (!is_null($game_id))
	{
		//fix data retrival for number suppliers and buyers draw scheme to make it work
		$gamestate_sql = "SELECT * FROM Game_State WHERE game_id = $game_id";
		$gamestate_result =  odbc_exec($connection, $gamestate_sql);
		$gamestate =  odbc_fetch_array($gamestate_result);
		
		if($gamestate['current_period']>-1)
		{
			header('Refresh: 10');
		}
		
		$gamesettings_sql = "SELECT game_id, num_suppliers, num_buyers, num_periods, exp_smooth_coeff, lead_time FROM Game_Settings WHERE game_id = $game_id";
		$gamesettings_result =  odbc_exec($connection, $gamesettings_sql);
		$gamesettings =  odbc_fetch_array($gamesettings_result);
		
		$supplier_sql = "SELECT * FROM Supplier_Settings s, Users_Link ul, Users2 u 
		WHERE ul.game_id = $game_id
		AND ul.link_id = s.link_id
		AND u.user_id = ul.user_id
		AND u.type = 2";
		$supplier_result =  odbc_exec($connection, $supplier_sql);
		while ($row =  odbc_fetch_array($supplier_result))
			$suppliersettings[$row['supplier_num']] = $row;
	
		$buyer_sql = "SELECT * FROM Buyer_Settings s, Users_Link ul, Users2 u 
		WHERE ul.game_id = $game_id
		AND ul.link_id = s.link_id
		AND u.user_id = ul.user_id
		AND u.type = 1";
		$buyer_result =  odbc_exec($connection, $buyer_sql);
		while ($row =  odbc_fetch_array($buyer_result))
			$buyersettings[$row['buyer_num']] = $row;
			
		$buyer_list_sql = "SELECT user_id, email FROM Users2 WHERE Users2.type = 1 ORDER BY email";
		
		//echo $buyer_list_sql;
		$buyer_list_result =  odbc_exec($connection, $buyer_list_sql);
		//$buyerlist = new array();
		while($row =  odbc_fetch_array($buyer_list_result))
			$buyerlist[]=$row;
			
		$supplier_list_sql = "SELECT user_id, email FROM Users2 WHERE Users2.type = 2 ORDER BY email";
		$supplier_list_result =  odbc_exec($connection, $supplier_list_sql);
		while($row =  odbc_fetch_array($supplier_list_result))
			$supplierlist[]=$row;