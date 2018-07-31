class GraphView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    Type=['Profit', 'ServiceLevel']

    def draw(self, chart, data, current_period, chartType):
        period = 1
        while period < current_period:
            chartData.append(data[period][chartType])
            period+=1

        chartData = GoogleChartData(chartData)

    def googleChart(self, chartData):

        chart_data = new GoogleChartData(chartData)
        chart->addData(chart_data)

    def drawProfit(self, chart, data, current_period):
        period = 1
        while period < current_period:
            profit_data.append(data[period]['profit'])
            period += 1

        profit_data = new GoogleChartData(profit_data)
        chart->addData(profit_data)

        # add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker: : CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setData(profit_data)
        chart->addMarker(shape_marker)

        # add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker: : VALUE)
        value_marker->setData(profit_data)
        chart->addMarker(value_marker)

        return(chart)


    def drawServiceLevel(self, chart, data, current_period):
        period = 1
        while period < current_period:
            service_data.append(data[period]['service_level'] * 100)
            period += 1

        service_data = new GoogleChartData(service_data)
        chart->addData(service_data)

        # add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker: : CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setData(service_data)
        chart->addMarker(shape_marker)

        # add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker: : VALUE)
        value_marker->setData(service_data)
        chart->addMarker(value_marker)
        return(chart)

    #Function to determine if the user checked a specified checkbox
    #Used for determining what to graph, what boxes to automatically check on a page submission, etc
    def IsChecked(self, chkname, value):
        if empty(_POST[chkname])=False:
            for i in _POST[chkname]:
                if i ==value:
                    return(True)
        return(False)

    #This def uses the Google Charts API to draw the data, it is
    #representative of all the other data out there as well
    def drawHoldingCost(self, chart, data, current_period, MIN, MAX, link_id, tConnection):
        global holding_cost_data
        user_result = "SELECT holding_cost FROM Buyer_Settings WHERE link_id = link_id"
        buyer_settings = odbc_fetch_array(user_result)  #grab first row
        holdingCost = buyer_settings['holding_cost']

        period = 1
        my_data = ""
        while period < current_period:
            my_data.append(data[period]['inventory'] * holdingCost)
            holding_cost_data.append(data[period]['inventory'] * holdingCost)
            period+=1
        
        my_data = new GoogleChartData(my_data)
        my_data->setColor('6699CC')
        my_data->setLegend('Holding Cost')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)

    def drawBacklogCost(self,chart, data, current_period, MIN, MAX, link_id, tConnection):

    def drawBacklog(self,chart, data, current_period, MIN, MAX, link_id, tConnection):

        global backlog_data
        
        period = 1
        my_data = ""
        while period < current_period:
            my_data.append(data[period]['backlog'])
            backlog_data.append(data[period]['backlog'])
            period+=1
        

        my_data = new GoogleChartData(my_data)
        my_data->setColor('CCCC66')
        my_data->setLegend('Backlog')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)
        
    def drawInventory(self, chart, data, current_period, MIN, MAX, tConnection):
        global inventory_data

        period = 1
        my_data = []
        while period < current_period:
            my_data[].append(data[period]['inventory'])
            inventory_data[].append(data[period]['inventory'])
            period+=1
        

        my_data = new GoogleChartData(my_data)
        my_data->setColor('CC9933')
        my_data->setLegend('Inventory')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return chart

    def drawProfit(self, chart, data, current_period, MIN, MAX, tConnection):
        #CALCULATING PROFIT"
        global profit_data
        
        period = 1
        my_data = ""
        while period < current_period:
            my_data.append(data[period]['profit'])
            profit_data.append(data[period]['profit'])
            period+=1

            #?

    def drawCumulativeProfit(self, chart, data, current_period, MIN, MAX, tConnection):

        global cumulative_profit_data

        period = 1
        total_profit = 0
        while period < current_period:
            total_profit = total_profit + data[period]['profit']
            my_data.append(total_profit)
            cumulative_profit_data.append(total_profit)
            period+=1

        my_data = new GoogleChartData(my_data)
        my_data->setColor('FFDFDF')
        my_data->setLegend('Cumulative Profit')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)
        
    def drawOrders(self, chart, data, current_period, MIN, MAX, tConnection):
    
        global orders_data
        
        period = 1
        my_data = []

        while period < current_period:
            my_data.append(data[period]['total_order'])
            profit_data.append(data[period]['total_order'])
            period+=1

        my_data = new GoogleChartData(my_data)
        my_data->setColor('33CC99')
        my_data->setLegend('Orders')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        returnchart)

    def drawReceivedShipment(self, chart, joint_data, current_period, MIN, MAX, tConnection):
    
        global received_shipments_data
        
        period = 1
        my_data = []

        while period < current_period:
            my_data.append(joint_data[period]['shipment'])
            received_shipments_data.append(joint_data[period]['shipment'])
            period+=1

        my_data = new GoogleChartData(my_data)
        my_data->setColor('66CCCC')
        my_data->setLegend('Received Shipment')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)    

    def drawRevenue(self, chart, buyerdata, current_period, MIN, MAX, link_id, tConnection):
        
        global revenue_data
        
        user_sql = "SELECT retail_price FROM Buyer_Settings WHERE link_id = link_id"
        user_result = odbc_exec(tConnection, user_sql)
        buyer_settings = odbc_fetch_array(user_result)  #grab first row
        retail_price = buyer_settings['retail_price']

        period = 1
        my_data = []

        while period < current_period:
            my_data.append(buyerdata[period]['sales'] * retail_price)
            revenue_data.append(buyerdata[period]['sales'] * retail_price)
            period+=1


        my_data = new GoogleChartData(my_data)
        my_data->setColor('999999')
        my_data->setLegend('Revenue')
        #my_data->setAutoscale(false)
        #my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)

    def drawSales(self, chart, buyerdata, current_period, MIN, MAX, tConnection):
    
        global sales_data
        
        period = 1
        my_data = []
        while period < current_period:
            my_data.append(buyerdata[period]['sales'])
            sales_data.append(buyerdata[period]['sales'])
            period+=1


        my_data = new GoogleChartData(my_data)
        my_data->setColor('006666')
        my_data->setLegend('Sales')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return chart

    def drawPurchaseCost(self, chart, data, jointdata, current_period, MIN, MAX, link_id, supplier_id, tConnection):

        global purchase_cost_data
        
        user_sql = "SELECT wholesale_price FROM Supplier_Settings WHERE link_id = supplier_id"
        user_result = odbc_exec(tConnection, user_sql)
        settings = odbc_fetch_array(user_result)  #grab first row
        wholesalePrice = settings['wholesale_price']

        period = 1
        my_data = ""
        while (period < current_period) {
            my_data[] = jointdata[period]['shipment'] * wholesalePrice
            purchase_cost_data[] = jointdata[period]['shipment'] * wholesalePrice
            #echo "Shipment = ", jointdata[period]['shipment'], "\n"
            period++
        }


        my_data = new GoogleChartData(my_data)
        my_data->setColor('0066CC')
        my_data->setLegend('Purchase Cost')
        my_data->setAutoscale(false)
        my_data->setScale(MIN, MAX)
        chart->addData(my_data)

        #add a shape marker with a border
        shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
        shape_marker->setSize(6)
        shape_marker->setBorder(2)
        shape_marker->setColor('000000')
        shape_marker->setData(my_data)
        chart->addMarker(shape_marker)

        #add a value marker
        value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
        value_marker->setColor('000000')
        value_marker->setData(my_data)
        chart->addMarker(value_marker)
        return(chart)

        def drawForecastAccuracy(self, chart, joint_data, current_period, MIN, MAX, tConnection):
        
            global forecast_accuracy_data
            
            period = 1
            my_data = ""
            while (period < current_period) {
                my_data[] = joint_data[period]['forecast_acc']
                forecast_accuracy_data[] = joint_data[period]['forecast_acc']
                period++
            }

            my_data = new GoogleChartData(my_data)
            my_data->setColor('FF99FF')
            my_data->setLegend('Forecast Accuracy')
            my_data->setAutoscale(false)
            my_data->setScale(0, 1)
            chart->addData(my_data)

            #add a shape marker with a border
            shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
            shape_marker->setSize(6)
            shape_marker->setBorder(2)
            shape_marker->setColor('0000FF')
            shape_marker->setData(my_data)
            chart->addMarker(shape_marker)

            #add a value marker
            value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
            value_marker->setColor('0000FF')
            value_marker->setData(my_data)
            chart->addMarker(value_marker)
            return(chart)
        

        def drawSmoothedAccuracy(self, chart, joint_data, current_period, MIN, MAX, tConnection):
        
            global smoothed_accuracy_data
            
            period = 1
            my_data = ""
            while (period < current_period) {
                my_data[] = joint_data[period]['smoothed_acc']
                smoothed_accuracy_data[] = joint_data[period]['smoothed_acc']
                period++
            }

            my_data = new GoogleChartData(my_data)
            my_data->setColor('330033')
            my_data->setLegend('Smoothed Accuracy')
            my_data->setAutoscale(false)
            my_data->setScale(0, 1)
            chart->addData(my_data)

            #add a shape marker with a border
            shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
            shape_marker->setSize(6)
            shape_marker->setBorder(2)
            shape_marker->setColor('0000FF')
            shape_marker->setData(my_data)
            chart->addMarker(shape_marker)

            #add a value marker
            value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
            value_marker->setColor('0000FF')
            value_marker->setData(my_data)
            chart->addMarker(value_marker)
            return(chart)

        def drawServiceLevel(self, chart, data, current_period, tConnection):
        
            global service_level_data
            
            period = 1
            my_data = ""
            #echo "NOT HERE\n"
            while (period < current_period) {
                #echo "HERE\n"
                my_data[] = data[period]['service_level']
                service_level_data[] = data[period]['service_level']
                #echo "P = period sl = ", data[period]['service_level'], "\n"
                period++
            }


            my_data = new GoogleChartData(my_data)
            my_data->setColor('990099')
            my_data->setLegend('Service Level')
            my_data->setAutoscale(false)
            my_data->setScale(0, 1)
            chart->addData(my_data)

            #add a shape marker with a border
            shape_marker = new GoogleChartShapeMarker(GoogleChartShapeMarker::CIRCLE)
            shape_marker->setSize(6)
            shape_marker->setBorder(2)
            shape_marker->setColor('0000FF')
            shape_marker->setData(my_data)
            chart->addMarker(shape_marker)

            #add a value marker
            value_marker = new GoogleChartTextMarker(GoogleChartTextMarker::VALUE)
            value_marker->setColor('0000FF')
            value_marker->setData(my_data)
            chart->addMarker(value_marker)
            return(chart)

