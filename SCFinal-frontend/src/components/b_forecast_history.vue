<template>
		<table align="center" cellspacing="0" cellpadding="0" border="1" bgcolor="#FFFFFF">
	
			<tr> 
			<td align='center' width='300' colspan='".({{lead_time}}-1)."'>{{supplier_label}}.{{supplier_name}}</td>	
			<td align='center' width='300' colspan='4'>Exp Smoothed Total Forecast Accuracy: ".round(100*({{accuracy}}), 2)."% </td>	
			</tr>
			<tr> 
			<td align='center' width='100'>Period</td>	
<!-- {# 			for ($y=1; $y <=$lead_time ; $y++) 
			{  #} -->
				<td align='center' width='100'>Forecast ".({{y}})."</td>
			{# } #}
			<td align='center' width='100'>Order Amount</td>	
			<td align='center' width='100'>Forecast Acc</td>	
			</tr>
<!-- 
			for ($i=1; $i <= $current_period+$lead_time; $i++) 
			{
				if($i<$lead_time)
				{ -->
					<tr> 
					<td align='center' width='100'>".($i)."</td>
					
<!-- 					$forecast_sql = "SELECT * FROM Forecast_Data WHERE buyer_id = $link_id 
					AND supplier_id = $supplier_id
					AND period_id = $i
					$forecast_result = odbc_exec($connection, $forecast_sql);
					while ($row = odbc_fetch_array($forecast_result))
					{ -->
						<td align='center' width='100'>".($row['forecast_value'])."</td>
<!-- 					}
					
					for ($z=0; $z < ($lead_time-$i); $z++) 
					{  -->
						<td align='center' width='100'>N/A</td>
<!-- 					}		

				}
				else
				{   -->
					<tr> 
					<td align='center' width='100'>".($i)."</td>
<!-- 					
					$forecast_sql = "SELECT * FROM Forecast_Data WHERE buyer_id = $link_id 
					AND supplier_id = $supplier_id
					AND period_id = $i
					$forecast_result = odbc_exec($connection, $forecast_sql);
					while ($row = odbc_fetch_array($forecast_result))
					{
						if($row['forecast_value']!=-1) -->
							<td align='center' width='100'>".($row['forecast_value'])."</td>
<!-- 						else -->
							<td align='center' width='100'>-</td>		
<!-- 					}
				
				}
				$acc_sql = "SELECT * FROM Joint_Data WHERE buyer_id = $link_id 
				AND supplier_id = $supplier_id
				AND period_id = $i
				$acc_result = odbc_exec($connection, $acc_sql);
				$row = odbc_fetch_array($acc_result);
				if($i <= $current_period)
				{ -->
					<td align='center' width='100'>".$row['order_amount']."</td>
					<td align='center' width='100'>".round(100*($row['forecast_acc']), 2)." %</td></tr>
<!-- 				}
								
			}
			
		}
		?>	 -->

		</table>
</template>