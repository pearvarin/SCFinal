<!-- do you have an assigned game, or existing game? -->
<!-- if assigned = enter code, reroutes to that game -->
<!-- existing game, pull up that game -->
<!-- if not, match with player -->
<!-- then routes to start game -->

<!-- cross check, see if general manager -->

<template>
	<div class="container">
    <h1 class="text-center">Welcome to the Supply Chain Game!</h1>
    <h2 class ="text-center">You have successfully logged in.
    Do you currently have a game assigned?</h2>

  	<div class="col-md">
      <form @submit.prevent="verCode">
        <!-- <form @submit.prevent="Find Game"> -->
        <div class="form-group">
        	<label for="code">Assigned Game</label>
        	<input type="text" class="form-control" id="code" placeholder="Please provide enter your verification code.">
        	<button class ="btn btn-primary">Enter</button>
        </div>
      </form>

      </div>
      <div class= "row">
      	<button v-on:click="newGame" class = "btn btn-primary">No</button>
			</div>


    <button v-on:click="generalManager" class="btn btn-primary">GeneralManager</button>
	</div>
</template>

<script>
  const $ = window.jQuery // JQuery
  export default {
    code () {
      return { vercode: ''
      }
    },
   	data () {
      return {
        email: '', username: '', password: ''
    }},
  //   created () {
	 //    this.username = sessionStorage.getItem('username')
	 //    console.log(sessionStorage);
	 //        // Setup headers for all requests
	 //    $.ajaxSetup({
	 //      headers: {
	 //        'Authorization': `Token ${sessionStorage.getItem('authToken')}`
	 //      }
	 //    })
	 //    if (this.$route.params.uri) {
	 //      this.joinGameSession()
	 //    }

	 //    setInterval(this.fetchGameSessionHistory, 1000)
  // },

    methods: {
      generalManager(){
        this.$router.push('/general-manager')
      },

      verCode() {
      	// const credentials = {username: this.username, password: this.password}
      	// $.get('http://localhost:8000/auth/xxxxx'. credentials, (vercode) =>{
      	// 	// get auth token
      	// }
       //  $.post('http://localhost:8000/auth/token/create/' => {
       //    sessionStorage.setItem('authToken', data.auth_token)
       //    sessionStorage.setItem('username', this.username)
       //    this.$router.push('/game')
       //  }))
       //  .fail((response) => {
       //    alert(response.responseText)
       //  })
      },

      newGame() {
      	this.$router.push('/game')
      },
    }
}

/*  
  $sql = "SELECT ul.game_id, u.type, u.user_id
  FROM Users2 u, Users_Link ul 
  WHERE u.user_id = '".$id."'
  AND u.user_id = ul.user_id
  AND ul.game_id = (SELECT MAX(ul.game_id) FROM Users2 u, Users_Link ul WHERE u.user_id = '".$id."' AND u.user_id = ul.user_id)";
  
  //echo $sql;
  
  $result = odbc_exec($connection, $sql);
  $row = odbc_fetch_array($result);
  $_SESSION['user_id'] = $id;
  $_SESSION['game_id'] = $row['game_id'];
  
  if(isset($_SESSION['game_id']))
  {
    $game_id = $_SESSION['game_id'];
    
    $sql = "SELECT gstate.current_period, gsett.num_periods 
    FROM Game_Settings gsett, Game_State gstate
    WHERE gsett.game_id = $game_id
    AND gsett.game_id = gstate.game_id";
    $result =  odbc_exec($connection, $sql);
    $row =odbc_fetch_array($result);
    $current_period = $row['current_period'];
    $num_periods = $row['num_periods'];
    //Lastly, we need to set the game_id to null if this game is over.
    if($current_period>$num_periods)
      $_SESSION['game_id']=NULL;
  }
  //echo $player_type;
  
  switch($player_type)
  {
    case NULL:
      echo "
          <script>
            window.alert('You have not been assigned to a game yet.')
            history.go(-1)
          </script>
        ";    
      break;
    case 0:
    //Here we'll create the server switch between games for the game master
      echo "<meta http-equiv='refresh' content='0;url=gm_game_manager.php'>";
      break;
    case 1:
      if (!is_null($_SESSION['game_id']))
        echo "<meta http-equiv='refresh' content='0;url=b_game.php'>";
      else
      {
        echo "
          <script>
            window.alert('You have not been assigned to a game yet.')
            history.go(-1)
          </script>
        ";
      }
      break;
    case 2:
      if (!is_null($_SESSION['game_id']))
        echo "<meta http-equiv='refresh' content='0;url=s_game.php'>";
      else
      {
        echo "
          <script>
            window.alert('You have not been assigned to a game yet.')
            history.go(-1)
          </script>
        ";  
      }
      break;
    default:  
      echo "
          <script>
            window.alert('You have not been assigned to a game yet.')
            history.go(-1)
          </script>
        ";    
      break;
  } 
?>

*/
// 
</script>

<style>
</style>