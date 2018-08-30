from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta
import numpy as np
from models import *
from collections import deque
from operator import add
from math import *


def input():  # feed from inputs
	procurement_cost = 1.0
	holding_cost = 0.15
	backlog_cost = 0.45
	selling_price = 2.0
	s_procurement_cost = 0.5
	s_holding_cost = 0.05
	s_backlog_cost = 0.15
	s_selling_price = 1.0
	supplier_finished_good_inventory = 454
	supplier_work_in_progress_inventory = deque([390, 390, 390])
	supplier_backlog = [0, 0]
	total_supplier_profit = 0

def calibrate2(b, s, j): #b = no of buyers, s = no of suppliers
	for i in [1,b]:
		totals_buyer.append([0]*14)
	for i in [1,s]:
		totals_supplier.append([0]*12)

def calibrate(b1, b2, j):  # change for more buyers
	totals_buyer1 = [0] * 14
	totals_buyer2 = [0] * 14
	totals_supplier = [0] * 12
	consumer_demand = [(200, 40, np.random.RandomState(j)),
	                   (200, 40, np.random.RandomState(np.random.RandomState(j).randint(10)))]
	buyer_orders = [b1, b2]
	buyer_inventory = [0, 0]
	buyer_backlog = [0, 0]
	buyer_total_cost = [0, 0]
	buyer_total_profit = [0, 0]
	past_sales = [0, 0]


def get_demand(buyer):
	mean, std, rng = buyer
	x = rng.normal(mean, std)
	while x < 0:
	    x = rng.normal(mean, std)
	return(x)


def uniform_allocation(supplier_capacity, order_amounts):  # order_amounts = list
	total_order_amount = sum(order_amounts)
	if total_order_amount <= supplier_capacity:
	  return(supplier_capacity - total_order_amount, [allocated for allocated in order_amounts])

	x = supplier_capacity / float(len(order_amounts))
	output_amounts = [x for i in order_amounts]
	while True:
		remaining_amount = 0.0
		not_fullfilled = 0
		for i in xrange(len(output_amounts)):
			if output_amounts[i] > order_amounts[i]:
				remaining_amount = output_amounts[i] - order_amounts[i]
				output_amounts[i] = order_amounts[i]
		else:
		    not_fullfilled += 1
		if remaining_amount == 0.0:
		  	break
		x = remaining_amount / float(not_fullfilled)
		for i in xrange(len(output_amounts)):
			if output_amounts[i] < order_amounts[i]:
				output_amounts[i] += x
	return(0.0, output_amounts)


def proportional_allocation(supplier_capacity, order_amounts):
	total_order_amount = sum(order_amounts)
	if total_order_amount <= supplier_capacity:
		return(supplier_capacity - total_order_amount, [allocated for allocated in order_amounts])

	output_amounts = [0 for i in order_amounts]
	for i in xrange(len(output_amounts)):
		order_ratio = (float(order_amounts[i])/total_order_amount) * supplier_capacity
		output_amounts[i] = min(order_amounts[i], order_ratio)
	return(0.0, output_amounts)


def turn_and_earn_allocation(supplier_capacity, past_sales, order_amounts):
	total_order_amount = sum(order_amounts)
	if total_order_amount <= supplier_capacity:
		return(supplier_capacity - total_order_amount, [allocated for allocated in order_amounts])

	output_amounts = [0 for i in order_amounts]

	sales_diff = abs(past_sales[0] - past_sales[1])

	remaining_diff = [0, 0]
	remaining_diff[0] = max(0, supplier_capacity - order_amounts[1])
	remaining_diff[1] = max(0, supplier_capacity - order_amounts[0])

	for i in xrange(len(order_amounts)):
		if past_sales[i] == max(past_sales):  # leader
			# guaranteed allocation
			leader_guaranteed = sales_diff + (float(supplier_capacity) - sales_diff) / 2
			output_amounts[i] = min(
			    order_amounts[i], (leader_guaranteed + remaining_diff[i]))
		else :  #laggard
		  	laggard_guaranteed =  (float(supplier_capacity) - sales_diff)/2
		  	output_amounts[i] = min(order_amounts[i],laggard_guaranteed + remaining_diff[i])  
	return(0.0, output_amounts)

