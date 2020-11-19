<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Músicas</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
	
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="styles.css">
	<link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="jumbotron">
            <h3>Compositor de Músicas <a href="https://openai.com/blog/gpt-2-1-5b-release/">Gpt2</a></h3>

            <p class="lead">MVP desenvolvido durante o Hackathon Code/Stage Sony</p>            
          </div>
		<form id="gen-form">
        <div class="row">
			<div class="col-sm">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Título</h5>
                    </div>
                    <div class="card-body">
                        <p class="card-text">Título da música sendo criada.</p>
                        <input id="titulo" type="text" value="O Vento"/>                          
                    </div>
                </div>  
            </div>
            <div class="col-sm">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Início da Música</h5>
                    </div>
                    <div class="card-body">
                        <p class="card-text">Começa a música com o texto escolhido <br>(Máx 500 caracteres).</p>
                        <textarea class="form-control" id="prefix" rows="4">Posso ouvir o vento passar&#13;Assistir a onda bater&#13;Mas o estrago que faz&#13;A vida é curta pra ver</textarea>
                    </div>
                </div>  
            </div>

            <div class="col-sm">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Tamanho texto gerado</h5>
                    </div>
                    <div class="card-body">
                        
                        <p class="card-text">Número de palavras geradas pelo gpt2 <br>(Máx 120).</p>
                        <input id="length" class="border-0" type="range" min="0" max="120" />  
                        <span class="font-weight-bold text-primary ml-2 mt-1 valueSpan"></span>
                    
                    </div>
                    
                </div>  
            </div>

            <div class="col-sm">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Criatividade</h5>
                    </div>
                    <div class="card-body">
                        <p class="card-text">Controla o índice de criatividade da gpt2. <br> (Máx 100)</p>
                        <input id="temperature" class="border-0" type="range" min="0" max="100" />  
                        <span class="font-weight-bold text-primary ml-2 mt-1 valueSpanCriatividade"></span>
                    </div>
                </div>  
			</div>
			
            
        </div>
		<button type="submit" class="btn btn-primary" id="generate-text">Gerar Música</button>
	</form>
		
           	<div class="row" style="display: block; margin-bottom: 1em;">
			   <div id="summernote">Letras de músicas geradas artificialmente</div>
			</div> 
			
    </div>
	<script type="text/javascript">
    
	const base_url = "https://gpt2-compositor-eroai6oftq-ue.a.run.app/"
	// const base_url = "http://localhost:8080/mock"
    var form = document.getElementById("gen-form");
	form.addEventListener("submit", sendRequest, true);

	

	$(function() {
        const $valueSpan = $('.valueSpan');
        const $value = $('#length');
        $valueSpan.html($value.val());
        $value.on('input change', () => {
            $valueSpan.html($value.val());
        });

		const $valueSpanCriatividade = $('.valueSpanCriatividade');
        const $valueCriatividade = $('#temperature');
        $valueSpanCriatividade.html($valueCriatividade.val());
        $valueCriatividade.on('input change', () => {
            $valueSpanCriatividade.html($valueCriatividade.val());
        });

		
		// $('#gen-form').submit(function (e) {
			// e.preventDefault();
		// 	$.ajax({
		// 		url: "http://localhost:8080/mock",
		// 		type: 'POST',
		// 		dataType: 'json',
		// 		data: {
		// 			'email': 'test@gmail.com'
		// 		},
		// 		success: function(data) {
		// 			return data;
		// 		}
		// 	});
			// $.ajax({
			// 	type: "POST",
			// 	url: "http://localhost:8080/mock",
			// 	// url: "https://gpt2-compositor-eroai6oftq-ue.a.run.app/",
			// 	dataType: "json",
			// 	data: {"titulo": "o vento",	"length": 100, "temperature": 0.8, "prefix": "Meu amor", "truncate": "."},
			// 	beforeSend: function (data) {
			// 	$('#generate-text').addClass("is-loading");
			// 	$('#generate-text').prop("disabled", true);
			// 	},
			// 	success: function (data) {
			// 	$('#generate-text').removeClass("is-loading");
			// 	$('#generate-text').prop("disabled", false);
			// 	$('#tutorial').remove();
			// 	console.log(JSON.stringify(getInputValues()))
			// 	console.log(data)
			// 	var gentext = data.text;
			// 	if ($("#prefix").length & $("#prefix").val() != '') {
			// 		var pattern = new RegExp('^' + $("#prefix").val(), 'g');
			// 		var gentext = gentext.replace(pattern, '<strong>' + $("#prefix").val() + '</strong>');
			// 	}

			// 	var gentext = gentext.replace(/\n\n/g, "<div><br></div>").replace(/\n/g, "<div></div>");
			// 	var html = '<div class=\"gen-box\"><h2>'+getInputValues().titulo+'</h2><div></div> ' + gentext + '</div><div class="gen-border"></div>';
						
			// 	$('#summernote').summernote('code', html);
			// 	$('#summernote').summernote({        
        	// 		tabsize: 2,
        	// 		height: 100
			// 	});
			// 	},
			// 	error: function (jqXHR, textStatus, errorThrown) {
			// 	$('#generate-text').removeClass("is-loading");
			// 	$('#generate-text').prop("disabled", false);
			// 	$('#tutorial').remove();
			// 	var html = '<div class="gen-box warning">Houve um erro gerando a letra, por favor tente novamente</div><div class="gen-border"></div>';
			// 	alert(html)
			// 	}
			// });
    	// });
    });
	async function sendRequest(event) {
			event.preventDefault();
			$('#generate-text').addClass("is-loading");
			$('#generate-text').prop("disabled", true);
			try {			
				const response = await axios.post(base_url, getInputValues());
				var gentext = response.data.text;				

				var gentext = gentext.replace(/\n\n/g, "<div><br></div>").replace(/\n/g, "<div></div>");
				var html = '<div class=\"gen-box\"><h2>'+getInputValues().titulo+'</h2><div></div> ' + gentext + '</div><div class="gen-border"></div>';
				console.log(html)		
				$('#summernote').summernote('code', html);
				$('#summernote').summernote({        
        			tabsize: 2,
        			height: 100
				});
			} catch (error) {
				alert("Erro")
				console.error(error);			
			}finally{
				$('#generate-text').removeClass("is-loading");
				$('#generate-text').prop("disabled", false);				
			}
	};
	
	function getInputValues() {
		var inputs = {}
		document.querySelectorAll("input, textarea").forEach(input=>{		
			inputs[input.id] = input.value;
		})	
		return inputs	
  	}
    </script>
</body>
</html>