# The point of this def is to predetermine the maximum and minimum values that will
# be used by all the various points of data plotted for the specified user settings.
# The reason we are doing this ahead of time before actually drawing the data is due
# to a limitation in the Google Charts API. The bounds must be specified at the time
# the data is added and autoresizing does not take place.

    def findMaxMin(self, buyerData, current_period, link_id, supplier_id, joint_data, tConnection):
        MAX = 0
        MIN = 0

        all_data = []
        if (IsChecked('dataDisplay', 'Profit')) {
            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['profit']
                period++
            }
        }
        if (IsChecked('dataDisplay', 'CumulativeProfit')) {
            period = 1
            total_profit = 0
            while (period < current_period) {
                total_profit = total_profit + buyerData[period]['profit']
                all_data[] = total_profit
                period++
            }
        }

        if (IsChecked('dataDisplay', 'inventory')) {
            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['inventory']
                period++
            }
        }

        if (IsChecked('dataDisplay', 'Backlog')) {
            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['backlog']
                period++
            }
        }
        if (IsChecked('dataDisplay', 'Orders')) {
            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['total_order']
                period++
            }
        }
        if (IsChecked('dataDisplay', 'ReceivedShipment')) {
            period = 1
            while (period < current_period) {
                all_data[] = joint_data[period]['shipment']
                period++
            }
        }
        if (IsChecked('dataDisplay', 'Sales')) {
            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['sales']
                period++
            }
        }
        if (IsChecked('dataDisplay', 'Revenue')) {
            user_sql = "SELECT retail_price FROM Buyer_Settings WHERE link_id = link_id"
            user_result = odbc_exec(tConnection, user_sql)
            buyer_settings = odbc_fetch_array(user_result)  #grab first row
            retail_price = buyer_settings['retail_price']

            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['sales'] * retail_price
                period++
            }
        }
        if (IsChecked('dataDisplay', 'PurchaseCost')) {
            user_sql = "SELECT wholesale_price FROM Supplier_Settings WHERE link_id = supplier_id"
            user_result = odbc_exec(tConnection, user_sql)
            buyer_settings = odbc_fetch_array(user_result)  #grab first row
            wholesalePrice = buyer_settings['wholesale_price']

            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['sales'] * wholesalePrice
                #echo "P = period profit = ", data[period]['profit'], "\n"
                period++
            }
        }

        if (IsChecked('dataDisplay', 'BacklogCost')) {
            user_sql = "SELECT backlog_cost FROM Buyer_Settings WHERE link_id = link_id"
            user_result = odbc_exec(tConnection, user_sql)
            buyer_settings = odbc_fetch_array(user_result)  #grab first row
            backlogCost = buyer_settings['backlog_cost']

            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['backlog'] * backlogCost
                #echo "P = period profit = ", data[period]['profit'], "\n"
                period++
            }
        }

        if (IsChecked('dataDisplay', 'HoldingCost')) {

            user_sql = "SELECT holding_cost FROM Buyer_Settings WHERE link_id = link_id"
            user_result = odbc_exec(tConnection, user_sql)
            buyer_settings = odbc_fetch_array(user_result)  #grab first row
            holdingCost = buyer_settings['holding_cost']

            period = 1
            while (period < current_period) {
                all_data[] = buyerData[period]['inventory'] * holdingCost
                #echo "P = period profit = ", data[period]['profit'], "\n"
                period++
            }
        }

        for (i = 0 i < count(all_data) i++) {
            if (MAX < all_data[i]) {
                MAX = all_data[i]
            }
            if (MIN > all_data[i]) {
                MIN = all_data[i]
            }
        }

