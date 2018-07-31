<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 offset-3">

        <div v-if="sessionStarted" id="chat-container" class="card">
          <div class="card-header text-white text-center font-weight-bold subtle-blue-gradient">
            Share the page URL to access the game (this needs to change)
          </div>

          <div class="card-body">
            <div class="container chat-body">
              <div v-for="message in messages" :key="message.id" class="row chat-section">
                <template v-if="username === message.user.username">
                  <div class="col-sm-7 offset-3">
                    <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                      {{ message.message }} 
                      <!-- this needs to change to order forecasts -->
                    </span>
                  </div>
                  <div class="col-sm-2">
                    <img class="rounded-circle" :src="`http://placehold.it/40/007bff/fff&text=${message.user.username[0].toUpperCase()}`" />
                    <!-- change this -->
                  </div>
                </template>
                <template v-else>
                  <div class="col-sm-2">
                    <img class="rounded-circle" :src="`http://placehold.it/40/333333/fff&text=${message.user.username[0].toUpperCase()}`" />
                  </div>
                  <div class="col-sm-7">
                    <span class="card-text speech-bubble speech-bubble-peer">
                      {{ message.message }}
                      <!-- change to order forecasts -->
                    </span>
                  </div>
                </template>
              </div>
            </div>
          </div>

          <div class="card-footer text-muted">
            <form @submit.prevent= "postMessage">
              <!-- post forecasts? -->
              <div class="row">
                <div class="col-sm-10">
                  <input v-model = "message" type="text" placeholder="Type a message" />
                  <!-- <input v-model = "forecasts" type="text" placeholder="Submit your forecasts" /> -->
                  <!-- submit your forecasts -->
                </div>
                <div class="col-sm-2">
                  <button class="btn btn-primary">Send</button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div v-else>
          <h3 class="text-center">Welcome !</h3>
          <br />
          <p class="text-center">
            To start chatting with friends click on the button below, it'll start a new chat session
            and then you can invite your friends over to chat!
            <!-- change -->
          </p>
          <br />
          <!-- <button @click="startChatSession" class="btn btn-primary btn-lg btn-block">Start Chatting</button> -->
          <button @click="startGameSession" class="btn btn-primary btn-lg btn-block">Start the Game</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const $ = window.jQuery

