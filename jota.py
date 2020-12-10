	let object1 = document.getElementById('objeto'),
			obj1 = new Objeto(object1, 0, 0, 0, 0, 1);
			obj1 = new Objeto(object1, 0, 0, 0, 0, 1);

		function Objeto(objeto, dirX, dirY, posX, posY, vel) {
			this.objeto = objeto;
			this.dirX = dirX;
			this.dirY = dirY;
			this.posX = posX;
			this.posY = posY;
			this.vel = vel;

			this.getDirX = function() {
				return this.dirX;
			}

			this.getDirY = function() {
				return this.dirY;
			}

			this.getPosX = function() {
				return this.posX;
			}

			this.getPosY = function() {
				return this.posY;
			}

			this.getVel = function() {
				return this.vel;
			}

			this.getObj = function() {
				return this.objeto;
			}


			this.setDirX = function(dx) {
				this.dirX = dx;
			}

			this.setDirY = function(dy) {
				this.dirY = dy;
			}

			this.setPosX = function(px) {
				this.posX = px;
			}

			this.setPosY = function(py) {
				this.posY = py;
			}

			this.setVel = function(vel) {
				this.vel = vel;
			}

			this.setProperty = function() {
				return this.objeto.style;
			}

			this.setPosition = function(posX, posY) {

				this.objeto.style.transform = `translate(${posX}px, ${posY}px)`;
			}
		}

		


		function keyPress(e, flag) {
			let tecla = e.keyCode;
			switch(tecla) {

				case 37: case 65: {

					if(flag) {
						obj1.setDirX(-1);
					} else {
						obj1.setDirX(0);
					}

					break;
				}

				case 38: case 87: {

					if(flag) {
						obj1.setDirY(-1);
					} else {
						obj1.setDirY(0);
					}

					break;
				}

				case 39: case 68:{

					if(flag) {
						obj1.setDirX(1);
					} else {
						obj1.setDirX(0);
					}

					break;
				}

				case 40: case 83: {

					if(flag) {
						obj1.setDirY(1);
					} else {
						obj1.setDirY(0);
					}

					break;
				}
			}
		}

		function frame() {
			let posX = obj1.getPosX(),
				posY = obj1.getPosY(),
				dirX = obj1.getDirX(),
				dirY = obj1.getDirY(),
				vel  = obj1.getVel();

			obj1.setPosX(posX + (dirX * vel));
			obj1.setPosY(posY + (dirY * vel));

			obj1.setPosition(obj1.getPosX(), obj1.getPosY());
		}

		let body = document.body;

		body.addEventListener("keydown", function() {

			keyPress(event, 1);
		});

		body.addEventListener("keyup", function() {
			keyPress(event, 0);
		});

		setInterval(frame, 1);

 let e1 = document.getElementById('e1');
        let e2 = document.getElementById('e2')
        let e3 = document.getElementById('e3');
        let e4 = document.getElementById('e4')
        let e5 = document.getElementById('e5');
        let e6 = document.getElementById('e6');
        
        let numero 

        let personagem1 
        let personagem2
        let min = 1
        let max = 5


        function joojs() {
        alert("jooj selecionado")
        personagem1 = "jooj"
        min = Math.ceil(min);
        max = Math.floor(max);
        numero = Math.floor(Math.random() * (max - min)) + min;
        if (numero === 1) {
                alert(" cpu = lospe selecionado")
                personagem2 = "jooj"
            }
            else if (numero === 2) {
                alert("cpu = lospe selecionado")
                personagem2 = "finndl"
            }
            else if (numero === 3) {
                alert("cpu = lospe selecionado")
                personagem2 = "mateus"
            }
            else if (numero === 4) {
                alert("cpu = lospe selecionado")
                personagem2 = "bernadino"
            }
            else if (numero === 5) {
                alert("cpu = lospe selecionado")
                personagem2 = "lospe"
            }
        
        
        }
        e1.addEventListener("click", joojs)
        e1.addEventListener("click", eap2)
        function finndls() {
        alert("finndl selecionado")
        personagem1 = "finndl"
        min = Math.ceil(min);
        max = Math.floor(max);
        numero = Math.floor(Math.random() * (max - min)) + min;
        if (numero === 1) {
                alert(" cpu = lospe selecionado")
                personagem2 = "jooj"
            }
            else if (numero === 2) {
                alert("cpu = lospe selecionado")
                personagem2 = "finndl"
            }
            else if (numero === 3) {
                alert("cpu = lospe selecionado")
                personagem2 = "mateus"
            }
            else if (numero === 4) {
                alert("cpu = lospe selecionado")
                personagem2 = "bernadino"
            }
            else if (numero === 5) {
                alert("cpu = lospe selecionado")
                personagem2 = "lospe"
            }
        
        
    
         }
        
        e2.addEventListener("click", finndls)
        e2.addEventListener("click", eap2)
        function mateuss() {
        alert("mateus selecionado")
        personagem1 = "mateus"
        min = Math.ceil(min);
        max = Math.floor(max);
        numero = Math.floor(Math.random() * (max - min)) + min;
        if (numero === 1) {
                alert(" cpu = lospe selecionado")
                personagem2 = "jooj"
            }
            else if (numero === 2) {
                alert("cpu = lospe selecionado")
                personagem2 = "finndl"
            }
            else if (numero === 3) {
                alert("cpu = lospe selecionado")
                personagem2 = "mateus"
            }
            else if (numero === 4) {
                alert("cpu = lospe selecionado")
                personagem2 = "bernadino"
            }
            else if (numero === 5) {
                alert("cpu = lospe selecionado")
                personagem2 = "lospe"
            }
        
        }
        e3.addEventListener("click", mateuss)
        e3.addEventListener("click", eap2)

        function bernadinos() {
        alert("bernadino selecionado")
        personagem1 = "bernadino"
        min = Math.ceil(min);
        max = Math.floor(max);
        numero = Math.floor(Math.random() * (max - min)) + min;
        if (numero === 1) {
                alert(" cpu = lospe selecionado")
                personagem2 = "jooj"
            }
            else if (numero === 2) {
                alert("cpu = lospe selecionado")
                personagem2 = "finndl"
            }
            else if (numero === 3) {
                alert("cpu = lospe selecionado")
                personagem2 = "mateus"
            }
            else if (numero === 4) {
                alert("cpu = lospe selecionado")
                personagem2 = "bernadino"
            }
            else if (numero === 5) {
                alert("cpu = lospe selecionado")
                personagem2 = "lospe"
            }
        
        
        }
        e4.addEventListener("click", bernadinos)
        e4.addEventListener("click", eap2)

        function lospes() {
        alert("lospe selecionado")
        personagem1 = "lospe"
        min = Math.ceil(min);
        max = Math.floor(max);
        numero = Math.floor(Math.random() * (max - min)) + min;
        if (numero === 1) {
                alert(" cpu = lospe selecionado")
                personagem2 = "jooj"
            }
            else if (numero === 2) {
                alert("cpu = lospe selecionado")
                personagem2 = "finndl"
            }
            else if (numero === 3) {
                alert("cpu = lospe selecionado")
                personagem2 = "mateus"
            }
            else if (numero === 4) {
                alert("cpu = lospe selecionado")
                personagem2 = "bernadino"
            }
            else if (numero === 5) {
                alert("cpu = lospe selecionado")
                personagem2 = "lospe"
            }
        
        }
        e5.addEventListener("click", lospes)
        e5.addEventListener("click", eap2)

        function eap2(numero) {

         
            while (personagem1 = personagem2) {
                min = Math.ceil(min);
                max = Math.floor(max);
               numero = Math.floor(Math.random() * (max - min)) + min;
               eap2
               
            }  
        }     
            
        e6.addEventListener("click", eap2)

	