# This def is an attempt to determine the labels that go along the left most axis
# The method here is to use the minimum and maximum values determined earlier as the
# bounds and then create 5 marks in between them.

    def generateLabelArray(self, MIN, MAX, tConnection):
        difference = MAX - MIN
        #echo "diff = difference\n"
        scale = difference / 5
        values = []
        for i in [MIN, MAX+scale]:
        #= MIN i < MAX i = i + scale:
            values.append(i)
        values.append(MAX)
        return(values)       

    def checkedAll(all_checkboxes):
        var aa= document.getElementById('all_checkboxes')
        if checked is False:
                {
                    checked = true
                }
                else
                {
                    checked = false
                }
                for (var i =0 i < aa.elements.length i++) 
                {
                    aa.elements[i].checked = checked
                }
            }
# The chart is 700 pixels by 400 pixels. However, we scale it up later using CSS.
# Note the API will break if the image is much larger than this!!!!

    chart = new GoogleChart('lc', 700, 400)
    chart->setLegendPosition('b')
    chart->setAutoscale(false)
    chart->setTitle("Buyer Data", '000000', 16)


#required for determining the scale
#We predetermine the MAX MIN values across all data used and then pass this data into
#each chart that is generated
    findMaxMin(buyerdata, current_period, link_id, supplier_id, joint_data, connection)

    if (IsChecked('dataDisplay', 'Profit')) {
        chart = drawProfit(chart, buyerdata, current_period, MIN, MAX, connection)
    }
    if (IsChecked('dataDisplay', 'CumulativeProfit')) {
        chart = drawCumulativeProfit(chart, buyerdata, current_period, MIN, MAX, connection)
    }

    if (IsChecked('dataDisplay', 'Service')) {
        chart = drawServiceLevel(chart, buyerdata, current_period, connection)
    }
    if (IsChecked('dataDisplay', 'Inventory')) {
        chart = drawInventory(chart, buyerdata, current_period, MIN, MAX, connection)
    }
    if (IsChecked('dataDisplay', 'BacklogCost')) {
        chart = drawBacklogCost(chart, buyerdata, current_period, MIN, MAX, link_id, connection)
    }
    if (IsChecked('dataDisplay', 'Backlog')) {
        chart = drawBacklog(chart, buyerdata, current_period, MIN, MAX, link_id, connection)
    }
    if (IsChecked('dataDisplay', 'HoldingCost')) {
        chart = drawHoldingCost(chart, buyerdata, current_period, MIN, MAX, link_id, connection)
    }
    if (IsChecked('dataDisplay', 'Orders')) {
        chart = drawOrders(chart, buyerdata, current_period, MIN, MAX, link_id, connection)
    }
    if (IsChecked('dataDisplay', 'PurchaseCost')) {
        chart = drawPurchaseCost(chart, buyerdata, joint_data, current_period, MIN, MAX, link_id, supplier_id, connection)
    }
    if (IsChecked('dataDisplay', 'ReceivedShipment')) {
        chart = drawReceivedShipment(chart, joint_data, current_period, MIN, MAX, connection)
    }
    if (IsChecked('dataDisplay', 'Sales')) {
        chart = drawSales(chart, buyerdata, current_period, MIN, MAX, connection)
    }
    if (IsChecked('dataDisplay', 'Revenue')) {
        chart = drawRevenue(chart, buyerdata, current_period, MIN, MAX, link_id, connection)
    }
    if (IsChecked('dataDisplay', 'ForecastAccuracy')) {
        chart = drawForecastAccuracy(chart, joint_data, current_period, MIN, MAX, connection)
    }
    if (IsChecked('dataDisplay', 'SmoothedAccuracy')) {
        chart = drawSmoothedAccuracy(chart, joint_data, current_period, MIN, MAX, connection)
    }