export default {
  data () {
    return {
      sessionStarted: false,
      messages: [],
      message: '',
      // submissions:[],
      // submission:''
    }
  },
  created () {
    this.username = sessionStorage.getItem('username')
    console.log(sessionStorage);
        // Setup headers for all requests
    $.ajaxSetup({
      headers: {
        'Authorization': `Token ${sessionStorage.getItem('authToken')}`
      }
    })
    if (this.$route.params.uri) {
      this.joinGameSession()
    }

    setInterval(this.fetchGameSessionHistory, 1000)
  },

  methods: {
    startGameSession () {
      this.sessionStarted = true
      this.$router.push('/game/game_url/')
      // this needs to be changed 
       $.post('http://localhost:8000/api/game/', (data) => {
        alert("A new session has been created you'll be redirected automatically")
        this.sessionStarted = true
        this.$router.push(`/game/${data.uri}/`)
      })
      .fail((response) => {
        alert(response.responseText)
      })
    },

    postForecasts (event) {
      const data = {message: this.message} 
      // change to forecasts
      $.post(`http://localhost:8000/api/game/${this.$route.params.uri}/messages/`, data, (data) => {
        this.messages.push(data)
        this.message = '' // clear the message after sending 
        // change
      })
      .fail((response) => {
        alert(response.responseText)
      })
    },

    joinGameSession () {
      const uri = this.$route.params.uri

      $.ajax({
        url: `http://localhost:8000/api/game/${uri}/`,
        data: {username: this.username},
        type: 'PATCH',
        success: (data) => {
          const user = data.members.find((member) => member.username === this.username)

          if (user) {
            // The user belongs/has joined the session
            this.sessionStarted = true
            this.fetchGameSessionHistory()
          }
        }
      })
    },

    fetchGameSessionHistory () {
      $.get(`http://127.0.0.1:8000/api/game/${this.$route.params.uri}/messages/`, (data) => {
        this.messages = data.messages
        // change data
      })
    },
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.btn {
  border-radius: 0 !important;
}

.card-footer input[type="text"] {
  background-color: #ffffff;
  color: #444444;
  padding: 7px;
  font-size: 13px;
  border: 2px solid #cccccc;
  width: 100%;
  height: 38px;
}

.card-header a {
  text-decoration: underline;
}

.card-body {
  background-color: #ddd;
}

.chat-body {
  margin-top: -15px;
  margin-bottom: -5px;
  height: 380px;
  overflow-y: auto;
}

.speech-bubble {
  display: inline-block;
  position: relative;
  border-radius: 0.4em;
  padding: 10px;
  background-color: #fff;
  font-size: 14px;
}

.subtle-blue-gradient {
  background: linear-gradient(45deg,#004bff, #007bff);
}

.speech-bubble-user:after {
  content: "";
  position: absolute;
  right: 4px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-left-color: #007bff;
  border-right: 0;
  border-top: 0;
  margin-top: -10px;
  margin-right: -20px;
}

.speech-bubble-peer:after {
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-right-color: #ffffff;
  border-top: 0;
  border-left: 0;
  margin-top: -10px;
  margin-left: -20px;
}

.chat-section:first-child {
  margin-top: 10px;
}

.chat-section {
  margin-top: 15px;
}

.send-section {
  margin-bottom: -20px;
  padding-bottom: 10px;
}
</style>

/*<?php
  session_start();
  include "dbconn.php";
  include "library.php";
  if($_POST['num_periods']<=0)
  {
    echo("<script>
    window.alert('You have entered an invalid number of periods, please try again.')
    history.go(-1)
    </script>");
    exit;
   }
  if($_POST['lead_time']<=0)
  {
    echo("<script>
    window.alert('You have entered an invalid lead time, please try again.')
    history.go(-1)
    </script>");
    exit;
   }
  if($_POST['exp_smooth_coeff']<=0)
  {
    echo("<script>
    window.alert('You have entered a negative exponential smoothing coefficient, please try again.')
    history.go(-1)
    </script>");
    exit;
   }
  if($_POST['exp_smooth_coeff']>1)
  {
    echo("<script>
    window.alert('You have entered an exponential smoothing coefficient greater than 1, please try again.')
    history.go(-1)
    </script>");
    exit;
   }
  
  if(($_POST['s_Prod_cost_1']<=0) || ($_POST['s_Hold_cost_1']<=0) || ($_POST['s_Whole_price_1']<=0))
   {
    echo("<script>
    window.alert('You have entered an invalid supplier cost or production parameter, please try again.')
    history.go(-1)
    </script>");
    exit;
   }
  for ($i=1; $i <= $_SESSION['num_buyers'] ; $i++) 
  { 
    if(($_POST['b_Hold_cost_'.$i]<0) || ($_POST['b_Backlog_cost_'.$i]<0) || ($_POST['b_Mean_'.$i]<0)
       || ( $_POST['b_Std_'.$i]<0) || ($_POST['b_Retail_price_'.$i]<0))
      {
        echo("<script>
        window.alert('You have entered an invalid buyer ".$i." parameter, please try again.')
        history.go(-1)
        </script>");
        exit;
      }
  }
  for ($i=1; $i <= $_SESSION['num_buyers'] ; $i++) 
  {
    for ($j=0; $j <= $_SESSION['num_suppliers']  ; $j++) 
    { 
      if($_POST['b_user_id_'.$i]==$_POST['s_user_id_'.$j])
      {
        echo("<script>
        window.alert('You have assigned the same user to two roles. Please check the user assignments.')
        history.go(-1)
        </script>");
        exit;
      }
    }
  } 
  
  $game_id = $_SESSION['game_id'];
  
  //Advance the game to period 0
  $gamestate['current_period']=0;
  $gamestate['suppliers_submitted']=1;
  $gamestate['buyers_submitted']=0;
  updatesql($gamestate, "Game_State", "WHERE game_id = ".$game_id, $connection);
  
  //Update the Game Settings Table
  $gamesettings['num_periods'] = $_POST['num_periods'];
  $num_periods = $_POST['num_periods'];
  $gamesettings['lead_time'] = $_POST['lead_time'];
  $lead_time = $_POST['lead_time'];
  $gamesettings['exp_smooth_coeff'] = $_POST['exp_smooth_coeff'];
  updatesql($gamesettings, "Game_Settings", "WHERE game_id = ".$game_id, $connection);
  
  
  //Save Supplier settings
  
  $usertable['type'] = 2;
  for ($i = 1; $i <= $_SESSION['num_suppliers']; $i++)
  {
  
    //update the player into a supplier
    updatesql($usertable, "Users2", "WHERE user_id = ".$_POST['s_user_id_'.$i], $connection);
    
    //insert the user into the game via the Users_Link table
    $suserlink[$i]['game_id'] = $game_id;
    $suserlink[$i]['user_id'] = $_POST['s_user_id_'.$i];
    insertsql($suserlink[$i], "Users_Link", $connection);
    
    //retrieve the link_id just generated
    $link_query = "SELECT link_id FROM Users_Link 
    WHERE user_id = ".$_POST['s_user_id_'.$i]." AND game_id=".$game_id."";
    $link_result =  odbc_exec($connection, $link_query);
    $s_linkid[$i] =  odbc_fetch_array($link_result);
    
    $suppliersettings[$i]['link_id'] = $s_linkid[$i]['link_id'];
    $suppliersettings[$i]['supplier_num'] = $i;
    $suppliersettings[$i]['production_cost'] = $_POST['s_Prod_cost_'.$i];
    $suppliersettings[$i]['holding_cost'] = $_POST['s_Hold_cost_'.$i];
    $suppliersettings[$i]['wholesale_price'] = $_POST['s_Whole_price_'.$i];
    $suppliersettings[$i]['alloc_rule'] = $_POST['s_Alloc_rule_'.$i];
    $suppliersettings[$i]['prod_strat'] = $_POST['s_Prod_strat_'.$i]; 
    $suppliersettings[$i]['automation'] = $_POST['s_automation_'.$i]; 
    insertsql($suppliersettings[$i], "Supplier_Settings", $connection);

    for ($z=0; $z <= $_POST['num_periods']; $z++) 
    {
      $supplierdata['period_id']=$z;
      $supplierdata['link_id']=$s_linkid[$i]['link_id'];
      insertsql($supplierdata, "Supplier_Data", $connection);
    }
    
    //Work is process allocation happens here for the first couple of periods
    $tot_mean = $_SESSION['num_buyers']*$_POST['b_Mean_1'];
    $tot_variance = $_SESSION['num_buyers']*$_POST['b_Std_1']*$_POST['b_Std_1'];
    
    if($_POST['s_Prod_strat_'.$i]==0)
      $safetyZ = -0.97;
    else if($_POST['s_Prod_strat_'.$i]==1)
      $safetyZ = -.17;
    else if($_POST['s_Prod_strat_'.$i]==2)
      $safetyZ = 1.01;
          
    $targetinventory = round($tot_mean + ($safetyZ * sqrt($tot_variance)));
    $supplierproddata['production'] = $targetinventory;
    
    for ($j=1; $j <= $gamesettings['lead_time'] ; $j++) 
    { 
      updatesql($supplierproddata, "Supplier_Data", "WHERE link_id = ".$s_linkid[$i]['link_id']." 
      AND period_id = $j", $connection);
    }
  }
  
  //Save Buyer settings
  $usertable['type'] = 1;
  for ($i = 1; $i <= $_SESSION['num_buyers']; $i++)
  {
    //update the player type to a buyer
    updatesql($usertable, "Users2", "WHERE user_id = ".$_POST['b_user_id_'.$i], $connection);
    
    //insert the user into the game via the Users_Link table
    $buserlink[$i]['game_id'] = $game_id;
    $buserlink[$i]['user_id'] = $_POST['b_user_id_'.$i];
    insertsql($buserlink[$i], "Users_Link", $connection);
    
    //retrieve the link_id just generated
    $link_query = "SELECT link_id FROM Users_Link 
    WHERE user_id = ".$_POST['b_user_id_'.$i]." AND game_id=".$game_id."";
    $link_result =  odbc_exec($connection, $link_query);
    $b_linkid[$i] =  odbc_fetch_array($link_result);
    
    $buyersettings[$i]['link_id'] = $b_linkid[$i]['link_id'];
    $buyersettings[$i]['buyer_num'] = $i;
    $buyersettings[$i]['holding_cost'] = $_POST['b_Hold_cost_'.$i];
    $buyersettings[$i]['backlog_cost'] = $_POST['b_Backlog_cost_'.$i];
    $buyersettings[$i]['retail_price'] = $_POST['b_Retail_price_'.$i];
    $buyersettings[$i]['mean'] = $_POST['b_Mean_'.$i];
    $buyersettings[$i]['s_dev'] = $_POST['b_Std_'.$i];  
    $buyersettings[$i]['gen_rule'] = $_POST['b_gen_rule'.$i]; 
    insertsql($buyersettings[$i], "Buyer_Settings", $connection);
    
    //Generate the demand stream for the whole game for each buyer
    if($_POST['b_gen_rule'.$i]==0)
    {
      for ($z=1; $z <= $_POST['num_periods']; $z++) 
      {
        //$filename = "".($i).".txt";
        $filename = "1.txt";
        $buyerdata['period_id']=$z;
        $buyerdata['link_id']=$b_linkid[$i]['link_id'];
        $buyerdata['demand']= intval(demandfromfile($z, $filename));
        insertsql($buyerdata, "Buyer_Data", $connection);
      }
    }
    else if($_POST['b_gen_rule'.$i]==1)
    {
      //Generate normal distribution here for the whole game for each buyer
    }
  }
  //Write the entire forecast data table so we can update it later.
  for ($a = 1; $a <= $_SESSION['num_buyers']; $a++)
  {
    for ($b = 1; $b <= $_SESSION['num_suppliers']; $b++)
    {
      for ($v=1; $v < $lead_time; $v++) 
      {
        for ($y=1; $y <= $v ; $y++) 
        { 
          $forecastdata['period_id']=$v;
          $forecastdata['supplier_id']=$s_linkid[$b]['link_id'];
          $forecastdata['buyer_id']=$b_linkid[$a]['link_id'];
          $forecastdata['forecast_value']=-1;
          $forecastdata['forecast_num']=$y;
          insertsql($forecastdata, "Forecast_Data", $connection);   
        }
      }
      for ($i=$lead_time; $i <= ($num_periods + $lead_time); $i++) 
      {
        for ($z=1; $z<=$lead_time ; $z++) 
        { 
          $forecastdata['period_id']=$i;
          $forecastdata['supplier_id']=$s_linkid[$b]['link_id'];
          $forecastdata['buyer_id']=$b_linkid[$a]['link_id'];
          $forecastdata['forecast_value']=-1;
          $forecastdata['forecast_num']=$z;
          insertsql($forecastdata, "Forecast_Data", $connection); 
        }
      }
    }
  }
  
  header("Location: ./gm_game.php")
?>*/