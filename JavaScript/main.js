number0 = document.getElementById('number1');
number1 = document.getElementById('number2');
number2 = document.getElementById('number3');
number3 = document.getElementById('number4');
number4 = document.getElementById('number5');
number5 = document.getElementById('number6');
number6 = document.getElementById('number7');
number7 = document.getElementById('number8');
number8 = document.getElementById('number9');
h2 = document.querySelector('.h2')

elements = []
elements.push(number0);
elements.push(number1);
elements.push(number2);
elements.push(number3);
elements.push(number4);
elements.push(number5);
elements.push(number6);
elements.push(number7);
elements.push(number8);

window.addEventListener('load', insertNumbers)

function insertNumbers(){
    var list = ['0', '1', '2', '3', '4', '5','6', '7', '8']
    var shuffled = list.sort(() => Math.random() - 0.5)

    console.log(shuffled)

    number0.textContent = shuffled[0]
    number1.textContent = shuffled[1]
    number2.textContent = shuffled[2]
    number3.textContent = shuffled[3]
    number4.textContent = shuffled[4]
    number5.textContent = shuffled[5]
    number6.textContent = shuffled[6]
    number7.textContent = shuffled[7]
    number8.textContent = shuffled[8]

    setTimeout(function(){
        number0.textContent = '*'
        number1.textContent = '*'
        number2.textContent = '*'
        number3.textContent = '*'
        number4.textContent = '*'
        number5.textContent = '*'
        number6.textContent = '*'
        number7.textContent = '*'
        number8.textContent = '*'
        analiseNumbers()
        }, 10000)

    var firsttime = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']

    console.log(firsttime)

    var spans = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

    function analiseNumbers(){  

        h2.textContent = 'Você se lembra? Clique nos quadrados e tente!'

        number0.addEventListener('click', function(){
            if (firsttime[0] === 'y'){
                i = number0; runApp(); firsttime[0] = 'n'}
            else{
            }})
        number1.addEventListener('click', function(){
            if (firsttime[1] === 'y'){
                i = number1; runApp(); firsttime[1] = 'n'}
            else{
        }})
        number2.addEventListener('click', function(){
            if (firsttime[2] === 'y'){
                i = number2; runApp(); firsttime[2] = 'n'}            
            else{
        }})
        number3.addEventListener('click', function(){
            if (firsttime[3] === 'y'){
                i = number3; runApp(); firsttime[3] = 'n'}  
            else{
        }})
        number4.addEventListener('click', function(){
            if (firsttime[4] === 'y'){
                i = number4; runApp(); firsttime[4] = 'n'}  
            else{
            }})
        number5.addEventListener('click', function(){
            if (firsttime[5] === 'y'){
                i = number5; runApp(); firsttime[5] = 'n'}  
            else{
            }})
        number6.addEventListener('click', function(){
            if (firsttime[6] === 'y'){
                i = number6; runApp(); firsttime[6] = 'n'}  
            else{
            }})
        number7.addEventListener('click', function(){
            if (firsttime[7] === 'y'){
                i = number7; runApp(); firsttime[7] = 'n'}  
            else{
        }})
        number8.addEventListener('click', function(){
            if (firsttime[8] === 'y'){
                i = number8; runApp(); firsttime[8] = 'n'}  
        else{
        }})

        function runApp(){
            var position = elements.indexOf(i) 
            var chute = prompt('Qual número estava aqui?')
            if(chute === shuffled[position]){
                i.textContent = chute;
                spans.push(chute)
                spans.sort().reverse().pop()
                if (spans.indexOf('*') == -1){
                    alert('YOU WON!')
                    if (confirm("Reiniciar?")){
                        insertNumbers()
                    }
                }
                else{
                    analiseNumbers()       
                }
            }
            if (chute !== shuffled[position]){
                alert('Erro!')
                insertNumbers() 
            }
            }
        
    }
}