def run(b1, b2, T, j, allocation_policy):
	calibrate(b1, b2, j)
	input()
	for t in xrange(T):
		last_period_supplier_backlog = supplier_backlog # backlog for buyers
		inventory_level = supplier_finished_good_inventory - sum(supplier_backlog)
		inventory_position = inventory_level + sum(supplier_work_in_progress_inventory)
		production_level = 1572 - (inventory_position - sum(buyer_orders))  
		if production_level < 0:
			production_level = 0
		elif production_level > 1000:
			production_level = 1000

		if allocation_policy == 'u':
			supplier_finished_good_inventory, buyer_backlog_allocated = uniform_allocation(supplier_finished_good_inventory,supplier_backlog)
			supplier_finished_good_inventory, buyer_order_allocated = uniform_allocation(supplier_finished_good_inventory,buyer_orders)
		elif allocation_policy == 'p':
			supplier_finished_good_inventory, buyer_backlog_allocated = proportional_allocation(supplier_finished_good_inventory,supplier_backlog)
			supplier_finished_good_inventory, buyer_order_allocated = proportional_allocation(supplier_finished_good_inventory,buyer_orders)
		elif allocation_policy == 't':
			supplier_finished_good_inventory, buyer_backlog_allocated = turn_and_earn_allocation(supplier_finished_good_inventory,past_sales,supplier_backlog)
			supplier_finished_good_inventory, buyer_order_allocated = turn_and_earn_allocation(supplier_finished_good_inventory,past_sales,buyer_orders)   
		else:
			assert False
  
		temp_foi = supplier_finished_good_inventory

		supplier_backlog = [supplier_backlog[i] - buyer_backlog_allocated[i] for i in xrange(len(supplier_backlog))]

		for i in xrange(len(supplier_backlog)) :
			if buyer_orders[i] > buyer_order_allocated[i] :     
				supplier_backlog[i] += buyer_orders[i] - buyer_order_allocated[i] 

		buyer_allocated = [buyer_backlog_allocated[i] + buyer_order_allocated[i] for i in xrange(len(buyer_backlog_allocated))]
	  
		supplier_finished_good_inventory += supplier_work_in_progress_inventory.popleft()

		supplier_work_in_progress_inventory.append(production_level)

		buyer_costs = [0,0]
		buyers_profit = [0,0]
		demands = [0,0]
		service_level = [0,0]
		sold = [0,0]
		HC = [0,0]
		BC = [0,0]
		PC = [0,0]
		buyers_revenue = [0,0]
		buyer_log = [0,0]
		supplier_fill_rate = [0,0]
	  
		for i in xrange(len(buyer_costs)):
			demands[i] = round(get_demand(consumer_demand[i]))
			max_sold = buyer_backlog[i] + demands[i]       
			buyer_inventory[i] += buyer_allocated[i] - buyer_backlog[i] - demands[i]
			if buyer_inventory[i] >= 0:
			    buyer_backlog[i] = 0
			else:
			    buyer_backlog[i] = -buyer_inventory[i] 
			    buyer_inventory[i] = 0
			sold[i] = max_sold - buyer_backlog[i]
			past_sales[i] = sold[i]
			buyer_costs[i] = procurement_cost * buyer_allocated[i] + holding_cost * buyer_inventory[i] + backlog_cost * buyer_backlog[i]  
			buyers_profit[i] = selling_price * sold[i] - buyer_costs[i]
			buyer_total_cost[i] +=   buyer_costs[i]
			buyer_total_profit[i] += buyers_profit[i]
			service_level[i] = 1 - (float(buyer_backlog[i])/float(demands[i])) 

			HC[i] = holding_cost * buyer_inventory[i]
			BC[i] = backlog_cost * buyer_backlog[i]
			PC[i] = procurement_cost * buyer_allocated[i]

			buyers_revenue[i] = selling_price * sold[i]

			temp_backlog = last_period_supplier_backlog[i] + buyer_orders[i] - buyer_allocated[i]
			supplier_fill_rate[i] = 1 - (float(max(temp_backlog,0))/ float(buyer_orders[i]))

		out_logs = [[], []]

		for i in range(len(buyer_costs)):
			temp_log = [t+1,
				buyers_profit[i],
				buyer_inventory[i],
				buyer_backlog[i],
				service_level[i],
				demands[i],
				sold[i],
				buyer_orders[i],
				buyer_allocated[i],
				supplier_fill_rate[i],
				HC[i],
				BC[i],
				PC[i],
				buyers_revenue[i] ]
			out_log = []
			for x in temp_log:
			  	if isinstance(x, float):
			  		out_log.append('%.2f' % x)
			  	else:
			  		out_log.append(str(x))
			out_logs[i] = out_log
			buyer_log[i] = temp_log 
  
		temp_supplier_backlog = sum(last_period_supplier_backlog) + sum(buyer_orders) - sum(buyer_allocated)

		fr_supplier =   1 - (float(max(temp_supplier_backlog,0))/ float(sum(buyer_orders)))  

		supplier_hc = s_holding_cost * temp_foi 
		supplier_bc = s_backlog_cost * sum(supplier_backlog)
		supplier_pc = s_procurement_cost * production_level
		supplier_revenue = s_selling_price * sum(buyer_allocated)
		supplier_cost =  supplier_hc + supplier_bc + supplier_pc
		supplier_profit =  supplier_revenue - supplier_cost

		total_supplier_profit += supplier_profit

		supplier_log = [t+1,fr_supplier,temp_foi,sum(supplier_backlog),supplier_profit,sum(buyer_orders),
		sum(buyer_allocated),production_level,supplier_hc,supplier_pc,supplier_bc,supplier_revenue]
		        
		totals_supplier = map(add,totals_supplier,supplier_log)

		return(int(total_supplier_profit),int(sum(buyer_total_profit)), int(buyer_total_profit[0]),int(buyer_total_profit[1]),int(sum(buyer_total_profit)) + int(total_supplier_profit))
