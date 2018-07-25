<template>
	<h>Financials</h>
	<table align="center" cellspacing="0" cellpadding="0" border="1" bgcolor="#FFFFFF">
		<tr>
			<td align="center" colspan='5'>Supplier Performance</td>
			<td align="center" width="80"></td>
			<td align="center" colspan='6'>Buyer Performance</td>
		</tr>
		<tr>
			<td align="center" width="80">Period</td>
			<td align="center" width="80">Order</td>
			<td align="center" width="80">Received Shipment</td>
			<td align="center" width="80">On Order</td>
			<td align="center" width="80">Supplier Fill Rate</td>	
			
			<td align="center" width="80">&nbsp;</td>
			
			<td align="center" width="80">Demand</td>
			<td align="center" width="80">Sales</td>
			<td align="center" width="80">Inventory</td>
			<td align="center" width="80">Backlog</td>
			<td align="center" width="80">Service Level</td>	
			<td align="center" width="80">Profit</td>				
		</tr>
		while, if{
		<tr>
			<td align="center" width="200">{{row['period_id']}}</td>
			<td align="center" width="200">{{row['total_order']}}</td>
			<td align="center" width="200">{{receive}}</td>
			<td align="center" width="200">{{on_order}}</td>
			<td align="center" width="200">{{round(100*fill_rate[row['period_id']],1)}}%</td>	
			<td align="center" width="200"></td>	
			
			<td align="center" width="200">{{row['demand']}}</td> 
			<td align="center" width="200">{{row['sales']}}</td>
			<td align="center" width="200">{{row['inventory']}}</td>
			<td align="center" width="200">{{row['backlog']}}</td>
			<td align="center" width="200">{{round(100*s_lvl[row['period_id']], 1)}}%</td>
			<td align="center" width="200">{{row['profit']}}</td>
		</tr>
		}					

					<tr></tr><tr class='total'>
					<td align="center" width="200">Total</td>
					<td align="center" width="200">{{tot_order}}</td>
					<td align="center" width="200">{{tot_receive}}</td> 
					<td align="center" width="200">{{tot_onorder}}</td>
					<td align="center" width="200">{{round(100*tot_fill_rate,1)}}%</td>
					<td align="center" width="200"></td>
					<td align="center" width="200">{{tot_demand}}</td>
					<td align="center" width="200">{{tot_ship}}</td>
					<td align="center" width="200">{{tot_stock}}</td>	
					<td align="center" width="200">{{tot_backlog}}</td>
					<td align="center" width="200">".round(100*tot_service,1)}}%</td>		
					<td align="center" width="200" $class>${{tot_profit}}</td>
					</tr>
			</table>
</template>