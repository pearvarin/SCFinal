<!-- 	/* s_game.php:
		It controls all the transaction information that made by the supplier. It transmits the collected informaition to 
		"insert_supplier.php" page to store in the database, and display the information from "buyer_data.php", "sup_inv_assign.php", and session values on the screen. -->
<!-- 		==========================================>===========
<link type="text/css" href="resources/css/cupertino/jquery-ui-1.8.custom.css" rel="stylesheet" id="pageStyle"/>
<link type="text/css" href="resources/css/jquery-ui-layout.css" rel="stylesheet" />
<link type="text/css" href="resources/css/controls/ui.accordion.css" rel="stylesheet" />
<link type="text/css" href="resources/css/tableshow/muffin.css" rel="stylesheet" />
<link type="text/css" href="resources/css/ccd.css" rel="stylesheet" />
=====================================================
<link type="text/css" rel="stylesheet" href="resources/css/stylechat.css" />
 -->
	
<template>
	<div class ="container">
		<table align="center" width=1032 cellspacing="0" cellpadding="0" border="1" bgcolor="#FFFFFF">
			<tr>
				<!-- Title -->
				<td colspan="6">					
					<h2>Game Master Page</h2>				
				</td>
			</tr>
			<tr>
				<!-- Display the current player's information (ID, playing type, and Email) -->
				<td colspan="3" align="center" height="90px">
					<p><b>Player's Information:</b></p>
					<table>
						<tr>
							<td align="right">ID: </td>
							<td name="id">
								<!-- {{user_id}} -->
							</td>
							<td align="right">Playing Type: </td><td align="left">Game Master</td>
						</tr>
						<tr>
							<td align="right">Email: </td>
							<td>
								<!-- {{email}} -->
							</td>
							<td align="right">Game ID: </td>
							<td>
								<!-- {{game_id}} -->
							</td>
						</tr>
						<tr>
							<td colspan="2" align="center">
							<form name="back_game" method="post" action="gm_game_manager.php">
								<button class='btn' type='submit' onClick='unsetgame()' style='height: 30px; width: 111px'><b>Back</b></button>
							</form>
							</td>
							<td colspan="2" align="center">
							<form name="end_game" method="post" action="gm_end_game.php">
								<button class='btn' type='submit' onClick='unsetgame()' style='height: 30px; width: 111px'><b>End Game</b></button>
							</form>
							</td>	
						</tr>
					</table>
				</td>
				
			</tr>			

				
			<!-- 
			<?php
			//CREATE GAME 
			//This section assigns the number of buyers and suppliers and creates a game 
			if(is_null($game_id))
			{
				?>	 -->				
				<td align="center">
					<form name="create_game" method="post" action="create_game.php">
					<!-- Define number of players -->
						<table>					
							<tr>
								<td><b>Number of Suppliers: </b></td>
								<td><input type=text size=8 maxlength=20 class=m_box name="num_suppliers" value='1'></td>
							</tr>
							<tr>
								<td><b>Number of Buyers: </b></td>
								<td><input type=text size=8 maxlength=20 class=m_box name="num_buyers" value='2'></td>
								
							</tr>
						</table>								
						<p></p>
						<button class='btn' type='submit' style='height: 30px; width: 111px'><b>Create Game</b></button>		
					</form>
				</td>	
				
		
				<!-- POPUPS TO BE FIXED  -->			
				<td align="center" height="60px">
					<table>
						<tr>
							<td><button class="btn" onClick="output()" style="height: 30px; width: 111px">Output</button></td>
							<td><button class="btn" onClick="graph()" style="height: 30px; width: 111px">Graph</button></td>
							<td><button class="btn" style="height: 30px; width: 111px" name="cancel" value="cancel" onClick="financial()">Financials</button></td>
							<td><button class="btn" style="height: 30px; width: 111px" name="submit" value="submit" onClick="parameter()">Parameters</button></td>
						</tr>
					</table>
				</td>
			</tr>			
		</table>
		<p></p>		
		<form name=settings method=post action='start_game.php'>
			<table align='center' width='1032' cellspacing='0' cellpadding='0' border='1' bgcolor='#FFFFFF'>
				<tr>
					<td>
						<table>
							<tr>
								<td>Periods</td>
								<td>
					<!-- input_g("num_periods", $gamesettings['num_periods'], $gamestate['current_period'], -1, 30); -->

												</td>
												<td>Lead Time</td>
												<td>

<!-- 					input_g("lead_time", $gamesettings['lead_time'], $gamestate['current_period'], -1, 4)
 -->
												</td>
												<td>Exponential Smoothing Coefficient</td>
												<td>
				<!-- 	input_g("exp_smooth_coeff", round($gamesettings['exp_smooth_coeff'], 2), $gamestate['current_period'], -1, .3) -->
		
												</td>
												<td>Current Period</td>
												<td>
<!-- 						";
					echo($gamestate['current_period']);
					echo " -->
												</td>
												<td>Buyers Submitted</td>
												<td>
<!-- 						";
					if($gamestate['buyers_submitted']==0)
						echo "No";
					else if($gamestate['buyers_submitted']==1)
						echo "Yes";	
					echo " -->
												</td>
												<td>Suppliers Submitted</td>
												<td>
<!-- 						";
					if($gamestate['suppliers_submitted']==0)
						echo "No";
					else if($gamestate['suppliers_submitted']==1)
						echo "Yes";	
					echo " -->
												</td>
											</tr>
										</table>
									</td>
								</tr>								
							</table>							
							<p></p>										
							<table align='center' width=1032 cellspacing='0' cellpadding='0' border='1' bgcolor='#FFFFFF'>
								<tr>
									<td align='center' valign='top'>				
<!-- 						";
		 			for($i = 1; $i <= $gamesettings['num_suppliers']; $i++)
					{
						if ($i > 1)
							echo "<p></p>";
						echo " -->
										<table>
											<tr>
												<td colspan=2 align='center'><h3>Supplier </h3></td> <!--".$i."-->
											</tr>
											<tr>
												<td>Player account: </td>
												<td>
<!-- 							";
						if ($gamestate['current_period'] > -1)
							echo $suppliersettings[$i]['email'];
						else
						{
							$numavail = count($supplierlist); -->
							
							<!-- echo "<select name=s_user_id_".$i.">";
							for ($a=0; $a < $numavail ; $a++) 
								{ 
									echo"<option value='".$supplierlist[$a]["user_id"]."'>".$supplierlist[$a]['email']."</option>";
								}
						
							echo"</select>";
						}	
						echo " -->
								<tr>
									<td>Automation: </td>
									<td>
							<!-- ";
						if ($gamestate['current_period'] > -1)
						{
							if($suppliersettings[$i]['automation']==0)
								echo "User Controlled";
							if($suppliersettings[$i]['automation']==1)
								echo "Automated";
						}
						else
						{
							echo "<select name=s_automation_".$i.">
							<option value='0'>No - User Controlled</option>
							<option value='1'>Yes - Automated</option>
							</select>";
						}
							
												
						echo "	 -->			
												</td>					
											</tr>
												<td>Production cost: </td>
												<td>
<!-- 							";
						input_g("s_Prod_cost_".$i, $suppliersettings[$i]['production_cost'], $gamestate['current_period'], -1, 50);								
						echo " -->				
												</td>					
											</tr>
			
											<tr>
												<td>Holding cost: </td>
												<td>
<!-- 							";
						input_g("s_Hold_cost_".$i, $suppliersettings[$i]['holding_cost'], $gamestate['current_period'], -1, 10);								
						echo "			 -->	
												</td>					
											</tr>
											<tr>
												<td>Wholesale price: </td>
												<td>
<!-- 							";	
						input_g("s_Whole_price_".$i, $suppliersettings[$i]['wholesale_price'], $gamestate['current_period'], -1, 100);								
						echo " -->				
												</td>					
											</tr>
											<tr>
												<td>Allocation Rule: </td>
												<td>
<!-- 							";
						if ($gamestate['current_period'] > -1)
						{
							switch($suppliersettings[$i]['alloc_rule'])
							{
								case 0:
									echo "Manual";
									break;
								case 1:
									echo "Proportional";
									break;
								case 2:
									echo "Uniform";
									break;
								case 3:
									echo "Forecast Accuracy";
									break;						
							}
						}
						else
						{
							echo " -->
								<select name=s_Alloc_rule_".$i.">
									<option value='0'>Manual</option>
									<option value='1'>Proportional</option>
									<option value='2'>Uniform</option>
									<option value='3'>Forecast Accuracy</option>
								</select>
<!-- 							";
						}
						echo "	 -->			
												</td>					
											</tr>
											<tr>
												<td>Production Strategy: </td>
												<td>
						<!-- 	";
						if ($gamestate['current_period'] > -1)
						{
							switch($suppliersettings[$i]['prod_strat'])
							{
								case 0:
									echo "Low";
									break;
								case 1:
									echo "Medium";
									break;
								case 2:
									echo "High";
									break;					
							}
						}
						else
						{
							echo " -->
								<select name=s_Prod_strat_".$i.">
									<option value='0'>Low</option>
									<option value='1'>Medium</option>
									<option value='2'>High</option>
								</select>
							<!-- ";
						}
						echo "				 -->
												</td>					
											</tr>
										</table>									
<!-- 							";
					}
					
					
					
					echo " -->
				</td>
<!-- 					//Begin buyer settings sections		 -->
					<td align='center' valign='top'>	
					<!-- for($i = 1; $i <= $gamesettings['num_buyers']; $i++)
					{
						if ($i > 1)
							echo "<p></p>";
						echo "	 -->						
										<table>
											<tr>
												<td colspan=2 align='center'><h3>Buyer $i</h3></td>
											</tr>
											<tr>
												<td>Player account: </td>
												<td>
						<!-- 	";
						if ($gamestate['current_period'] > -1)
							echo $buyersettings[$i]['email'];
						else
						{
							$numavail = count($buyerlist);
							echo "<select name=b_user_id_".$i.">";
							for ($a=0; $a < $numavail ; $a++) 
								{ 
									echo"<option value='".$buyerlist[$a]["user_id"]."'>".$buyerlist[$a]['email']."</option>";
								}
							echo"</select>";
						}
						echo "	 -->			
												</td>					
											</tr>
											<tr>
												<td>Holding cost: </td>
												<td>
							<!-- ";	
						input_g("b_Hold_cost_".$i, $buyersettings[$i]['holding_cost'], $gamestate['current_period'], -1, 15);								
						echo "	 -->			
												</td>					
											</tr>
											<tr>
												<td>Backlog cost: </td>
												<td>
							<!-- ";
						input_g("b_Backlog_cost_".$i, $buyersettings[$i]['backlog_cost'], $gamestate['current_period'], -1, 45);								
						echo "		 -->		
												</td>					
											</tr>
											<tr>
												<td>Retail price: </td>
												<td>
							<!-- ";
						input_g("b_Retail_price_".$i, $buyersettings[$i]['retail_price'], $gamestate['current_period'], -1, 200);								
						echo "		 -->		
												</td>					
											</tr>
											<tr>
												<td>Demand mean: </td>
												<td>
				<!-- 			";
						input_g("b_Mean_".$i, $buyersettings[$i]['mean'], $gamestate['current_period'], -1, 200);								
						echo "		 -->		
												</td>					
											</tr>
											<tr>
												<td>Demand standard deviation: </td>
												<td>
			<!-- 				";
						input_g("b_Std_".$i, $buyersettings[$i]['s_dev'], $gamestate['current_period'], -1, 40);								
						echo "			 -->	
												</td>					
											</tr>						
								
					<tr><td>Buyer Distribution Generation</td>
												<td></td></tr>
											</table>

						<!-- ";
					if ($gamestate['current_period'] > -1)
						{
							//make sure to change database to write dist mode for each buyer
							switch($buyersettings[$i]['gen_rule'])
							{
								case 0:
									echo "From File";
									break;
								case 1:
									echo "Generated";
									break;					
							}
						}
						else
						{
							echo "
								<select name=b_gen_rule".$i.">
									<option value='0'>From File</option>
									<option value='1'>Generated</option>
								</select>
							";
						}
					echo "
					</tr> -->

											




<!-- 					
					}
if ($gamestate['current_period'] == -1)
						{				
					echo "
									</td>
								</tr>
							</table>
							<table align='center' width=1032 cellspacing='0' cellpadding='0' border='1' bgcolor='#FFFFFF'>
								<tr>
									<td align='right'>
										<button class='btn' style='height: 35px; width: 180px' name='submit' value='submit' type='submit'><b>Start Game</b></button>
									</td>
								</tr>
							</table>	</form>										