#Here we setup the axis along the bottom, left and right
#customize y axis
    y_axis = new GoogleChartAxis('y')
    build_y_label = generateLabelArray(MIN, MAX, connection)
    y_axis->setDrawTickMarks(false)->setLabels(build_y_label)
#y_axis->setDrawTickMarks(false)->setRange()
#y_axis->setTickMarks(10)
    y_axis->setDrawTickMarks(true)
    chart->addAxis(y_axis)

#customize x axis
    x_axis = new GoogleChartAxis('x')
    x_axis->setTickMarks(5)
    x_axis->setlabels(range(1, current_period - 1))
    chart->addAxis(x_axis)

    r_axis = new GoogleChartAxis('r')
    r_axis->setTickMarks(5)
    r_axis->setlabels(array(0, 0.2, 0.4, 0.6, 0.8, 1))
    r_axis->setlabelColor('0000FF')
    chart->addAxis(r_axis)


#This part of the code sets up the submission form
/*
        echo "<div id=\"main_image\">\n"
        if (isset(_GET['debug'])) {
            var_dump(chart->getQuery())
            printf('<iframe src="%s" ></iframe>', chart->getValidationUrl())
            echo chart->toHtml()
        } else {
            #header('Content-Type: image/png')
            echo chart->toHtml()
        }
*/
        echo "</div>\n"
        echo "<div id=\"plot_target\">\n"
        echo "</div>\n"

        <div id="checkbox_container">
            <form id="all_checkboxes" action="<?php echo "graph_buyer.new.php?uid=".user_id."&gid=".game_id ?>" method="post">
                <table id="checkbox_layout">
                    <tr><td colspan="6">Specify data to display?</td></tr>
                    <tr>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Profit"  <?php if (IsChecked('dataDisplay', 'Profit')) echo "checked" ?> >Profit</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Revenue" <?php if (IsChecked('dataDisplay', 'Revenue')) echo "checked" ?> >Revenue</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="PurchaseCost" <?php if (IsChecked('dataDisplay', 'PurchaseCost')) echo "checked" ?> >Purchase Cost</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Inventory" <?php if (IsChecked('dataDisplay', 'Inventory')) echo "checked" ?> >Inventory</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Service" <?php if (IsChecked('dataDisplay', 'Service')) echo "checked" ?> >Service Level</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Orders" <?php if (IsChecked('dataDisplay', 'Orders')) echo "checked" ?> />Orders</input></td>
                    </tr>
                    <tr>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="CumulativeProfit"  <?php if (IsChecked('dataDisplay', 'CumulativeProfit')) echo "checked" ?> >Cumulative Profit</input></td>
                        <td></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="HoldingCost" <?php if (IsChecked('dataDisplay', 'HoldingCost')) echo "checked" ?> >Holding Cost</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Backlog" <?php if (IsChecked('dataDisplay', 'Backlog')) echo "checked" ?> >Backlog</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="ForecastAccuracy" <?php if (IsChecked('dataDisplay', 'ForecastAccuracy')) echo "checked" ?> >Forecast Accuracy</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="ReceivedShipment" <?php if (IsChecked('dataDisplay', 'ReceivedShipment')) echo "checked" ?> />Received Shipment</input></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="BacklogCost" <?php if (IsChecked('dataDisplay', 'BacklogCost')) echo "checked" ?> >Backlog Cost</input></td>
                        <td></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="SmoothedAccuracy" <?php if (IsChecked('dataDisplay', 'SmoothedAccuracy')) echo "checked" ?> >Smoothed Accuracy</input></td>
                        <td><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Sales" <?php if (IsChecked('dataDisplay', 'Sales')) echo "checked" ?> />Sales</input></td>
                    </tr>
                    <tr>
                    </tr>

                    <tr><td colspan="6"><input type='checkbox' name='checkall' onclick='checkedAll(all_checkboxes)'>Select/Unselect All</input></td></tr>
                    <tr><td colspan="6">(Note: A maximum of 10 lines can be displayed)</td></tr>
                    <tr><td colspan="6"><input type="submit" name="formSubmit" value="Refresh" /></td></tr>
                </table>
                
                <ul>
                    <li><ul>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Profit"  <?php if (IsChecked('dataDisplay', 'Profit')) echo "checked" ?> >Profit</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Revenue" <?php if (IsChecked('dataDisplay', 'Revenue')) echo "checked" ?> >Revenue</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="PurchaseCost" <?php if (IsChecked('dataDisplay', 'PurchaseCost')) echo "checked" ?> >Purchase Cost</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Inventory" <?php if (IsChecked('dataDisplay', 'Inventory')) echo "checked" ?> >Inventory</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Service" <?php if (IsChecked('dataDisplay', 'Service')) echo "checked" ?> >Service Level</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Orders" <?php if (IsChecked('dataDisplay', 'Orders')) echo "checked" ?> />Orders</input></li>
                    </ul></li>
                    <li><ul>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="CumulativeProfit"  <?php if (IsChecked('dataDisplay', 'CumulativeProfit')) echo "checked" ?> >Cumulative Profit</input></li>
                        <li></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="HoldingCost" <?php if (IsChecked('dataDisplay', 'HoldingCost')) echo "checked" ?> >Holding Cost</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Backlog" <?php if (IsChecked('dataDisplay', 'Backlog')) echo "checked" ?> >Backlog</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="ForecastAccuracy" <?php if (IsChecked('dataDisplay', 'ForecastAccuracy')) echo "checked" ?> >Forecast Accuracy</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="ReceivedShipment" <?php if (IsChecked('dataDisplay', 'ReceivedShipment')) echo "checked" ?> />Received Shipment</input></li>
                    </ul></li>
                    <li><ul>
                        <li></li>
                        <li></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="BacklogCost" <?php if (IsChecked('dataDisplay', 'BacklogCost')) echo "checked" ?> >Backlog Cost</input></li>
                        <li></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="SmoothedAccuracy" <?php if (IsChecked('dataDisplay', 'SmoothedAccuracy')) echo "checked" ?> >Smoothed Accuracy</input></li>
                        <li><input class="checkbox" type="checkbox" name="dataDisplay[]" value="Sales" <?php if (IsChecked('dataDisplay', 'Sales')) echo "checked" ?> />Sales</input></li>
                    </ul></li>
                </ul>
            </form>
        </div>

        
    def make_array(self, name, values):
        separator = ""
        for values in value:
            separator.value
            separator = ", "


    # make_array("backlog", backlog_data)
    # make_array("holding_cost", holding_cost_data)
    # make_array("backlog_cost", backlog_cost_data)
    # make_array("inventory", inventory_data)
    # make_array("profit", profit_data)
    # make_array("cumulative_profit", cumulative_profit_data)
    # make_array("service_level", service_level_data)
    # make_array("orders", orders_data)
    # make_array("purchase_cost", purchase_cost_data)
    # make_array("received_shipments", received_shipments_data)
    # make_array("sales", sales_data)
    # make_array("revenue", revenue_data)
    # make_array("forecast_accuracy", forecast_accuracy_data)
    # make_array("smoothed_accuracy", smoothed_accuracy_data)
    
    # tCurrentPeriod = current_period



        var plot_data = new Array()
        if(backlog_cost.length > 0) { plot_data.push(backlog_cost) }
        if(holding_cost.length > 0) { plot_data.push(holding_cost) }
        if(backlog.length > 0) { plot_data.push(backlog) }
        if(inventory.length > 0) { plot_data.push(inventory) }
        if(profit.length > 0) { plot_data.push(profit) }
        if(cumulative_profit.length > 0) { plot_data.push(cumulative_profit) }
        if(service_level.length > 0) { plot_data.push(service_level) }
        if(orders.length > 0) { plot_data.push(orders) }
        if(purchase_cost.length > 0) { plot_data.push(purchase_cost) }
        if(received_shipments.length > 0) { plot_data.push(received_shipments) }
        if(sales.length > 0) { plot_data.push(sales) }
        if(revenue.length > 0) { plot_data.push(revenue) }
        if(forecast_accuracy.length > 0) { plot_data.push(forecast_accuracy) }
        if(smoothed_accuracy.length > 0) { plot_data.push(smoothed_accuracy) }
        
        var tTicks = new Array()
        tTicks.push(0)
        var tHeaderRow = ("#header_row")
        for(i = 1 i < tCurrentPeriod i++) 
        {
            tTicks.push(i)
            var tString = "<td><h2>" + i.toString() + "</h2></td>"
            tHeaderRow.append(tString)
        }
        tTicks.push(i)
        
        var tBody = ("#data_table tbody")
        if(backlog_cost.length > 0) 
        {
            tBody.append("<tr>")
            tBody.append("<td class=\"first_column\">" + "Backlog Cost" + "</td>")
            for(i in backlog_cost)
            {
                var tCell
                tCell="<td class=\"inner_column\">" + backlog_cost[i] + "</td>"
                tBody.append(tCell)
            }
            tBody.append("</tr>")
        }
        
        .jqplot('plot_target', plot_data,
            {
                title: "Buyer Data",
                seriesDefaults: { showMarker: true, pointLabels: { show:true }},
                grid: {
                    drawGridLines: true,        #wether to draw lines across the grid or not.
                    gridLineColor: '#cccccc',    #**Color of the grid lines.
                    background: '#FFFF99',      #CSS color spec for background color of grid.
                    borderColor: '#999999',     #CSS color spec for border around grid.
                    borderWidth: 2.0,           #pixel width of border around grid.
                    shadow: true,               #draw a shadow for grid.
                    shadowAngle: 45,            #angle of the shadow.  Clockwise from x axis.
                    shadowOffset: 1.5,          #offset from the line of the shadow.
                    shadowWidth: 3,             #width of the stroke for the shadow.
                    shadowDepth: 3,             #Number of strokes to make when drawing shadow.  
                                                #Each stroke offset by shadowOffset from the last.
                    shadowAlpha: 0.07,           #Opacity of the shadow
                    renderer: .jqplot.CanvasGridRenderer,  #renderer to use to draw the grid.
                    rendererOptions: {}         #options to pass to the renderer.  Note, the default
                                                #CanvasGridRenderer takes no additional options.
                },
                axes: {
                    xaxis: {
                        ticks: tTicks,
                        pad: 1.2
                    }
                },
                highlighter: {
                    show: true,
                    sizeAdjust: 10,         
                    tooltipLocation: 'n',         
                    tooltipAxes: 'y',         
                    tooltipFormatString: '<b><i><span style="color:red">value:  %i</span></i></b>',         
                    useAxesFormatters: false     
                },     
                cursor: { show: true }
