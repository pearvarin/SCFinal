
					<td align="center" colspan='5'>Supplier Performance</td>




					<td align="center" colspan='6'>Buyer Performance</td>
				</tr>
				<tr>
					<td align="center" width="80">Period</td>
					<td align="center" width="80">Order</td>
					<td align="center" width="80">Received Shipment</td>
					<td align="center" width="80">On Order</td>
					<td align="center" width="80">Supplier Fill Rate</td>	
					
					<td align="center" width="80">&nbsp</td>
					
					<td align="center" width="80">Demand</td>
					<td align="center" width="80">Sales</td>
					<td align="center" width="80">Inventory</td>
					<td align="center" width="80">Backlog</td>
					<td align="center" width="80">Service Level</td>	
					<td align="center" width="80">Profit</td>				
				</tr>

					user_id
					game_id


					//Load data

					user_result = 
					sql= "SELECT u.user_id, u.email, ul.user_id, ul.link_id \
					FROM Users2 u, Users_Link ul \
					WHERE u.user_id = user_id \
					AND ul.user_id = user_id\
					AND ul.game_id = game_id"

					usertable =  odbc_fetch_array(user_result(sql))
					link_id = usertable['link_id']
					
					suppliers_sql = "SELECT ul.link_id, ul.user_id, ul.game_id, u.type, u.user_id\
					FROM Users_Link ul, Users2 u\
					WHERE ul.game_id = game_id\
					AND u.user_id = ul.user_id\
					AND u.type = 2"
					suppliers_result =  odbc_exec(connection, suppliers_sql)
					while row <  odbc_fetch_array(suppliers_result):
						suppliers[] = row['link_id']
					
					gamestate = "SELECT * FROM Game_State WHERE game_id = game_id"
					current_period = gamestate['current_period']
					
					gamesettings_sql = "SELECT * FROM Game_Settings WHERE game_id = game_id"
					num_buyers = gamesettings['num_buyers']
					lead_time = gamesettings['lead_time']

					result = "SELECT * FROM Buyer_Data WHERE link_id = link_id"

					tot_profit = 0
					tot_demand = 0
					tot_order = 0
					tot_receive = 0
					tot_ship = 0
					tot_stock = 0
					tot_backlog = 0
					tot_onorder = 0
					whilerow < odbc_fetch_array(result)""
						if row['period_id'] < current_period && row['period_id'] > 0:
			
							period_id = row['period_id']
							receive_result = "SELECT shipment, period_id, fill_rate, on_order FROM Joint_Data WHERE buyer_id = link_id\
							AND supplier_id = suppliers[0] \
							AND period_id = period_id"
							line =  odbc_fetch_array(receive_result)
							receive = line['shipment']
							on_order = line['on_order']
							fill_rate[row['period_id']] = line['fill_rate']
							s_lvl[row['period_id']] = row['service_level']

						#send it via json to front end
							row[profit]>0 
						['period_id', 'total_order', receive, on_order, (100*fill_rate[row['period_id']])]
						[demand, sales, inventory, backlog, (100*s_lvl[row['period_id']]), profit]

							tot_onorder += on_order
							tot_profit += row['profit']
							tot_demand += row['demand']
							tot_receive += receive
							tot_order += row['total_order']
							tot_ship += row['sales']
							tot_stock += row['inventory']
							tot_backlog += row['backlog']			

					tot_service = max(0,(1-(tot_backlog/tot_demand)))
					tot_fill_rate = max(0,(1-(tot_onorder/tot_order)))

					 tot_profit > 0 :
					 total:
					 [tot_order, tot_Receive, tot_onorder, round(100*tot_fill_rate,1)]
					 [tot_demand, tot_ship, tot_stock, tot_backlog, round(100*tot_service,1), tot_profit]
